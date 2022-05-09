from flask import Blueprint, redirect, render_template, request, url_for
from models.solicita import Categoria, Solicita
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def index():
    return render_template('home_usuario.html')

@contacts.route('/nova-solicitacao')
def nova():
    categoria = Categoria.query.all()
    return render_template('form_usuario_solicitacao.html', categorias=categoria)

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

    return redirect('/historico')


@contacts.route('/atualizar/<id>', methods=['POST','GET'])
def atualiza(id):
    consulta = Solicita.query.get(id)
    if request.method == "POST":
        consulta.resposta_solicitacao = request.form['resposta']
        db.session.commit()
        return redirect('/demanda')

    return render_template('resposta-executor.html', solicita=consulta)

@contacts.route('/justificar/<id>', methods=['POST', 'GET'])
def justifica(id):
    consulta = Solicita.query.get(id)
    if request.method == "POST":
        consulta.resposta_solicitacao = request.form['justificativa']
        db.session.commit()
        return render_template('executor-demandas.html', solicita=consulta)
