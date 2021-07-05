import BookController
#import telegramBot
import uiController
import hardwareControllerr 
import time 


def cleaning():
    position = BookController.getFlesPosition('Spoel Water')
    hardwareControllerr.travelTo(position)
        
    hardwareControllerr.pump(10, 'up')#door even te spoelen gaan restjes uit het rietje weg
    hardwareControllerr.pump(10, 'down')#door de andere kant op te spoelen verdwijnt ook het water uit het rietje


def makeDrink(name, volume):
    #verzamelen van de data
    mixToMake = BookController.getIngrdients(name)
    drinksInMix = list(mixToMake.keys())
    amountInDrinks = list(mixToMake.values())

    #het formateren van de data om overzichtelijker alles overzichtelijker te houden

    total = sum(amountInDrinks)

    #2 lijsten zodat ze bijde tegelijk mee gewerkt kan worden in de zelfde loop
    parallelDrinkPosition = []
    parallelVolume = []
    
    leng = len(mixToMake)

    for i in range(leng):
        #de postitie word gezocht van de fles
        drinkname = drinksInMix[i]
        position = BookController.getFlesPosition(drinkname)
        parallelDrinkPosition.append(position)

        #hoeveel ml er moet worden ingeschonken word berekend
        intPart = amountInDrinks[i]
        partInDrink = (intPart/total) * volume
        parallelVolume.append(int(partInDrink))


    for i in range(leng):
        #variabelen ophalen
        position = parallelDrinkPosition[i]
        volumeOfPart = parallelVolume[i]


        #ga naar de juiste positie
        hardwareControllerr.travelTo(position)
        
        #pompp de vloeistof door en spuuw overgebleven terug
        hardwareControllerr.pump(volumeOfPart, 'up')
        hardwareControllerr.pump(10, 'down')
    #wacht 10 seconde alvorens de machine zich na spoelt
    time.sleep(10)

    cleaning()

    

    

#makeDrink('baco', 200)
