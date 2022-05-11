from flask import session, flash, g


def verifica(db_consulta, email, senha):
    for verifica in db_consulta:
        db_email = verifica.email_usuario
        if email == db_email:
            db_senha = verifica.senha_usuario
            if senha == db_senha:
                categoria_usuario = verifica.id_categoria_usuario
                if categoria_usuario == 1: #usuario comum
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    flash('Usuário logado com sucesso!')
                    return 'contacts.usuario'
                elif categoria_usuario == 2: #operador
                    session['id_usuario'] = verifica.id_usuario
                    flash('Usuário logado com sucesso!')
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    return 'contacts.demanda'
                elif categoria_usuario == 3: #admin
                    flash('Usuário logado com sucesso!')
                    return 'contact.index'
            else:
                flash('Usuário/Senha incorreto')
                return 'contacts.index'#senha incorreta
    flash('Usuário não cadastrado')
    return 'contacts.index' #usuario não cadastrado
