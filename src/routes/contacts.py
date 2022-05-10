import os
import pathlib
from flask import Blueprint, redirect, render_template, request, url_for, send_from_directory, current_app
from sqlalchemy import text, engine
from models.solicita import Categoria, Solicita
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def index():
    return render_template('home_usuario.html')

@contacts.route('/admin')
def admin():
    return render_template('home_admin.html') 

@contacts.route('/nova-solicitacao')
def nova():
    categoria = Categoria.query.all()
    return render_template('form_usuario_solicitacao.html', categorias=categoria)

@contacts.route('/relatorios')
def relatorio():
    sql1 = text('select count(*) from solicitacoes')
    sql2 = text('select count(*) from solicitacoes where resposta_solicitacao is not null')
    results1 = db.engine.execute(sql1)
    results2 = db.engine.execute(sql2)
    return render_template('relatorios.html', res1=results1, res2=results2)

@contacts.route('/historico')
def historico():
    lista = Solicita.query.all()
    return render_template('usuario-historico.html', listas=lista)

@contacts.route('/demanda')
def demanda():
    lista = Solicita.query.filter_by(resposta_solicitacao = None)
    consulta = Solicita.query.filter(Solicita.resposta_solicitacao.isnot(None))
    return render_template('executor-demandas.html', listas=lista, consultas=consulta)

@contacts.route('/resposta')
def resposta():
    return render_template('resposta-executor.html')

@contacts.route('/criar', methods=['POST',])
def criar():
    tipo = request.form['Tipo de serviço']
    descricao = request.form['descrição do problema']
    #data_solicitacao = request.form['Data']
    novo = Solicita(tipo, descricao)
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



@contacts.route('/atualizar/<id>', methods=['POST','GET'])
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

    return render_template('resposta-executor.html', solicita=consulta, arquivo_no_html = file)