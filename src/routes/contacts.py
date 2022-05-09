from flask import Blueprint, redirect, render_template, request, url_for, flash, g, session
from models.solicita import Categoria, Solicita, Usuario
from utils.db import db
from utils.verifica import verifica

contacts = Blueprint('contacts', __name__)

@contacts.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user = session['user']

@contacts.route('/sair')
def sair():
    session.pop('user', None)
    return redirect(url_for('contacts.index'))

@contacts.route('/')
def index():
    return render_template('tela-inicial.html')

@contacts.route('/autentica', methods=['POST', 'GET'])
def autentica():
    if request.method == 'POST':
        session.pop('user', None)
        email = request.form['email']
        senha = request.form['senha']
        db_consulta = Usuario.query.all()
        redir = verifica(db_consulta, email, senha)
        return redirect(url_for(redir))
    return render_template('tela-inicial.html')
    
@contacts.route('/usuario')
def usuario():
    if g.user != None:
        if g.user[0] == 4 or g.user[0] == 14:
            return render_template('home_usuario.html', user=session['user'])
    session.pop('user', None)        
    return redirect(url_for('contacts.index'))

@contacts.route('/nova-solicitacao')
def nova():
    if g.user != None:
        if g.user[0] == 4 or g.user[0] == 14:
            categoria = Categoria.query.all()
            return render_template('form_usuario_solicitacao.html', categorias=categoria, user=session['user'])
    session.pop('user', None)        
    return redirect(url_for('contacts.index'))

@contacts.route('/historico')
def historico():
    if g.user != None:
        if g.user[0] == 4 or g.user[0] == 14:
            lista = Solicita.query.all()
            return render_template('usuario-historico.html', listas=lista, user=session['user'])
    session.pop('user', None)        
    return redirect(url_for('contacts.index'))

@contacts.route('/demanda')
def demanda():
    if g.user != None:
        if g.user[0] == 14:
            lista = Solicita.query.filter_by(resposta_solicitacao = None)
            consulta = Solicita.query.filter(Solicita.resposta_solicitacao.isnot(None))
            return render_template('executor-demandas.html', listas=lista, consultas=consulta, user=session['user'])
    session.pop('user', None)
    return redirect(url_for('contacts.index'))

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