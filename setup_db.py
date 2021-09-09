from helpers import connect_db
from config import *

""" setup.py """
""""
 Cria o DB/tabela e realiza a conexão com o MySQL server.
Autor: Marcos Fabricio Sizanosky
Email: fabricio_sizanosky@hotmail.com
Date: 2021.09.08
"""

# Create DB.
my_db = connect_db(HOST, USER, PASSWORD)
my_cursor = my_db.cursor()
my_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")

# Create table.
my_db = connect_db(HOST, USER, PASSWORD, DATABASE_NAME)
my_cursor = my_db.cursor()
my_cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} "
                  f"("
                  f"id_entrada INTEGER AUTO_INCREMENT PRIMARY KEY, "
                  f"data DATE NOT NULL, "
                  f"tipo VARCHAR(25) NOT NULL, "
                  f"descricao VARCHAR(255) NOT NULL, "
                  f"valor DECIMAL(10,2) NOT NULL "
                  f")")
