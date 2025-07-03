import sqlite3

def conectar_banco():
	conn = sqlite3.connect('gastos.db')
	return conn
	
	
def criar_tabela():
	conn = conectar_banco()
	c = conn.cursor()
	c.execute(''' CREATE TABLE IF NOT EXISTS gastos (
	descricao TEXT NOT NULL,
	valor REAL NOT NULL)''')
	conn.commit()
	conn.close()
	
def adicionar_gasto_bd(descricao, valor):
	conn = conectar_banco()
	c = conn.cursor()
	c.execute("INSERT INTO gastos (descricao, valor) VALUES (?,?)", (descricao, valor))
	conn.commit()
	conn.close()
	
def listar_gastos():
	conn = conectar_banco()
	c = conn.cursor()
	c.execute("SELECT * FROM gastos")
	gastos = c.fetchall()
	conn.close()
	for gasto in gastos:
		print (gasto)
	
	
	

	
