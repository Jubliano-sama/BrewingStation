import BookController
import telegramBot
import uiController
#import hardwareController


def makeDrink(name, volume):
    mixToMake = BookController.getIngrdients(name)
    
    drinksInMix = list(mixToMake.keys())
    amountInDrinks = list(mixToMake.values())

    total = sum(amountInDrinks)

    parallelDrinkPosition = []
    parallelPart = []
    
    leng = len(mixToMake)

    for i in range(leng):
        
        drinkname = drinksInMix[i]
        position = BookController.getFlesPosition(drinkname)
        parallelDrinkPosition.append(position)

        intPart = amountInDrinks[i]
        partInDrink = (intPart/total) * volume
        parallelPart.append(partInDrink)
    
    print(parallelDrinkPosition)
    print(parallelPart)
    print(drinksInMix)

    #for i in range(leng):


    

makeDrink('baco', 2024)
