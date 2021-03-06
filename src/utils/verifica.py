from itertools import cycle
from flask import session, flash, g
from sqlalchemy import text, engine
from utils.db import db


def verifica(db_consulta, email, senha):
    for verifica in db_consulta:
        db_email = verifica.email_usuario
        if email == db_email:
            db_senha = verifica.senha_usuario
            if senha == db_senha:
                categoria_usuario = verifica.id_categoria_usuario
                if categoria_usuario == 1: #usuario comum
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    session['id_usuario'] = verifica.id_usuario
                    flash('Usuário logado com sucesso!')
                    return 'contacts.usuario'
                elif categoria_usuario == 2: #operador
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    session['id_usuario'] = verifica.id_usuario
                    flash('Usuário logado com sucesso!')
                    return 'contacts.demanda'
                elif categoria_usuario == 3: #admin
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    session['id_usuario'] = verifica.id_usuario
                    flash('Usuário logado com sucesso!')
                    return 'contacts.admin'
            else:
                flash('Usuário/Senha incorreta')
                return 'contacts.index'#senha incorreta
    flash('Usuário não cadastrado')
    return 'contacts.index' #usuario não cadastrado


def distribui():
    id_solicitacao_anterior = text(
        'SELECT MAX(id_solicitacao) from solicitacoes')
    results = db.engine.execute(id_solicitacao_anterior)
    id1 = ''
    for i in results:
        pass
    id1 = i
    print(id1[0])
    if id1[0] != None:
        id_operador_anterior = text(
            "SELECT FK_id_executor FROM solicitacoes where id_solicitacao=:id")
        results2 = db.engine.execute(id_operador_anterior, id=id1[0])
        for j in results2:
            pass
        id2=j[0]
    else:
        id2 = None
    print(id2)
    todos_operadores = text(
        'SELECT id_usuario FROM usuarios WHERE id_categoria_usuario = 2')
    todos_operadores = db.engine.execute(todos_operadores)
    print(todos_operadores)
    lista = []
    for r in todos_operadores:
        lista.append(r)
    print(lista)
    proximo_operador = ''
    if lista == []:
        adm = text(
        'SELECT id_usuario FROM usuarios WHERE id_categoria_usuario = 3')
        adm = db.engine.execute(adm)
        id_adm = ''
        for i in adm:
            pass
        id_adm = i
        proximo_operador = id_adm[0]
        return proximo_operador
    tamanho = len(lista) - 1
    if id2 == None:
        proximo_operador = lista[0]
        proximo_operador = proximo_operador[0]
        return proximo_operador
    else:
        if j not in lista or lista.index(j) == tamanho:
            proximo_operador = lista[0]
            proximo_operador = proximo_operador[0]
            return proximo_operador
        else:
            nova_posicao = lista.index(j) + 1
            proximo_operador = lista[nova_posicao]
            proximo_operador = proximo_operador[0]
            return proximo_operador
        
def distribui_permissao(id_da_solicitacao, qtd_chamados, ext):
    if id_da_solicitacao != None:
        id_operador_anterior = text(
            "SELECT FK_id_executor FROM solicitacoes where id_solicitacao=:id")
        results2 = db.engine.execute(id_operador_anterior, id=id_da_solicitacao)
        for j in results2:
            pass
        id2=j[0]
    else:
        id2 = None
    todos_operadores = text(
        'SELECT id_usuario FROM usuarios WHERE id_categoria_usuario = 2')
    todos_operadores = db.engine.execute(todos_operadores)
    print(todos_operadores)
    lista = []
    for r in todos_operadores:
        lista.append(r)
    proximo_operador = ''
    tamanho = len(lista) - 1
    if len(lista) == 1:
        adm = text(
        'SELECT id_usuario FROM usuarios WHERE id_categoria_usuario = 3')
        adm = db.engine.execute(adm)
        id_adm = ''
        for i in adm:
            pass
        id_adm = i
        proximo_operador = id_adm[0]
        return proximo_operador
    else:
        if j not in lista or lista.index(j) == tamanho:
            proximo_operador = lista[0]
            proximo_operador = proximo_operador[0]
            return proximo_operador
        else:
            contador = 0
            lista.remove(j)
            nova_lista = []
            ciclo = cycle(lista)
            for m in ciclo:
                if contador > qtd_chamados:
                    break
                else:
                    nova_lista.append(m)
                    contador+=1
            proximo_operador = nova_lista[ext]
            proximo_operador = proximo_operador[0]
            return proximo_operador