from flask import session, flash, g


def verifica(db_consulta, email, senha):
    for verifica in db_consulta:
        db_email = verifica.email_usuario
        if email == db_email:
            db_senha = verifica.senha_usuario
            if senha == db_senha:
                categoria_usuario = verifica.id_categoria_usuario
                if categoria_usuario == 4:
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    flash('Usuário logado com sucesso!')
                    return 'contacts.usuario' #página usuario
                elif categoria_usuario == 14:
                    session['id_usuario'] = verifica.id_usuario # aqui thiago
                    flash('Usuário logado com sucesso!')
                    session['user'] = [categoria_usuario, verifica.nome_usuario]
                    return 'contacts.demanda' #página operador
                else:
                    flash('Usuário logado com sucesso!')
                    return 'contact.index' #página admin,  FALTA PAGINA ADMIN
            else:
                flash('Usuário/Senha incorreto')
                return 'contacts.index'#senha incorreta
    flash('Usuário/Senha incorreto')
    return 'contacts.index' #usuario não cadastrado
