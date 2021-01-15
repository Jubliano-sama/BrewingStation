import json

print("BookController loaded")

def listMixen():
        MixenNames = []

        with open("Receptboek.json") as f:
                mixen = json.load(f)
        for mix in mixen:
                mixName = mix["name"]
                MixenNames.append(mixName)
        return MixenNames

def listMixenForPrint():
        msg = "Mixen nu in het systeem zijn: \n"
        mixList = listMixen()

        for mixName in mixList:
                msg += mixName + "\n"
                
        return msg

def listFlessen():
        with open('flessen.json') as json_file:
                data = json.load(json_file)
        return data

def listFlessenForPrint():
        msg = "Flessen nu in het systeem zijn: \n"
        flesList = listFlessen()

        for flesName in flesList:
                msg += flesName + "\n"
                
        return msg

def addMix():
        newDrinkName = input("Naam van het nieuwe drankje: ")

        #loop om de alleen door te gaan met 0 < int < 14
        numberOfIngredients = -1
        while numberOfIngredients <= 0 or numberOfIngredients > 14:
                numberOfIngredientsInput = input("Aantal bestandsdelen: ")
                try:
                        numberOfIngredients = int(numberOfIngredientsInput)
                except: 
                        print("De opgegeven waarde moet een geheel getal zijn van 1 t.e.m. 14 zonder spaties,\n of geef het commando 'CANCEL'") 

                if numberOfIngredients > 14:
                        print("Er kunnen niet meer als 14 verschillende dranken worden gekozen.")

        # de ingredienten naar verhouding toevoegen
        ingredients = {}
        with open("flessen.json") as data:
                baverages = json.load(data)
        for i in range(numberOfIngredients):
                while True:
                        message = "ingredient #" + str(i + 1) + ": "
                        ingredient = str.lower(input(message))
                        if ingredient in baverages: 
                                break
                        else:
                                command = input("dit drankje bestaat nog niet in de database wil u het toevoegen of in de lijst kijken? (z/k)")
                                #hier was je 
                message = ingredient + " maakt zoveel delen van " + newDrinkName + ": "
                parts = str.lower(input(message))                  
                ingredients[ingredient] = int(parts)

        #recept opbouwen
        page = {
        "name" : newDrinkName,
        "composition": ingredients
        }

        #controle 
        print("ter controle:")
        print("Naam nieuwe drankje:", newDrinkName)
        print("Met ingredienten: ")
        for fluid in sorted(ingredients):
                print(fluid, ingredients[fluid], "delen")

        while True:
                lastCheck = input("Goedgekeurd? (j/n)")

                if lastCheck == "j":

                        #with open("Receptboek.json") as data:
                        with open('Receptboek.json') as json_file:
                                data = json.load(json_file)
                                data.append(page)
                        outfile = open("Receptboek.json", "w+")
                        json.dump(data, outfile, indent = 4)
                        outfile.close()
                                #data.close()

                        print(newDrinkName + "is toegevoed aan het systeem")
                        break   
                elif lastCheck == "n":
                        print("jammer, probeer het opnieuw.")
                        break
                else:
                        print("invalide input, probeer opnieuw.")

def addFles(name):
        data = listFlessen()
        name = name.strip()
        name = name.title()
        data.append(name)
        data.sort()
        data = list(dict.fromkeys(data))

        outfile = open("flessen.json", "w+")
        json.dump(data, outfile, indent = 0)
        outfile.close()
        print(name, "toegevoed")

def removeFles(name):
        data = listFlessen()
        name = name.strip()
        name = name.title()
        data.remove(name)
        data.sort()
        data = list(dict.fromkeys(data))

        outfile = open("flessen.json", "w+")
        json.dump(data, outfile, indent = 0)
        outfile.close()
        print(name, "toegevoed")

def updatePositionFlessen(position, flesname):
        with open("flessenInPosition.json") as f:
                places = json.load(f)

        places[position]
