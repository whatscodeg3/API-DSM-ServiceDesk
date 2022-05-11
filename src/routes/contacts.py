from sqlalchemy import text, engine
import os
import pathlib
from flask import Blueprint, redirect, render_template, request, session, g, url_for, send_from_directory, current_app
from models.solicita import Avaliacao, Categoria, Solicita, Usuarios
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
        email = request.form['email']
        senha = request.form['senha']
        db_consulta = Usuarios.query.all()
        redir = verifica(db_consulta, email, senha)
        return redirect(url_for(redir))
    return render_template('tela-inicial.html')


@contacts.route('/usuario')
def usuario():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            print(g.id_usuario)
            return render_template('home_usuario.html', user=session['user'])
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


@contacts.route('/historico')
def historico():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 3:
            lista = Solicita.query.all()
            return render_template('usuario-historico.html', listas=lista, user=session['user'])
    session.pop('user', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/demanda')
def demanda():
    if g.user != None:
        if g.user[0] == 2:
            print(g.id_usuario)
            lista = Solicita.query.filter_by(resposta_solicitacao=None)
            consulta = Solicita.query.filter(
                Solicita.resposta_solicitacao.isnot(None))
            return render_template('executor-demandas.html', listas=lista, consultas=consulta, user=session['user'])
    session.pop('user', None)
    return redirect(url_for('contacts.index'))


# @contacts.route('/')
# def index():
#     return render_template('home_usuario.html')

@contacts.route('/admin')
def admin():
    return render_template('home_admin.html')

# @contacts.route('/nova-solicitacao')
# def nova():
#     categoria = Categoria.query.all()
#     return render_template('form_usuario_solicitacao.html', categorias=categoria)

# @contacts.route('/historico')
# def historico():
#     lista = Solicita.query.all()
#     return render_template('usuario-historico.html', listas=lista)

# @contacts.route('/demanda')
# def demanda():
#     lista = Solicita.query.filter_by(resposta_solicitacao = None)
#     consulta = Solicita.query.filter(Solicita.resposta_solicitacao.isnot(None))
#     return render_template('executor-demandas.html', listas=lista, consultas=consulta)


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
    print(id)
    # teste = request.form['1estrela']
    # print(teste)
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
        consulta.fk_id_executor = g.id_usuario
        db.session.commit()
        return redirect('/demanda')

    return render_template('resposta-executor.html', solicita=consulta, arquivo_no_html=file)


@contacts.route('/admin/permissoes')
def testeperm():
    nome = Usuarios.query.all()
    return render_template('adm_permissoes.html', nome=nome)


@contacts.route('/permissoes/<id>', methods=['POST', ])
def attperm(id):
    consultar = Usuarios.query.get(id)
    consultar.id_categoria_usuario = request.form['botao']
    db.session.commit()
    return redirect('/admin/permissoes')
