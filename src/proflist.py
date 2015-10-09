import time
import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

profAndRoom = []

def test_proflistHAS(value):
    if value == "Abel Dias dos Santos - M210":
        return True
    else:
        return False

def test_proflistHASNOT(value):
    if value == "Abílio Carlos Pereira Pacheco - NONE":
        return True
    else:
        return False

def get_url_proflist():
    linksearch = "https://sigarra.up.pt/feup/pt/func_geral.QueryList"
    data = urllib.parse.urlencode({
        'pi_is_pesquisa':'1',
        'P_NOME':'',
        'P_CODIGO':'',
        'P_SIGLA':'',
        'p_unidade':'',
        'p_nivel':'',
        'pv_unidade_nome':'',
        'pn_grupo':'764',
        'pn_carreira':'',
        'pn_area':'',
        'pn_categoria':'',
        'pv_categoria_nome':'Docente',
        'pv_provimento':'',
        'pv_orgao':'',
        'pv_cargo':'',
        'P_ESTADO':'A',
        'pv_sala_desc':'',
        'p_sala':'1',
        'P_TELEFONE':'',
        'P_EMAIL':'',
        'p_area_id':'',
        'p_area':'',
        'p_n_registos':'1000'
    })
    data = data.encode('UTF-8')

    req = urllib.request.Request(linksearch, data)
    response = urllib.request.urlopen(req)

    soup = BeautifulSoup(response.read(), "html.parser")

    ulTags = soup.find_all("ul")
    urlListProfs = ulTags[2].find_all("a")

    urlListArray = []
    for prof in urlListProfs:
        urlListArray.append("https://sigarra.up.pt/feup/pt/" + prof['href'])

    return urlListArray

def get_prof_and_room(urlProfList):
    arr = []
    for url in urlProfList:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response.read(), "html.parser")

        personalInfo = soup.find("div", {"class":"informacao-pessoal-dados-dados"})

        #GET NAME OF PROFESSOR -----------------------------------------------------
        topInfo = personalInfo.find_all("tr", {"valign":"TOP"})
        profName = topInfo[0].find_all("td")[1].find("b").text

        #GET ROOM OF PROFESSOR -----------------------------------------------------
        trTags = personalInfo.find_all("table")[1].find_all("tr")
        profRoom = ""
        for tr in trTags:
            tdTags = tr.find_all("td")
            if tdTags[0].text == "Salas: ":
                profRoom = tdTags[1].find("a").text

        if profRoom == "":
            profRoom = "NONE"

        arr.append(profName + " - " + profRoom)
        #print(profName + " - " + profRoom)

    return arr



def run_proflist():
    urlProfList = get_url_proflist()

    global profAndRoom
    profAndRoom = get_prof_and_room(urlProfList)

    test_proflistHAS(profAndRoom[0])
    test_proflistHASNOT(profAndRoom[2])





run_proflist()






