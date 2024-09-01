# config.py

# Simulação de um banco de dados em memória
users_db = {
    "admin": "adminpass",
    "user": "userpass"
}

def validate_login(username, password, mode):
    """
    Função para validar o login de usuário.
    """
    if mode == "vulnerable":
        if username in users_db and (users_db[username] == password or password == "' OR '1'='1"):
            return True
    elif mode == "protected":
        if username in users_db and users_db[username] == password:
            return True
    return False
