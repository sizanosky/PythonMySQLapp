import mysql.connector

""" helpers.py """
""""
 Funções auxiliares do programa.
Autor: Marcos Fabricio Sizanosky
Email: fabricio_sizanosky@hotmail.com
Date: 2021.09.08
"""


def connect_db(host, user, password, name_db=None):
    """
    Creates an object connection to MySQL database.
    :param host: hostname or IP server (string)
    :param user: username (string)
    :param password: user password (string)
    :param name_db: (string)
    :return: object "my_db"
    """

    # Verifica se foi passado um DB como parâmetro e se DB já existe.
    if not name_db:
        my_db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password
        )
    else:
        my_db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=name_db
        )

    return my_db


def cabecalho():
    """
    Função para formatar um cabeçalho para o programa.
    :return: string
    """
    texto = "Controle Financeiro - MySQL DB"
    print(f'{"=" * len(texto) + 10 * "="}')
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f"++++ {texto} ++++")
    print(f'{"*" * len(texto) + 10 * "*"}')
    print(f'{"=" * len(texto) + 10 * "="}')
