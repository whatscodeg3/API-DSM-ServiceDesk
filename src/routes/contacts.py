from multiprocessing.sharedctypes import Value
from xml.etree.ElementPath import ops
from sqlalchemy import false, text, engine
import os
import pathlib
from flask import Blueprint, flash, redirect, render_template, request, session, g, url_for, send_from_directory, current_app
from models.solicita import Avaliacao, Categoria, Solicita, Usuarios, CategoriaUsuarios
from sqlalchemy import text, engine
from utils.db import db
from utils.verifica import distribui, verifica

contacts = Blueprint('contacts', __name__)


@contacts.before_request
def before_request():
    g.user = None
    g.id_usuario = None
    if 'user' in session:
        g.user = session['user']
    if 'id_usuario' in session:
        g.id_usuario = session['id_usuario']

##################################### Inicio #######################################


@contacts.route('/')
def index():
    return render_template('tela-inicial.html')


@contacts.route('/autentica', methods=['POST', 'GET'])
def autentica():
    if request.method == 'POST':
        session.pop('user', None)
        session.pop('id_usuario', None)
        email = request.form['email']
        senha = request.form['senha']
        db_consulta = Usuarios.query.all()
        redir = verifica(db_consulta, email, senha)
        return redirect(url_for(redir))
    return redirect(url_for('contacts.index'))


@contacts.route('/usuario')
def usuario():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            return render_template('home_usuario.html', user=session['user'])
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/nova-solicitacao')
def nova():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            categoria = Categoria.query.all()
            return render_template('form_usuario_solicitacao.html', categorias=categoria, user=session['user'])
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))

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
    if len(arquivo.filename) != 0:

        ext = pathlib.Path(arquivo.filename)

        upload_path = current_app.config['UPLOAD_PATH']

        arquivo.save(f'{upload_path}/anexo{novo.id_solicitacao}{ext.suffix}')

        return redirect('/historico')
    else:
        return redirect('/historico')


@contacts.route('/historico')
def historico():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            print(g.id_usuario)
            lista = Solicita.query.filter_by(fk_id_usuario_comum=g.id_usuario)
            return render_template('usuario-historico.html', listas=lista, user=session['user'])
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/uploads/<nome_arquivo>')
def anexos(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


@contacts.route('/avaliar/<id>', methods=['POST', ])
def avalia(id):
    consulta = Solicita.query.get(id)
    consulta.fk_id_avaliacao = request.form['avaliacao']
    db.session.commit()
    return redirect('/historico')

##################################### Executor #######################################


@contacts.route('/demanda')
def demanda():
    if g.user != None:
        if g.user[0] == 2:
            lista = Solicita.query.filter_by(
                resposta_solicitacao=None, fk_id_executor=g.id_usuario)
            consulta = Solicita.query.filter_by(
                resposta_solicitacao=not Value, fk_id_executor=g.id_usuario)
            return render_template('executor-demandas.html', listas=lista, consultas=consulta, user=session['user'])
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualiza(id):
    consulta = Solicita.query.get(id)
    upload_path = current_app.config['UPLOAD_PATH']
    termo = f'{id}'
    for raiz, diretorio, arquivos in os.walk(upload_path):
        for arquivo in arquivos:
            if termo in arquivo:
                file = arquivo
            else:
                file = ''
    if request.method == "POST":
        consulta.resposta_solicitacao = request.form['resposta']
        db.session.commit()
        return redirect('/demanda')
    return render_template('resposta-executor.html', solicita=consulta, arquivo_no_html=file)


@contacts.route('/resposta')
def resposta():
    return render_template('resposta-executor.html')


@contacts.route('/demanda/<id>')
def modal_id(id):
    just = Solicita.query.get(id)
    return render_template('executor-demandas.html', just=just, user=session['user'])


@contacts.route('/demanda/<id>/justificar', methods=['POST', 'GET'])
def justificativa(id):
    consulta = Solicita.query.get(id)
    if request.method == 'POST':
        consulta.resposta_solicitacao = request.form['justificativa']
        db.session.commit()
        return redirect('/demanda')

    return render_template('executor-demandas.html', solicita=consulta)

##################################### Admin #######################################


@contacts.route('/admin')
def admin():
    if g.user != None:
        if g.user[0] == 3:
            return render_template('home_admin.html')
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/admin/permissoes')
def testeperm():
    if g.user != None:
        if g.user[0] == 3:
            nome = Usuarios.query.filter(Usuarios.id_categoria_usuario != 3)
            #nome = Usuarios.query.all()
            return render_template('adm_permissoes.html', nome=nome)
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/permissoes/<id>', methods=['POST', 'GET'])
def attperm(id):
    if g.user != None:
        if g.user[0] == 3:
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
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))

    # return render_template('adm_permissoes.html', consulta=consultar)


@contacts.route('/relatorios/instantaneos', methods=['POST', 'GET'])
def relInstantaneo():
    if g.user != None:
        if g.user[0] == 3:
            ############### DIA ATUAL ######################
            sql1 = text(
                'select count(*) from solicitacoes where resposta_solicitacao is null and Date(data_abertura) = curdate()')
            sql2 = text(
                'select count(*) from solicitacoes where resposta_solicitacao is not null and Date(data_abertura) = curdate()')
            results1 = db.engine.execute(sql1)
            print(results1)
            for i in results1:
                pass
            res1 = i[0]
            results2 = db.engine.execute(sql2)
            for j in results2:
                pass
            res2 = j[0]
            ############### 7 DIAS ATRÁS ######################
            sql3 = text(
                'select count(*) from solicitacoes where resposta_solicitacao is null and data_abertura between date_sub(curdate(), interval 7 day) and curdate() ')
            sql4 = text('select count(*) from solicitacoes where resposta_solicitacao is not null and data_abertura between date_sub(curdate(), interval 7 day) and curdate() ')
            results3 = db.engine.execute(sql3)
            for t in results3:
                pass
            res3 = t[0]
            results4 = db.engine.execute(sql4)
            for k in results4:
                pass
            res4 = k[0]
            ############### 15 DIAS ATRÁS ######################
            sql5 = text(
                'select count(*) from solicitacoes where resposta_solicitacao is null and data_abertura between date_sub(curdate(), interval 15 day) and curdate() ')
            sql6 = text('select count(*) from solicitacoes where resposta_solicitacao is not null and data_abertura between date_sub(curdate(), interval 15 day) and curdate() ')
            results5 = db.engine.execute(sql5)
            for m in results5:
                pass
            res5 = m[0]
            results6 = db.engine.execute(sql6)
            for n in results6:
                pass
            res6 = n[0]
            ############### 30 DIAS ATRÁS ######################
            sql7 = text(
                'select count(*) from solicitacoes where resposta_solicitacao is null and data_abertura between date_sub(curdate(), interval 1 month) and curdate() ')
            sql8 = text('select count(*) from solicitacoes where resposta_solicitacao is not null and data_abertura between date_sub(curdate(), interval 1 month) and curdate() ')
            results7 = db.engine.execute(sql7)
            for l in results7:
                pass
            res7 = l[0]
            results8 = db.engine.execute(sql8)
            for p in results8:
                pass
            res8 = p[0]
            operador = Usuarios.query.filter_by(id_categoria_usuario=2)
            return render_template('rel-instantaneos.html', data="teste", res1=res1, res2=res2, res3=res3, res4=res4, res5=res5, res6=res6, res7=res7, res8=res8, operadores=operador )
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))


@contacts.route('/relatorios/especificados', methods=['POST', 'GET'])
def relEspecificados():
    return render_template('rel-especificado.html')


@contacts.route('/relatorios/avaliacoes', methods=['POST', 'GET'])
def relAvaliacoes():
    if g.user != None:
        if g.user[0] == 3:
            todos = text('select count(*) from solicitacoes')
            pessimo = text(
                'select count(*) from solicitacoes where FK_id_avaliacao in (1)')
            regular = text(
                'select count(*) from solicitacoes where FK_id_avaliacao in (2)')
            bom = text(
                'select count(*) from solicitacoes where FK_id_avaliacao in (3)')
            otimo = text(
                'select count(*) from solicitacoes where FK_id_avaliacao in (4)')
            executor = text(
                'select * from usuarios where id_usuario=:id;')
            pessimo2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=1')
            regular2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=2')
            bom2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=3')
            otimo2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=4')
            id_executor = 2
            ava1 = db.engine.execute(pessimo2, id=id_executor)
            for i in ava1:
                pass
            a1 = i[0]
            ava2 = db.engine.execute(regular2, id=id_executor)
            for i in ava2:
                pass
            a2 = i[0]
            ava3 = db.engine.execute(bom2, id=id_executor)
            for i in ava3:
                pass
            a3 = i[0]
            ava4 = db.engine.execute(otimo2, id=id_executor)
            for i in ava4:
                pass
            a4 = i[0]
            Ex = db.engine.execute(executor, id=id_executor)
            for i in Ex:
                pass
            ex = i[0]
            geral1 = db.engine.execute(pessimo)
            for i in geral1:
                pass
            g1 = i[0]
            geral2 = db.engine.execute(regular)
            for i in geral2:
                pass
            g2 = i[0]
            geral3 = db.engine.execute(bom)
            for i in geral3:
                pass
            g3 = i[0]
            geral4 = db.engine.execute(otimo)
            for i in geral4:
                pass
            g4 = i[0]
            total = db.engine.execute(todos)
            if request.method == "POST":
                data = request.form['filtro']
                print(data)
                return redirect('/relatorios')

            operador = Usuarios.query.filter_by(id_categoria_usuario=2)
            return render_template('rel-avaliacoes.html', tot=total, ger1=g1, ger2=g2, ger3=g3, ger4=g4, ava1=a1, ava2=a2, ava3=a3, ava4=a4, Ex=ex, 
            operadores=operador)
    
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))
    

@contacts.route('/grafico', methods=['POST']) 
def grafico():
    operador_selecionado = request.form['id_do_operador']
    return render_template('rel-avaliacao-executor.html', ops = operador_selecionado)

##################################### Novo cadastro #######################################

@contacts.route('/cadastro')
def cadastro():
    return render_template('tela-cadastro.html')


@contacts.route('/cadastrando', methods=['POST', 'GET'])
def cadastrando():
    if request.method == 'POST':
        primeiro_nome = request.form['name']
        sobrenome = request.form.get('surname')
        email_usuario = request.form['email']
        emailConfirmado = request.form.get('emailConfirmation')
        senha_usuario = request.form['password']
        senhaConfirmada = request.form.get('passwordConfirmation')
        nome_usuario = f'{primeiro_nome} {sobrenome}'

    if email_usuario != emailConfirmado:
        flash('Email não confere')
        return redirect('/cadastro')
    elif senha_usuario != senhaConfirmada:
        flash('Senha não confere')
        return redirect('/cadastro')
    id_usuario = None
    usuario = Usuarios(id_usuario, nome_usuario,
                       email_usuario, senha_usuario, 1)
    db.session.add(usuario)
    db.session.commit()
    print(usuario)
    flash('ok')

    return redirect('/')

##################################### Sair #######################################


@contacts.route('/sair')
def sair():
    session.pop('user', None)
    return render_template('tela-inicial.html')
