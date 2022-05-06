from flask import Blueprint, redirect, render_template, request, url_for, jsonify 
from models.solicita import Categoria, Solicita, Usuarios
from utils.db import db

contacts = Blueprint('contacts', __name__)

# flake8: noqa


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
    lista = Solicita.query.filter_by(resposta_solicitacao=None)
    consulta = Solicita.query.filter(Solicita.resposta_solicitacao.isnot(None))
    return render_template('executor-demandas.html', listas=lista, consultas=consulta)


@contacts.route('/resposta')
def resposta():
    return render_template('resposta-executor.html')


@contacts.route('/criar', methods=['POST', ])
def criar():
    tipo = request.form['Tipo de serviço']
    descricao = request.form['descrição do problema']
    #data_solicitacao = request.form['Data']
    novo = Solicita(tipo, descricao)
    db.session.add(novo)
    db.session.commit()

    return redirect('/historico')


@contacts.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualiza(id):
    consulta = Solicita.query.get(id)
    if request.method == "POST":
        consulta.resposta_solicitacao = request.form['resposta']
        db.session.commit()
        return redirect('/demanda')

    return render_template('resposta-executor.html', solicita=consulta)


@contacts.route('/cadastro')
def cadastro():
    return render_template('tela-cadastro.html')

@contacts.route('/alert')
def alert():
    return render_template('sweetalerts.html')

@contacts.route('/cadastrando', methods=['POST', 'GET'])
def cadastrando():
    body = request.get_json()
    if request.method == 'POST':
        nome = request.form.get('name')
        sobrenome = request.form.get('surname')
        email = request.form.get('email')
        emailConfirmado = request.form.get('emailConfirmation')
        senha = request.form.get('password')
        senhaConfirmada = request.form.get('passwordConfirmation')
        dataCheckbox = request.form.get('checkboxData')
        print(dataCheckbox)

    if email != emailConfirmado:
        print('Email não confere')
        return redirect('/cadastro')
    elif senha != senhaConfirmada:
        print('Senha não confere') 
        return redirect('/cadastro')
    elif dataCheckbox != 'check':
        print('Confirme o uso de dados para continuar o cadastro')
        return redirect('/cadastro')
    elif not nome or not sobrenome:
        print('Nome ou sobrenome não preenchido')
        return redirect('/cadastro')
    elif not email:
        print('Email não preenchido')
        return redirect('/cadastro')
    elif not emailConfirmado:
        print('Confirme seu email')
        return redirect('/cadastro')
    elif not senha:
        print('Senha não preenchida')
        return redirect('/cadastro')
    elif not senhaConfirmada:
        print('Confirme sua senha')
        return redirect('/cadastro')
    else:
        try:
           #usuario = Usuarios(nome_usuario = body[f'{nome} {sobrenome}'], email_usuario = body[f'{email}'], senha_usuario = body[f'{senha}'])
            usuario = Usuarios.to_json(f"{nome} {sobrenome}", f"{email}", f"{senha}")
            print(usuario)
            db.session.add(usuario)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return print('error')
