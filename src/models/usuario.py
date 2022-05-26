from utils.db import db
class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(255))
    email_usuario = db.Column(db.String(255))
    senha_usuario = db.Column(db.String(14))
    id_categoria_usuario = db.Column(db.Integer, db.ForeignKey(
        'categoria_usuarios.id_categoria_usuario'))
    cat_usu = db.relationship('CategoriaUsuarios', back_populates="usu")
    #sol_usu = db.relationship('Solicita', back_populates="usu_sol")

    def __init__(self, id_usuario, nome_usuario, email_usuario, senha_usuario, id_categoria_usuario):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.senha_usuario = senha_usuario
        self.id_categoria_usuario = id_categoria_usuario

        
class CategoriaUsuarios(db.Model):
    __tablename__ = 'categoria_usuarios'
    id_categoria_usuario = db.Column(db.Integer, primary_key=True)
    categoria_usuario = db.Column(db.String)
    usu = db.relationship('Usuarios', back_populates="cat_usu")