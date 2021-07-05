#!/usr/bin/ python3
import telebot
import BookController
import threading
import random
import main
import math
print("telegramBot loaded")
token = "1500225290:AAEUN3lPnv7pOZmHphssGmLFB2Td1hr4-0o"
bot = telebot.TeleBot(token)

# https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py

ValidCommands = ['addFles', 'listFles', 'listMix', 'help', 'removeFles', 'addMix', 'order', 'updatePositie', 'makeMix']
ValidCommandsUpperLowerCase = []
# globale variabelen voor de telegrambot die interfunctionair nodig zijn
flesPosition = -1
composition = {}
mixName = ""
orderCallback = None
mixToMakeName = ""
mixToMakeVolume = ""

for command in ValidCommands:
    ValidCommandsUpperLowerCase.append(command.lower())
    ValidCommandsUpperLowerCase.append(command)

#op het moment dat er een commado word gegeven verwerkt deze functie het commando
@bot.message_handler(commands=ValidCommandsUpperLowerCase)
def mainHandler(message):
    boodschap = message.text
    boodschap = boodschap.lower()
    print(boodschap)

    if boodschap == "/addfles":
        msg = bot.send_message(message.chat.id, "Aaahhhh een drankje toevoegen, komt goed! wat is de naam?")
        bot.register_next_step_handler(msg, handleFlesNameAdd)

    elif boodschap == "/listfles":
        bot.send_message(message.chat.id, BookController.listFlessenForPrint())

    elif boodschap == "/listmix":
        bot.send_message(message.chat.id, BookController.listMixenForPrint())

    elif boodschap == "/help":

        msg = "Beschikbare commando's zijn: \n"
        #opbouw lijst met alle commando's
        for command in ValidCommands:
            msg += '/' + command + '\n'

        bot.send_message(message.chat.id, msg)

    elif boodschap == "/removefles":
        msg = bot.send_message(message.chat.id, "Aaahhhh een drankje verwijderen, komt goed! wat is de naam?")
        bot.register_next_step_handler(msg, handleFlesNameRemove)

    elif boodschap == "/addmix":
        msg = bot.send_message(message.chat.id, "Wat is de naam van deze nieuwe smaak-sensatie")
        bot.register_next_step_handler(msg, handleMixNameAdd)

    
    elif boodschap == "/updatepositie":
        msg = bot.send_message(message.chat.id, "Op welke positie wil je een andere fles toevoegen?")
        bot.register_next_step_handler(msg, handlePosition)
    
    elif boodschap == '/makemix':
       #bouw een bericht op welke alle beschikbare dranken doorgeeft
        mixes = BookController.listAvailableMixes
        bericht = 'De beschikbare dranken zijn: /n'
        for mix in mixes:
            bericht += mix
            bericht += '/n'

        msg = bot.send_message(message.chat.id, bericht)

        bot.register_next_step_handler(msg, handleMixNaam)

    #in het geval het commando niet word herkent word gesuggereerd het help commando te gebruiken
    else:
        bot.reply_to(message, "Onbekend commando gebruik '/help' voor een lijst met commando's")


def handleMixNaam(message):
    global mixToMakeName
    boodschap = message.text
    boodschap = boodschap.strip()
    if boodschap in BookController.listAvailableMixes():
        mixToMakeName = boodschap
        msg = bot.send_message("hoeveel ml?")
        bot.register_next_step_handler(msg, handleMixVolume)
    else: 
        mixes = BookController.listAvailableMixes
        bericht = 'Deze mix is niet beschikbaar. De beschikbare dranken zijn: /n'
        for mix in mixes:
            bericht += mix
            bericht += '/n'

        msg = bot.send_message(message.chat.id, bericht)

        bot.register_next_step_handler(msg, handleMixNaam)

def handleMixVolume(message):
    #data ophalen
    global mixToMakeVolume
    global mixToMakeName
    boodschap = message.text
    boodschap = boodschap.strip()

    if boodschap.lower() != 'cancel':
        #kijken of de input valide is en anders terug lopen tot er een goede hoeveelheid op word gegeven
        try:
            mixToMakeVolume = int(boodschap)
            math.sqrt(mixToMakeVolume) #op het moment dat een input fout is probeer ik in deze try een foutmelding te genereren, als iemand een negatieve waarde heeft ingevult krijg je hier een fout en word je terug geloopt om het opniew te proberen
            bot.send_message(message.chat.id, 'Sir yes Sir!')
            main.makeDrink(mixToMakeName, mixToMakeVolume)
            bot.send_message(message.chat.id, 'Uw drankjes is gereed')
            
        except: 
            msg = bot.send_message(message.chat.id, 'input heeft het verkeerde format, gebruik positieve integers')
            bot.register_next_step_handler(msg, handleMixVolume)
    #een mogelijkheid voor mensen om te stoppeen met het maken van hun drankje
    else: msg = bot.send_message(message.chat.id, '*sad alchoholic noices*')
    

#een functie die zich bezig houd met het instellen van positiets van drankjes
def handlePosition(message):
    #voorbereiding data
    global flesPosition
    boodschap = message.text
    boodschap = boodschap.strip()
    position = -1

    #controle goede format
    try: 
        if int(boodschap) <= 11 and int(boodschap) >= 0:
            position = int(boodschap)
    except:
        y = 1
    if position == -1:
        msg = bot.send_message(message.chat.id, "De positie moet een getal zijn van 0 tm 11, probeer het opnieuw")
        bot.register_next_step_handler(msg, handlePosition)
    else: 
        flesPosition = position
        repons = "Oké top we gaan de fles op positie " + boodschap + " veranderen, welke fles komt hier te staan?"
        msg = bot.send_message(message.chat.id, repons)
        #door verwijzing naar volgende functie als het goede format is gegeven
        bot.register_next_step_handler(msg, handleFlesNameForPosition)

def handleFlesNameForPosition(message):
    #data ophalen
    global flesPosition
    boodschap = message.text
    boodschap = boodschap.strip()
    boodschap = boodschap.title()
    flessenList = BookController.listFlessen()

    #als iemand een fles toe wil voegen die niet in het systeem staat kan dit meteen door een '+' te gebruiken voor de naam van het drankje
    if boodschap[0] == "+":
                boodschap = boodschap[1:]
                boodschap = boodschap.strip()
                boodschap = boodschap.title()
                BookController.addFles(boodschap)

    
    if boodschap in flessenList:
        #verwerking indien positie is correct
        global flesPosition
        repons = "op positie: " + flesPosition + " staat nu " + boodschap + "."
        bot.send_message(message.chat.id, repons)
        BookController.updatePositionFlessen(flesPosition, boodschap)
    else:
        #een onbekende fles is toegevoegd en word terug geloopt tot een correcte naam is gegeven
        repons = "Deze fles bestaat niet, als U deze toe wil voegen herhaal Uw bericht met +[naamfles] \n De flessen die wel in het systeem staan zijn:\n" + BookController.listFlessenForPrint
        msg = bot.send_message(message.chat.id, repons)
        bot.register_next_step_handler(msg, handleFlesNameForPosition)


def handleFlesNameRemove(message):
    nameFlesToRemove = message.text
    BookController.removeFles(nameFlesToRemove)
    msg = nameFlesToRemove + " is uit het systeem verwijderd."
    bot.send_message(message.chat.id, msg)


def handleFlesNameAdd(message):
    nameFlesToAdd = message.text
    BookController.addFles(nameFlesToAdd)


def handleMixNameAdd(message):
    global mixName
    mixName = message.text
    returntext = "Oke we openen een nieuwe pagina in het kookboek schrijven voor een heerlijke Mixdrank. Je kunt zelf ingrdienten toevoegen dit doe je door een bericht te sturen in het volgende format\n [naamfles] [deel] \n b.v. \n 'Cola 20' \n\n Ben je klaar met het toevoegen van flessen? geef het commando 'KLAAR'"
    msg = bot.send_message(message.chat.id, returntext)
    bot.register_next_step_handler(msg, handleMixIngredients)


def handleMixIngredients(message):
    messageText = message.text
    #eerst een controle of mensen nog door willen gaan
    if(messageText.lower() != "cancel"):
        #data klaarzetten
        messageTextBackup = messageText
        messageList = []
        global composition
        global mixName

        #conrtoleren of het drankje niet al klaar is anders
        if messageText != "KLAAR":
            #als mensen een lijst met flessen willen zien die ze toe willen voegen
            if messageText == "lijst":
                msg = bot.send_message(message.chat.id, BookController.listFlessenForPrint())
                bot.register_next_step_handler(msg, handleMixIngredients)

            #ook hier kunnen mensen meteen een fles toevoegen aan het systeem 
            if messageText[0] == "+":
                messageText = messageText[1:]
                messageText = messageText.strip()
                messageText = messageText.title()
                messageList = messageText.split(" ")
                naamFles = messageList[0]
                BookController.addFles(naamFles)

            #een controle of het goede format is behaald
            try:
                if messageList == []:
                    messageText = messageText.strip()
                    messageText = messageText.title()
                    messageList = messageText.split(" ")
                naamFles = messageList[0]
                deelVanMix = int(messageList[1])
                if naamFles in BookController.listFlessen():
                    #waneer het bericht tot hier is gekomen betekend dit dat het in het goede format was en dat het verwerkt kan worden
                    composition[naamFles] = deelVanMix
                    msg = bot.send_message(message.chat.id,
                                           "Staat genoteerd. Voeg op de zelfde mannier uw volgende drankje toe, of om af te ronden stuur 'KLAAR'")
                    bot.register_next_step_handler(msg, handleMixIngredients)
                else:
                    msg = bot.send_message(message.chat.id,
                                           "Deze fles staat niet in het systeem, herhaal je bericht met een een '+' (b.v. '+ Cola 20') of reageer met 'lijst' om een overzicht van beschikbarenflessen te zien")
                    bot.register_next_step_handler(msg, handleMixIngredients)
########################################################################### nog onderste helft van errorhandling
            except:
                if messageText != "lijst":
                    msg = bot.send_message(message.chat.id, "Het format is incorrect probeer het opnieuw")
                    bot.register_next_step_handler(msg, handleMixIngredients)

        else:
            if (mixName != "" and composition != {}):
                BookController.addMix(BookController.Mix(mixName, composition))
                text = "Proficiat " + mixName + " staat nu in het receptenboek."
                bot.send_message(message.chat.id, text)
                mixName = ""
                composition = {}
            else:
                print("Error: mixname and/or composition empty")
                bot.send_message(message.chat.id, "Je hebt geen ingrediënten of naam ingevuld. Probeer het nog een keer door /addMix te sturen")
    else:
        print("addMix canceled")
        mixName = ""
        composition = {}
#####################################################################################



# error handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,
                 "gebruik '/' om een commando te sturen, '/help' om een lijst te ontvangen met mogelijke commando's")


backgroundCheck = threading.Thread(target=bot.polling)
backgroundCheck.start()
