
#Importa Pacotes
# 1. biblioteca padrão
import random
# 2. pacotes de terceiros
from openpyxl import Workbook
# 3. pacotes desenvolvidos
import planilha

def main():
	lista_planilhas = ['receitas', 'despesas', 'resultado']
	pasta = planilha.cria_xls()
	pasta.active
	for planilha in lista_planilhas:
		planilha.cria_planilha(planilha,pasta)
	pasta.save("orcamento.xls")

if __name__ == "__main__"
	main()