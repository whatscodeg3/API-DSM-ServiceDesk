from flask import session


def verifica(db_consulta, email, senha):
    for verifica in db_consulta:
        db_email = verifica.email_usuario
        if email == db_email:
            db_senha = verifica.senha_usuario
            if senha == db_senha:
                categoria_usuario = verifica.id_categoria_usuario
                if categoria_usuario == 4:
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    return 'contacts.usuario' #página usuario
                elif categoria_usuario == 14:
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    return 'contacts.demanda' #página operador
                else:
                    return '/' #página admin
            else:
                return 'contacts.index'#senha incorreta
    return '/' #usuario não cadastrado
