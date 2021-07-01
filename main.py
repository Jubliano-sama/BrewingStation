import BookController
#import telegramBot
import uiController
import hardwareControllerr
import time 


def cleaning():
    position = BookController.getFlesPosition('Spoel Water')
    hardwareControllerr.travelTo(position)
        
    hardwareControllerr.pump(10, 'up')
    hardwareControllerr.pump(10, 'down')


def makeDrink(name, volume):
    #verzamelen van de data
    mixToMake = BookController.getIngrdients(name)
    drinksInMix = list(mixToMake.keys())
    amountInDrinks = list(mixToMake.values())

    #het formateren van de data om overzichtelijker alles overzichtelijker te houden

    total = sum(amountInDrinks)

    parallelDrinkPosition = []
    parallelVolume = []
    
    leng = len(mixToMake)

    for i in range(leng):
        
        drinkname = drinksInMix[i]
        position = BookController.getFlesPosition(drinkname)
        parallelDrinkPosition.append(position)

        intPart = amountInDrinks[i]
        partInDrink = (intPart/total) * volume
        parallelVolume.append(int(partInDrink))


    for i in range(leng):
        position = parallelDrinkPosition[i]
        volumeOfPart = parallelVolume[i]


        #kijk nog eventjes of dit voldoende is, of dat je het rietje nog moet bedienen
        hardwareControllerr.travelTo(position)
        
        hardwareControllerr.pump(volumeOfPart, 'up')
        hardwareControllerr.pump(10, 'down')
    
    time.sleep(5)

    cleaning()

    

    

makeDrink('baco', 200)
