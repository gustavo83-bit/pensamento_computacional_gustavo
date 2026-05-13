# importar biblioteca
import sqlite3

# conecetar banco de dados 
conn = sqlite3.connect('atividade_info_cliente.db')


# executar o  sql
curso = conn.cursor()




conn.commit()


