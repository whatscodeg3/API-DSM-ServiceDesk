from flask import Blueprint, redirect, render_template, request, url_for, jsonify, Response , json, flash
from models.solicita import Categoria, Solicita, Usuario
from utils.db import db

contacts = Blueprint('contacts', __name__)

# flake8: noqa

#def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
   # body = {}
  #  body[nome_do_conteudo] = conteudo
    
  #  if(mensagem):
 #       body["mensagem"] = mensagem
 #   return Response(jsonify(body), content_type="application/json", status=status)

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
    if request.method == 'POST':
        nome_usuario = request.form.get('name')
        sobrenome = request.form.get('surname')
        email_usuario = request.form.get('email')
        emailConfirmado = request.form.get('emailConfirmation')
        senha_usuario = request.form.get('password')
        senhaConfirmada = request.form.get('passwordConfirmation')
        dataCheckbox = request.form.get('checkboxData')
        print(dataCheckbox)
    

    if email_usuario != emailConfirmado:
        flash('Email não confere')
        return redirect('/cadastro')
    elif senha_usuario != senhaConfirmada:
        flash('Senha não confere') 
        return redirect('/cadastro')
    elif dataCheckbox != 'check':
        flash('Confirme o uso de dados para continuar o cadastro')
        return redirect('/cadastro')
    elif not nome_usuario or not sobrenome:
        flash('Nome ou sobrenome não preenchido')
        return redirect('/cadastro')
    elif not email_usuario:
        Flash('Email não preenchido')
        return redirect('/cadastro')
    elif not emailConfirmado:
        flash('Confirme seu email')
        return redirect('/cadastro')
    elif not senha_usuario:
        flash('Senha não preenchida')
        return redirect('/cadastro')
    elif not senhaConfirmada:
        flash('Confirme sua senha')
        return redirect('/cadastro')
    usuario = Usuario(nome_usuario, email_usuario,  senha_usuario)
    db.session.add(usuario)
    db.session.commit()
    print(usuario)
   
    
    return redirect('/')
