from multiprocessing.sharedctypes import Value
from sqlalchemy import text, engine
import os
import pathlib
from flask import Blueprint, flash, redirect, render_template, request, session, g, url_for, send_from_directory, current_app
from models.solicita import Avaliacao, Categoria, Solicita, Usuarios
from sqlalchemy import text, engine
from utils.db import db
from utils.verifica import distribui, verifica

contacts = Blueprint('contacts', __name__)

@contacts.before_request
def before_request():
    g.user = None
    g.id_usuario = None  # aqui thiago
    if 'user' in session:
        g.user = session['user']
    if 'id_usuario' in session:  # aqui thiago
        g.id_usuario = session['id_usuario']  # aqui thiago


@contacts.route('/sair')
def sair():
    session.pop('user', None)
    return render_template('tela-inicial.html')

@contacts.route('/')
def index():
    return render_template('tela-inicial.html')

@contacts.route('/autentica', methods=['POST', 'GET'])
def autentica():
    if request.method == 'POST':
        session.pop('user', None)
        session.pop('id_usuario', None) #aqui thiago
        email = request.form['email']
        senha = request.form['senha']
        db_consulta = Usuarios.query.all()
        redir = verifica(db_consulta, email, senha)
        return redirect(url_for(redir))
    return redirect(url_for('contact.index'))
    
@contacts.route('/usuario')
def usuario():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            return render_template('home_usuario.html', user = session['user'])
    session.pop('user', None)     
    return redirect(url_for('contacts.index'))


@contacts.route('/nova-solicitacao')
def nova():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            categoria = Categoria.query.all()
            return render_template('form_usuario_solicitacao.html', categorias=categoria, user=session['user'])
    session.pop('user', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/relatorios')
def relatorio():
    sql1 = text('select count(*) from solicitacoes')
    sql2 = text('select count(*) from solicitacoes where resposta_solicitacao is not null')
    results1 = db.engine.execute(sql1)
    results2 = db.engine.execute(sql2)
    return render_template('relatorios.html', res1=results1, res2=results2)


@contacts.route('/historico')
def historico():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            print(g.id_usuario)
            lista = Solicita.query.filter_by(fk_id_usuario_comum=g.id_usuario)
            return render_template('usuario-historico.html', listas=lista, user=session['user'])
    session.pop('user', None)        
    return redirect(url_for('contacts.index'))


@contacts.route('/demanda')
def demanda():
    if g.user != None:
        if g.user[0] == 2:
            print(g.id_usuario)
            lista = Solicita.query.filter_by(resposta_solicitacao=None, fk_id_executor=g.id_usuario)
            consulta = Solicita.query.filter_by(resposta_solicitacao= not Value, fk_id_executor=g.id_usuario)
            return render_template('executor-demandas.html', listas=lista, consultas=consulta, user=session['user'])
    session.pop('user', None)
    return redirect(url_for('contacts.index'))

@contacts.route('/admin')
def admin():
    return render_template('home_admin.html')


@contacts.route('/resposta')
def resposta():
    return render_template('resposta-executor.html')


@contacts.route('/criar', methods=['POST', ])
def criar():
    tipo = request.form['Tipo de serviço']
    descricao = request.form['descrição do problema']
    id_user = g.id_usuario
    proximo_operador = distribui()
    novo = Solicita(tipo, descricao, id_user, proximo_operador)
    db.session.add(novo)
    db.session.commit()

    arquivo = request.files['arquivo']
    ext = pathlib.Path(arquivo.filename)
    upload_path = current_app.config['UPLOAD_PATH']

    arquivo.save(f'{upload_path}/anexo{novo.id_solicitacao}{ext.suffix}')

    return redirect('/historico')


@contacts.route('/uploads/<nome_arquivo>')
def anexos(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


@contacts.route('/avaliar/<id>', methods=['POST', ])
def avalia(id):
    consulta = Solicita.query.get(id)
    consulta.fk_id_avaliacao = request.form['avaliacao']
    db.session.commit()
    return redirect('/historico')


@contacts.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualiza(id):
    consulta = Solicita.query.get(id)
    upload_path = current_app.config['UPLOAD_PATH']
    termo = f'{id}'
    for raiz, diretorio, arquivos in os.walk(upload_path):
        for arquivo in arquivos:
            if termo in arquivo:
                file = arquivo
    if request.method == "POST":
        consulta.resposta_solicitacao = request.form['resposta']
        db.session.commit()
        return redirect('/demanda')
    return render_template('resposta-executor.html', solicita=consulta, arquivo_no_html=file)


@contacts.route('/admin/permissoes')
def testeperm():
    nome = Usuarios.query.all()
    return render_template('adm_permissoes.html', nome=nome)

@contacts.route('/permissoes/<id>', methods=['POST','GET'])
def attperm(id):
        consultar = Usuarios.query.get(id)
        if consultar.id_categoria_usuario == 2:
            consultar.id_categoria_usuario = 1
            print("Setou OPERADOR pra USUARIO")
            db.session.commit()
            return redirect('/admin/permissoes')
            

        if consultar.id_categoria_usuario == 1:
            consultar.id_categoria_usuario = 2
            print("Setou usuario pra operador")
            db.session.commit()
            return redirect('/admin/permissoes')
            
        return render_template('adm_permissoes.html')

        # return render_template('adm_permissoes.html', consulta=consultar)

@contacts.route('/cadastro')
def cadastro():
    return render_template('tela-cadastro.html')

@contacts.route('/cadastrando', methods=['POST', 'GET'])
def cadastrando():
    if request.method == 'POST':
        nome_usuario = request.form['name']
        sobrenome = request.form.get('surname')
        email_usuario = request.form['email']
        emailConfirmado = request.form.get('emailConfirmation')
        senha_usuario = request.form['password']
        senhaConfirmada = request.form.get('passwordConfirmation')
        dataCheckbox = request.form.get('checkboxData')
    

    if email_usuario != emailConfirmado:
        flash('Email não confere')
        return redirect('/cadastro')
    elif senha_usuario != senhaConfirmada:
        flash('Senha não confere') 
        return redirect('/cadastro')

    # elif dataCheckbox != 'check':
    #     flash('Confirme o uso de dados para continuar o cadastro')
    #     return redirect('/cadastro')
    # elif not nome_usuario or not sobrenome:
    #     flash('Nome ou sobrenome não preenchido')
    #     return redirect('/cadastro')
    # elif not email_usuario:
    #     Flash('Email não preenchido')
    #     return redirect('/cadastro')
    # elif not emailConfirmado:
    #     flash('Confirme seu email')
    #     return redirect('/cadastro')
    # elif not senha_usuario:
    #     flash('Senha não preenchida')
    #     return redirect('/cadastro')
    # elif not senhaConfirmada:
    #     flash('Confirme sua senha')
    #     return redirect('/cadastro')
    id_usuario = None
    usuario = Usuarios(id_usuario, nome_usuario, email_usuario, senha_usuario, 1)
    db.session.add(usuario)
    db.session.commit()
    print(usuario)
   
    return redirect('/')
