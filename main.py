import pandas as pd

from helpers import *
from setup_db import *

""" main.py """
"""
 Programa em Python para simular um controle financeiro (entradas/despesas)
  com o MySQL server.
Autor: Marcos Fabricio Sizanosky
Email: fabricio_sizanosky@hotmail.com
Date: 2021.09.08
"""
print("Hello World!\n")
cabecalho()

my_db = connect_db(HOST, USER, PASSWORD, DATABASE_NAME)
my_cursor = my_db.cursor()

print()

while True:
    mensagem = "Digite a opção desejada (1-Inserir, 2-Visualizar, 3-Sair): "
    inicial = input(mensagem)

    try:
        if inicial == "1":
            data_usr = input("Digite a data (Formato AAAA-MM-DD): ")
            tipo_usr = input("Digite o tipo do dado (1-Entrada, 2-Despesa): ")
            tipo_usr = "entrada" if tipo_usr == "1" else "despesa"
            desc_usr = input("Descrição breve do registro: ")
            valor_usr = input("Digite o valor: ")

            insert_query = f"INSERT INTO {TABLE_NAME} " \
                           f"(data, tipo, descricao, valor) " \
                           f"VALUES (%s, %s, %s, %s)"
            registro = (data_usr, tipo_usr, desc_usr, valor_usr)

            my_cursor.execute(insert_query, registro)
            my_db.commit()

        elif inicial == "2":
            my_cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            resultado = my_cursor.fetchall()
            df = pd.DataFrame(resultado,
                              columns=["ID", "DATA", "TIPO", "DESCRIÇÃO",
                                       "VALOR"])
            print()
            print(df)
            soma_entradas = 0
            soma_despesas = 0

            for linha in resultado:
                if linha[2] == "entrada":
                    soma_entradas += linha[4]
                elif linha[2] == "despesa":
                    soma_despesas += linha[4]
                else:
                    pass
            print()
            print(f"Total entradas: R${soma_entradas: >10}\n"
                  f"Total despesas: R${soma_despesas: >10}\n"
                  f"Saldo final:    R${soma_entradas - soma_despesas: >10}")
            print()
        else:
            break

    except ValueError:
        print("Opção invalida, tente novamente!")
        continue
