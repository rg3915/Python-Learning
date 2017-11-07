import requests
from bs4 import BeautifulSoup

y = 1

while ( y < 12):

	url = ("https://www.infojobs.com.br/vagas-de-emprego-*.aspx?Page={}").format(y)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	Site = soup.find(id="ctl00_phMasterPage_cGrid_divGrid")

	NomeVagas = Site.find_all(class_ = "vaga ")
	NomeEmpresas = Site.find_all(class_ = "vaga-company")
	Data = Site.find_all(class_ = "data")
	Local = Site.find_all(itemprop="addressLocality")
	Sigla = Site.find_all(itemprop="addressRegion")
	Area = Site.find_all(class_ = "area ")

	prVagas = []
	prEmpresas = []
	prDias = []
	prRegiao = []
	prSiglas = []
	prAreas = []

	for Vagas in NomeVagas:
		Vagas2 = (Vagas.get_text())
		Vagas3 = Vagas2.split("\n")
		listVagas = list(Vagas3)
		strVagas = "".join(listVagas)
		stripVagas = strVagas.strip()
		prVagas.append(stripVagas)
		
	for Empresas in NomeEmpresas:
		Empresas2 = (Empresas.get_text())
		Empresas3 = Empresas2.split("\n")
		listEmpresas = list(Empresas3)
		strEmpresas = "".join(listEmpresas)
		stripEmpresas = strEmpresas.strip()
		prEmpresas.append(stripEmpresas)
		
	for Dia in Data:
		Dias = (Dia.get_text())
		Dias2 = Dias.split("\n")
		listDias = list(Dias2)
		strDias = "".join(listDias)
		stripDias = strDias.strip()
		prDias.append(stripDias)

	for Regiao in Local:
		Regiao2 = (Regiao.get_text())
		Regiao3 = Regiao2.split("\n")
		listRegiao = list(Regiao3)
		strRegiao = "".join(listRegiao)
		stripRegiao = strRegiao.strip()
		prRegiao.append(stripRegiao)
		
	for Siglas in Sigla:
		Siglas2 = (Siglas.get_text())
		Siglas3 = Siglas2.split("\n")
		listSiglas = list(Siglas3)
		strSiglas = "".join(listSiglas)
		stripSiglas = strSiglas.strip()
		prSiglas.append(stripSiglas)
		
	for Areas in Area:
		Areas2 = (Areas.get_text())
		Areas3 = Areas2.split("\n")
		listAreas = list(Areas3)
		strAreas = "".join(listAreas)
		stripAreas = strAreas.strip()
		prAreas.append(stripAreas)
		
	frmV = ["{aff     Vaga:"]*100
	frmE = ["    Empresa:"]*100
	frmD = ["    Data:"]*100
	frmR = ["    Região:"]*100
	frmS = ["    Sigla:"]*100
	frmA = ["    Area:"]*100
	Virgula = ["..aff"]*500
	fim = ["aff }..aff"] *100
	a = "-" *50

	tudo = ([j for i in zip (
		frmV,prVagas,Virgula,
		frmE,prEmpresas,Virgula,
		frmD,prDias,Virgula,
		frmR,prRegiao,Virgula,
		frmS,prSiglas,Virgula,
		frmA,prAreas,fim
		)for j in i])
	
	MarcaPagina = ("{0}Página {1}{2}").format(a,y,a)
	print (MarcaPagina)
	
	tudos = str(tudo)
	strtudo = "".join(tudos)
	pulartudo = strtudo.replace("aff","\n")
	pulartudo1 = pulartudo.replace("'","")
	pulartudo2 = pulartudo1.replace(",","")
	pulartudo3 = pulartudo2.replace("..",",")
	pulartudo4 = pulartudo3.replace("asdasd","-"*100)
	pulartudo5 = pulartudo4.replace("aff","\n")
	print(pulartudo5)
	
	y = y + 1