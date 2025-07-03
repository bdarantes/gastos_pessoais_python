from db import criar_tabela, adicionar_gasto_bd, listar_gastos

class ControleFinanceiro:
	def __init__(self):
		self.gastos=[]
		

def adicionar_gasto(self, descricao, valor):
	self.gastos.append({"descricao": descricao, "valor": valor})
	
def main():
	criar_tabela()
	controle = ControleFinanceiro()
	
	
	
	while True:
		print("\n--Controle de Gastos--")
		print("1. Adicionar Gastos")
		print("2. Mostrar Gastos")
		print("3. Sair")
		
		
		opcao = input("Escolha uma opção: ")
		if opcao =="1":
			descricao = input("Digite a descrição ")
			valor = float(input("Digite o valor "))
			adicionar_gasto_bd(descricao,valor)
			
		elif opcao =="2":
			listar_gastos()
			
		elif opcao =="3":
			print("Saindo do programa")
			break
			
		else:
			print("Opção incorreta, tente novamente")
			
if __name__ =="__main__":
	main()
			
		
