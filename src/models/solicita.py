from utils.db import db
from datetime import datetime

class Solicita(db.Model):
    __tablename__ = 'solicitacoes'
    id_solicitacao = db.Column(db.Integer, primary_key=True)
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow)
    data_aceite = db.Column(db.Date)
    data_fechamento = db.Column(db.DateTime, default=datetime.utcnow)
    descricao_solicitacao = db.Column(db.String)
    resposta_solicitacao = db.Column(db.String)
    fk_id_categoria_solicitacao = db.Column(db.Integer, db.ForeignKey('categoria_solicitacoes.id_categoria_solicitacao'))
    fk_id_avaliacao = db.Column(db.Integer, db.ForeignKey('avaliacoes.id_avaliacao'))
    cat = db.relationship('Categoria', back_populates="solicit")
    av = db.relationship('Avaliacao', back_populates="sol")

    def __init__(self, fk_id_categoria_solicitacao, descricao_solicitacao):
        self.fk_id_categoria_solicitacao = fk_id_categoria_solicitacao
        self.descricao_solicitacao=descricao_solicitacao
        #self.data_abertura=data_abertura

    def executor(self,resposta_solicitacao):
        self.resposta_solicitacao=resposta_solicitacao

class Categoria(db.Model):
    __tablename__ = 'categoria_solicitacoes'
    id_categoria_solicitacao = db.Column(db.Integer, primary_key=True)
    categoria_solicitacao = db.Column(db.String)
    solicit = db.relationship('Solicita', back_populates="cat")

    def __init__(self, id_categoria_solicitacao, categoria_solicitacao):
        self.id_categoria_solicitacao = id_categoria_solicitacao
        self.categoria_solicitacao = categoria_solicitacao

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    id_avaliacao = db.Column(db.Integer, primary_key=True)
    quant_estrelas = db.Column(db.Integer)
    sol = db.relationship('Solicita', back_populates="av")

    def __init__(self, id_avaliacao, quant_estrelas):
        self.id_avaliacao = id_avaliacao
        self.quant_estrelas = quant_estrelas