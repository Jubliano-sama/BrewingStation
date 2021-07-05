import json

print("BookController loaded")


################################################################## alles voor mixen

class Mix:
    def __init__(self, name="", ingredients={}):
        self.name = name
        self.ingredients = ingredients



def listMixNames():
    with open("Receptboek.json") as json_file:
        book = json.load(json_file)
    
    mixes = list(book.keys())

    return mixes

def listMixenForPrint():
    msg = "Mixen nu in het systeem zijn: \n"
    mixList = listMixNames()
    #opbouw string voor alle mixen in het systeem
    for mixName in mixList:
        msg += mixName + "\n"

    return msg

def listAvailableMixes():
    #verzameling data
    availableMixes = []

    with open('flessenInPosition.json') as json_file:
        drinksInSystem = json.load(json_file)
    with open("Receptboek.json") as json_file:
        book = json.load(json_file)
    
    #het maken van een lijst van alle drankjes
    mixes = list(book.keys())

    for name in mixes:
        mix = book[name]
        #per mix worden de flessen opgeslagen in een list
        bottles = list(mix.keys())
        
        possible = True
        for bottle in bottles:
            if bottle not in drinksInSystem: possible = False # als er een fles mist zal deze loop hem op niet mogelijk zetten
        
        #als na de loop de mix nogsteeds mogelijk blijkt word deze toegevoegd aan mogelijke mixen
        if possible: availableMixes.append(name)
        
    
    return availableMixes

#een functie die aan geroepen word vanuit de telegrambot om een mix op te slaan in het systeem
def addMix(newMix=Mix()):
    page = {
        "name": newMix.name,
        "composition": newMix.ingredients
    }

    with open('Receptboek.json') as json_file:
        data = json.load(json_file)
        data[newMix.name] = newMix.ingredients
        
    outfile = open("Receptboek.json", "w+")
    json.dump(data, outfile, indent=4)
    outfile.close()


############################################################################################# alles voor flessen

def listFlessen():
    with open('flessen.json') as json_file:
        data = json.load(json_file)
    return data

def listAvilibleFlessen():
    with open('flessenInPosition.json') as json_file:
        data = json.load(json_file)
    return data

def listFlessenForPrint():
    msg = "Flessen nu in het systeem zijn: \n"
    flesList = listFlessen()

    #opbouw string
    for flesName in flesList:
        msg += flesName + "\n"

    return msg

def addFles(name):
    #data verzameling
    data = listFlessen()
    name = name.strip()
    name = name.title()
    data.append(name)
    data.sort() #sorteert de flessen alfabetische
    data = list(dict.fromkeys(data)) #zorgt er voor dat drankjes niet dubbel worden toegevoed

    #verwerking
    outfile = open("flessen.json", "w+")
    json.dump(data, outfile, indent=0)
    outfile.close()

    #feedback naar console voor debug
    print(name, "toegevoed")

def removeFles(name):
    #data verzamelen
    data = listFlessen()
    name = name.strip()
    name = name.title()
    data.remove(name)
    #data opslaan
    outfile = open("flessen.json", "w+")
    json.dump(data, outfile, indent=0)
    outfile.close()
    print(name, "toegevoegd")

def updatePositionFlessen(position, flesname):
    #inladen data
    with open("flessenInPosition.json") as f:
        places = json.load(f)
    
    #updaten
    places[position] = flesname

    #wegschrijven
    outfile = open("flessenInPosition.json", "w+")
    json.dump(places, outfile, indent=0)
    outfile.close()

def getFlesPosition(flesnaam):
    with open('flessenInPosition.json') as json_file:
        data = json.load(json_file)
    position  = data.index(flesnaam)
    return position+1 # +1 omdat we niet met een 0 positie werken

def getIngrdients(mixname):
    with open('Receptboek.json') as json_file:
        data = json.load(json_file)
        return data[mixname]
    
