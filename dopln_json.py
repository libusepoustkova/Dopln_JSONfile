
import json
#with open('ontologie_v9.json') as handle:
#    dictdump = json.loads(handle.read(),encoding='utf8')
#print(dictdump)


def nacti_JSON():
#fnction reads JSON file
    try:
       with open('ontologie_definice.json', encoding='utf8') as ontoJsonFile:
            ontoJsonStr = ontoJsonFile.read()
            #print(json.dumps(ontoJsonStr)) #, ensure_ascii=False, indent=2))
            ontoJson_data = json.loads(ontoJsonStr)
            #print(ontoJson_data)
            return ontoJsonStr

    except FileNotFoundError:
        print("Nenalezeno")

def nacti_doplnovana_data(listDopln):
#function reads text file to list of list
    try:
        with open('TextFile1.txt', encoding='ansi') as doplnFile:
           
            for radek in doplnFile:
                radek = radek.rstrip("\n")
                listDopln.append(radek.split(";"))

            #print(listDopln)
            return listDopln
    except FileNotFoundError:
        print("Nenalezeno")

def preved_na_slovnik(listDopln):
#function convert my special list to dictionary,the first item in the list is the key, the other is the value in the list
    slDopln = {}   
    for polozka in listDopln:
        slDopln[polozka[0]] = polozka[1:]
    return slDopln

def dopln_JVFK_do_retezce(JSONstr,slDopln):
#function adds a new attribute to the string
    novyJSON = JSONstr
    for onto, dtm in slDopln.items():
        maleonto = onto.lower()
        malynovyJSON = novyJSON.lower()
        #Onto = onto.capitalize()
        if  maleonto in malynovyJSON:
            #print("nalezeno: " + Onto)
            poziceOnto = malynovyJSON.index(maleonto)
            poziceJVFDTM = poziceOnto + len(onto) + 3
            novyJSON = '{0}"JVF_DTM":{1},{2}'.format(novyJSON[0:poziceJVFDTM], json.dumps(dtm, ensure_ascii=False,), novyJSON[poziceJVFDTM:])
        else:
            print("Nenalezeno: " + onto)
    return novyJSON

def zapis_JSON_do_souboru(JSONstr):
    try:
        #new_file = open("D:\\new_dir\\newfile.txt", mode="a+", encoding="utf-8")
        with open('JSONedit.JSON', mode="w", encoding='utf8') as novyJSONfile:
            novyJSONfile.write (JSONstr)

    except FileNotFoundError:
        print("Nenalezen soubor")

listDoplneni = []
listDoplneni = nacti_doplnovana_data(listDoplneni)
#Data = nacti_JSON()
retezecJSON = nacti_JSON()

slovnikDopl = {}
slovnikDopln = preved_na_slovnik(listDoplneni)
novyJSONstr=dopln_JVFK_do_retezce(retezecJSON, slovnikDopln)
zapis_JSON_do_souboru(novyJSONstr)