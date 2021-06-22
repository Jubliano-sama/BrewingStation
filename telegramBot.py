#!/usr/bin/ python3
import telebot
import BookController

print("telegramBot loaded")
token = "1500225290:AAEUN3lPnv7pOZmHphssGmLFB2Td1hr4-0o"
bot = telebot.TeleBot(token)

# https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py

ValidCommands = ['addFles', 'listFles', 'listMix', 'help', 'removeFles', 'addMix', 'order']

# global variabel

# voor addMix
composition = {}
mixName = ""
orderCallback = None


@bot.message_handler(commands=ValidCommands)
def mainHandler(message):
    boodschap = message.text
    print(boodschap)

    if boodschap == "/addFles":
        msg = bot.send_message(message.chat.id, "Aaahhhh een drankje toevoegen, komt goed! wat is de naam?")
        bot.register_next_step_handler(msg, handleFlesNameAdd)

    elif boodschap == "/listFles":
        bot.send_message(message.chat.id, BookController.listFlessenForPrint())

    elif boodschap == "/listMix":
        bot.send_message(message.chat.id, BookController.listMixenForPrint())

    elif boodschap == "/help":

        msg = "Beschikbare commando's zijn: \n"
        for command in ValidCommands:
            msg += '/' + command + '\n'

        bot.send_message(message.chat.id, msg)

    elif boodschap == "/removeFles":
        msg = bot.send_message(message.chat.id, "Aaahhhh een drankje verwijderen, komt goed! wat is de naam?")
        bot.register_next_step_handler(msg, handleFlesNameRemove)

    elif boodschap == "/addMix":
        msg = bot.send_message(message.chat.id, "Wat is de naam van deze nieuwe smaak-sensatie")
        bot.register_next_step_handler(msg, handleMixNameAdd)

    elif boodschap == "/order":
        msg = bot.send_message(message.chat.id, "Welk drankje wilt u bestellen?")
        bot.register_next_step_handler(msg, handleOrder)

    else:
        bot.reply_to(message, "Onbekend commando gebruik '/help' voor een lijst met commando's")


def handleFlesNameRemove(message):
    nameFlesToRemove = message.text
    # hier
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
    if(messageText != "CANCEL"):
        messageTextBackup = messageText
        messageList = []
        global composition
        global mixName

        if messageText != "KLAAR":

            if messageText == "lijst":
                msg = bot.send_message(message.chat.id, BookController.listFlessenForPrint())
                bot.register_next_step_handler(msg, handleMixIngredients)

            if messageText[0] == "+":
                messageText = messageText[1:]
                messageText = messageText.strip()
                messageText = messageText.title()
                messageList = messageText.split(" ")
                naamFles = messageList[0]
                BookController.addFles(naamFles)

            try:
                if messageList == []:
                    messageText = messageText.strip()
                    messageText = messageText.title()
                    messageList = messageText.split(" ")
                naamFles = messageList[0]
                deelVanMix = int(messageList[1])
                if naamFles in BookController.listFlessen():
                    composition[naamFles] = deelVanMix
                    msg = bot.send_message(message.chat.id,
                                           "Staat genoteerd. Voeg op de zelfde mannier uw volgende drankje toe, of om af te ronden stuur 'KLAAR'")
                    bot.register_next_step_handler(msg, handleMixIngredients)
                else:
                    msg = bot.send_message(message.chat.id,
                                           "Deze fles staat niet in het systeem, herhaal je bericht met een een '+' (b.v. '+ Cola 20') of reageer met 'lijst' om een overzicht van beschikbarenflessen te zien")
                    bot.register_next_step_handler(msg, handleMixIngredients)

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


def handleOrder(message):
    print("Handling Telegram order")
    if (message.text != "CANCEL"):
        if (message.text != "/addMix"):
            if (message.text in BookController.listMixNames()):
                if callable(orderCallback):
                    orderCallback(BookController.getMix(message.text))
                    bot.send_message(message.chat.id, "Je bestelling staat in de wachtrij!")
                else:
                    print("Error: orderCallback telegramBot empty")
                    bot.send_message(message.chat.id, "Error: orderCallback empty")
            else:
                msg = bot.send_message(message.chat.id,
                                       "Die mix bestaat niet, probeer het opnieuw of voeg een mix toe met het /addMix commando. Typ CANCEL om te annuleren.")
                bot.register_next_step_handler(msg, handleOrder)
        else:
            handleMixNameAdd(message)
    else:
        print("Telegram order canceled")


# error handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,
                 "gebruik '/' om een commando te sturen, '/help' om een lijst te ontvangen met mogelijke commando's")


bot.polling()
