from multiprocessing.sharedctypes import Value
from xml.etree.ElementPath import ops
from sqlalchemy import false, text, engine
import os
import pathlib
from flask import Blueprint, flash, redirect, render_template, request, session, g, url_for, send_from_directory, current_app
from models.solicita import Avaliacao, Categoria, Solicita
from models.usuario import Usuarios
from sqlalchemy import text, engine
from utils.db import db
from utils.verifica import distribui, distribui_permissao, verifica

contacts = Blueprint('contacts', __name__)


@contacts.before_request
def before_request():
    g.user = None
    g.id_usuario = None
    if 'user' in session:
        g.user = session['user']
    if 'id_usuario' in session:
        g.id_usuario = session['id_usuario']

@contacts.route('/')
def index():
    session.pop('id_usuario', None)
    session.pop('user', None) 
    return render_template('tela-inicial.html')

##################################### Login #######################################

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

##################################### Usuário ####################################### 

@contacts.route('/usuario')
def usuario():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2:
            return render_template('home_usuario.html', user = session['user'])    
    return redirect(url_for('contacts.index'))


@contacts.route('/nova-solicitacao')
def nova():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2 or g.user[0] == 3:
            categoria = Categoria.query.all()
            return render_template('form_usuario_solicitacao.html', categorias=categoria, user=session['user'])
    return redirect(url_for('contacts.index'))

@contacts.route('/criar', methods=['POST', ])
def criar():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2 or g.user[0] == 3:
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
    return redirect(url_for('contacts.index'))

@contacts.route('/historico')
def historico():
    if g.user != None:
        if g.user[0] == 1 or g.user[0] == 2 or g.user[0] == 3:
            print(g.id_usuario)
            lista = Solicita.query.filter_by(fk_id_usuario_comum=g.id_usuario)
            return render_template('usuario-historico.html', listas=lista, user=session['user'])     
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

##################################### Operador #######################################

@contacts.route('/demanda')
def demanda():
    if g.user != None:
        if g.user[0] == 2 or g.user[0] == 3:
            lista = Solicita.query.filter_by(resposta_solicitacao=None, fk_id_executor=g.id_usuario)
            consulta = Solicita.query.filter_by(resposta_solicitacao= not Value, fk_id_executor=g.id_usuario)
            chamado = Solicita.query.filter_by(fk_id_executor=g.id_usuario)
            return render_template('executor-demandas.html', listas=lista, consultas=consulta, chamados=chamado, user=session['user'])
    return redirect(url_for('contacts.index'))

@contacts.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualiza(id):
    consulta = Solicita.query.get(id)
    consulta_usuario = Usuarios.query.get(consulta.fk_id_usuario_comum)
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
    return render_template('resposta-executor.html', quem_abriu=consulta_usuario, solicita=consulta, arquivo_no_html=file, user=session['user'])

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
            return render_template('home_admin.html', user=session['user'])
    return redirect(url_for('contacts.index'))

@contacts.route('/admin/permissoes')
def testeperm():
    if g.user != None:
        if g.user[0] == 3:
            nome= Usuarios.query.filter(Usuarios.id_categoria_usuario != 3)
            return render_template('adm_permissoes.html', nome=nome, user=session['user'])
    return redirect(url_for('contacts.index'))

@contacts.route('/permissoes/<id>', methods=['POST','GET'])
def attperm(id):
    if g.user != None:
        if g.user[0] == 3:
            consultar = Usuarios.query.get(id)
            if consultar.id_categoria_usuario == 2:
                teste = text(
                "SELECT id_solicitacao FROM solicitacoes where resposta_solicitacao is null and FK_id_executor=:id")
                results2 = db.engine.execute(teste, id=id)
                lista_de_chamados = []
                for a in results2:
                    lista_de_chamados.append(a[0])
                if lista_de_chamados != []:
                    ext=0
                    print(len(lista_de_chamados))
                    while len(lista_de_chamados) > ext:
                        id_solic = lista_de_chamados[ext]
                        consulta = Solicita.query.filter_by(id_solicitacao=id_solic, resposta_solicitacao=None).first()
                        proximo_operador = distribui_permissao(id_solic, len(lista_de_chamados), ext)
                        consulta.fk_id_executor = proximo_operador
                        db.session.commit()
                        ext+=1
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
    return redirect(url_for('contacts.index'))

    # return render_template('adm_permissoes.html', consulta=consultar)

@contacts.route('/relatorios/instantaneos', methods=['POST', 'GET'])
def relInstantaneo():
    if g.user != None:
        if g.user[0] == 3:
            data=''
            if request.method == 'POST':
                data = request.form['data']
                ############### DIA ATUAL ######################
                sql1 = text(
                    'select count(*) from solicitacoes where resposta_solicitacao is null and Date(data_abertura) = DATE(:data)')
                sql2 = text(
                    'select count(*) from solicitacoes where resposta_solicitacao is not null and Date(data_abertura) = DATE(:data)')
                results1 = db.engine.execute(sql1, data=data)
                print(results1)
                for i in results1:
                    pass
                res1 = i[0]
                results2 = db.engine.execute(sql2, data=data)
                for j in results2:
                    pass
                res2 = j[0]
                ############### 7 DIAS ATRÁS ######################
                sql3 = text(
                    'select count(*) from solicitacoes where resposta_solicitacao is null and data_abertura between date_sub(DATE(:data), interval 7 day) and DATE(:data) ')
                sql4 = text('select count(*) from solicitacoes where resposta_solicitacao is not null and data_abertura between date_sub(DATE(:data), interval 7 day) and DATE(:data) ')
                results3 = db.engine.execute(sql3, data=data)
                for t in results3:
                    pass
                res3 = t[0]
                results4 = db.engine.execute(sql4, data=data)
                for k in results4:
                    pass
                res4 = k[0]
                ############### 15 DIAS ATRÁS ######################
                sql5 = text(
                    'select count(*) from solicitacoes where resposta_solicitacao is null and data_abertura between date_sub(DATE(:data), interval 15 day) and DATE(:data) ')
                sql6 = text('select count(*) from solicitacoes where resposta_solicitacao is not null and data_abertura between date_sub(DATE(:data), interval 15 day) and DATE(:data) ')
                results5 = db.engine.execute(sql5, data=data)
                for m in results5:
                    pass
                res5 = m[0]
                results6 = db.engine.execute(sql6, data=data)
                for n in results6:
                    pass
                res6 = n[0]
                ############### 30 DIAS ATRÁS ######################
                sql7 = text(
                    'select count(*) from solicitacoes where resposta_solicitacao is null and data_abertura between date_sub(DATE(:data), interval 1 month) and DATE(:data) ')
                sql8 = text('select count(*) from solicitacoes where resposta_solicitacao is not null and data_abertura between date_sub(DATE(:data), interval 1 month) and DATE(:data)')
                results7 = db.engine.execute(sql7, data=data)
                for l in results7:
                    pass
                res7 = l[0]
                results8 = db.engine.execute(sql8, data=data)
                for p in results8:
                    pass
                res8 = p[0]
                operador = Usuarios.query.filter_by(id_categoria_usuario=2)
                return render_template('rel-instantaneos.html', data=data, res1=res1, res2=res2, res3=res3, res4=res4, res5=res5, res6=res6, res7=res7, res8=res8, operadores=operador )
            return render_template('rel-instantaneos.html', data=data)
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))

@contacts.route('/relatorios/especificados', methods=['GET', 'POST'])
def relatorios():
    if g.user != None:
         if g.user[0] == 3:
            if request.method == 'POST':
                data_inicio= request.form['data_inicio']
                data_fim= request.form['data_fim']

                if data_inicio > data_fim:
                    flash('Data inicial não pode ser maior que a data final')
                    return redirect('/relatorios/especificados')
                
                print(data_inicio, data_fim)
                # usar COUNT(*)
                
                query_solicitacoes_abertas = text(
                        'SELECT DATE(data_abertura) as data_abertura, COUNT(*) as solicitacoes_abertas FROM solicitacoes WHERE(data_abertura) BETWEEN DATE(:data_inicio) AND  DATE(:data_fim) and resposta_solicitacao is null group by DATE(data_abertura);')
                query_solicitacoes_fechadas = text(
                        'SELECT DATE(data_abertura) as data_abertura, COUNT(*) as solicitacoes_abertas FROM solicitacoes WHERE(data_abertura) BETWEEN DATE(:data_inicio) AND  DATE(:data_fim) and resposta_solicitacao is not null group by DATE(data_abertura);')
                resultado_solicitacoes_abertas = db.engine.execute(query_solicitacoes_abertas, data_fim=data_fim, data_inicio=data_inicio)
                solicitacoes_abertas = []
                for solicitacoes in resultado_solicitacoes_abertas:
                    solicitacoes_abertas.append(solicitacoes)
                resultado_solicitacoes_fechadas = db.engine.execute(query_solicitacoes_fechadas, data_fim=data_fim, data_inicio=data_inicio)
                solicitacoes_fechadas = []
                for solicitacoes in resultado_solicitacoes_fechadas:
                    solicitacoes_fechadas.append(solicitacoes)
                
                
                return render_template('rel-especificado.html', data_inicio=data_inicio, data_fim=data_fim,  resultado_solicitacoes_abertas = resultado_solicitacoes_abertas, solicitacoes_abertas = solicitacoes_abertas, solicitacoes_fechadas = solicitacoes_fechadas)
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
            return render_template('rel-avaliacoes.html', tot=total, ger1=g1, ger2=g2, ger3=g3, ger4=g4, ava1=a1, ava2=a2, ava3=a3, ava4=a4, Ex=ex, operadores=operador)
    
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))
    

@contacts.route('/grafico', methods=['POST']) 
def grafico():
    if g.user != None:
        if g.user[0] == 3:
            operador_selecionado = request.form['id_do_operador']
            operador = Usuarios.query.filter_by(id_categoria_usuario=2)
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
            pessimo2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=1')
            regular2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=2')
            bom2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=3')
            otimo2 = text(
                'select count(*) as FK_id_executor, count(*) as FK_id_avaliacao from solicitacoes where FK_id_executor=:id and FK_id_avaliacao=4')
            ava1 = db.engine.execute(pessimo2, id=operador_selecionado)
            for i in ava1:
                pass
            a1 = i[0]
            ava2 = db.engine.execute(regular2, id=operador_selecionado)
            for i in ava2:
                pass
            a2 = i[0]
            ava3 = db.engine.execute(bom2, id=operador_selecionado)
            for i in ava3:
                pass
            a3 = i[0]
            ava4 = db.engine.execute(otimo2, id=operador_selecionado)
            for i in ava4:
                pass
            a4 = i[0]
            return render_template('rel-avaliacao-executor.html', ops = operador_selecionado, operadores=operador, ava1=a1, ava2=a2, ava3=a3, ava4=a4, tot=total, ger1=g1, ger2=g2, ger3=g3, ger4=g4, Ex=ex)
    session.pop('user', None)
    session.pop('id_usuario', None)
    return redirect(url_for('contacts.index'))

@contacts.route('/admin/historico')
def adminhist():
    if g.user != None:
        if g.user[0] == 3:
            lista = Solicita.query.filter_by(resposta_solicitacao=None)
            consulta = Solicita.query.filter_by(resposta_solicitacao= not Value)
            chamado = Solicita.query.all()
            usuario = Usuarios.query.all()
            return render_template('historico-admin.html', listas=lista, consultas=consulta, chamados=chamado, usuarios=usuario, user=session['user'])
    return redirect(url_for('contacts.index'))    


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
        else:
            db_consulta = Usuarios.query.all()
            for verifica in db_consulta:
                db_email = verifica.email_usuario
                if db_email == email_usuario:
                    flash('Email já cadastrado!')
                    return redirect('/cadastro')

        id_usuario = None
        usuario = Usuarios(id_usuario, nome_usuario, email_usuario, senha_usuario, 1)
        db.session.add(usuario)
        db.session.commit()
        flash('ok')
    return redirect('/')

##################################### Sair #######################################


@contacts.route('/sair')
def sair():
    return redirect(url_for('contacts.index'))
