def verifica(db_consulta, email, senha):
    for verifica in db_consulta:
        db_email = verifica.email_usuario
        print(db_email)
        if email == db_email:
            db_senha = verifica.senha_usuario
            print(db_senha)
            if senha == db_senha:
                categoria_usuario = verifica.id_categoria_usuario
                if categoria_usuario == 1:
                    return '/usuario'
                elif categoria_usuario == 2:
                    return '/demanda'
                else:
                    return '/'
            else:
                return 'Senha incorreta'
                

    return 'Usuario não cadastrado'
