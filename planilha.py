
#Módulo Planilha - manipular arquivos xls

#importação de pacotes
 
from openpyxl import openpyxl


def cria_xls() -> Workbook:
	pasta = Workbook()
	return pasta

def cria_planilha(nome_planilha: str, pasta: Workbook) -> None:
	pasta.active
	pasta.create_sheet(nome_planilha)