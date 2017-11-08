import json
import requests
from bs4 import BeautifulSoup

lista = []

for y in range(1, 12):
    url = ("https://www.infojobs.com.br/vagas-de-emprego-*.aspx?Page={}").format(y)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    site = soup.find(id="ctl00_phMasterPage_cGrid_divGrid")

    nome_vagas = site.find_all(class_="vaga ")
    nome_empresas = site.find_all(class_="vaga-company")
    data = site.find_all(class_="data")
    local = site.find_all(itemprop="addressLocality")
    sigla = site.find_all(itemprop="addressRegion")
    area = site.find_all(class_="area ")

    prvagas = []
    prempresas = []
    prdias = []
    prregiao = []
    prsiglas = []
    prareas = []

    for vagas in nome_vagas:
        vagas2 = vagas.get_text().strip()
        prvagas.append(vagas2)

    for empresas in nome_empresas:
        empresas2 = empresas.get_text().strip()
        prempresas.append(empresas2)

    for dia in data:
        dias = dia.get_text().strip()
        prdias.append(dias)

    for regiao in local:
        regiao2 = regiao.get_text().strip()
        prregiao.append(regiao2)

    for siglas in sigla:
        siglas2 = siglas.get_text().strip()
        prsiglas.append(siglas2)

    for areas in area:
        areas2 = areas.get_text().strip()
        prareas.append(areas2)

    for i in zip(prvagas, prempresas, prdias, prregiao, prsiglas, prareas):
        dt = {}
        dt['vaga'] = i[0]
        dt['empresa'] = i[1]
        dt['data'] = i[2]
        dt['regiao'] = i[3]
        dt['sigla'] = i[4]
        dt['area'] = i[5]
        lista.append(dt)

with open('vagas.json', 'w') as f:
    json.dump(lista, f, indent=4)
