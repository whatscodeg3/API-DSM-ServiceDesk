from utils.db import db
from datetime import datetime
from flask import jsonify 


class Solicita(db.Model):
    __tablename__ = 'solicitacoes'
    id_solicitacao = db.Column(db.Integer, primary_key=True)
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow)
    data_aceite = db.Column(db.Date)
    data_fechamento = db.Column(db.DateTime, default=datetime.utcnow)
    descricao_solicitacao = db.Column(db.String)
    resposta_solicitacao = db.Column(db.String)
    fk_id_categoria_solicitacao = db.Column(db.Integer, db.ForeignKey(
        'categoria_solicitacoes.id_categoria_solicitacao'))
    fk_id_executor = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id_usuario'))
    fk_id_usuario = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id_usuario'))
    cat = db.relationship('Categoria', back_populates="solicit")

    def __init__(self, fk_id_categoria_solicitacao, descricao_solicitacao):
        self.fk_id_categoria_solicitacao = fk_id_categoria_solicitacao
        self.descricao_solicitacao = descricao_solicitacao
        # self.data_abertura=data_abertura

    def executor(self, resposta_solicitacao):
        self.resposta_solicitacao = resposta_solicitacao


class Categoria(db.Model):
    __tablename__ = 'categoria_solicitacoes'
    id_categoria_solicitacao = db.Column(db.Integer, primary_key=True)
    categoria_solicitacao = db.Column(db.String)
    solicit = db.relationship('Solicita', back_populates="cat")

    def __init__(self, id_categoria_solicitacao, categoria_solicitacao):
        self.id_categoria_solicitacao = id_categoria_solicitacao
        self.categoria_solicitacao = categoria_solicitacao
        
class CategoriaUsuario(db.Model):
    __tablename__ = 'categoria_usuarios'
    id_categoria_usuario = db.Column(db.Integer, primary_key=True)
    categoria_solicitacao = db.Column(db.String)
    categoria = db.relationship('Usuario', back_populates="user")

    def __init__(self, id_categoria_usuario, categoria_usuario):
        self.id_categoria_solicitacao = id_categoria_usuario
        self.categoria_solicitacao = categoria_usuario      


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(255))
    email_usuario = db.Column(db.String(255))
    senha_usuario = db.Column(db.String(14))
    id_categoria_usuario = db.Column(db.Integer, db.ForeignKey(
        'categoria_usuarios.id_categoria_usuario'))
    user = db.relationship("CategoriaUsuario", back_populates="categoria")

    def __init__(self, nome_usuario,email_usuario, senha_usuario, id_categoria_usuario = 4):
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.senha_usuario = senha_usuario
        self.id_categoria_usuario = id_categoria_usuario
        
        