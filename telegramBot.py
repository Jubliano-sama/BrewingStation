import telebot
import BookController

token = "1500225290:AAEUN3lPnv7pOZmHphssGmLFB2Td1hr4-0o"
bot = telebot.TeleBot(token)

#https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py

Validcommands = ['addFles', 'listFles', 'listMix', 'help', 'removeFles']
#keyboard = telebot.types.ReplyKeyboardMarkup(True)
#keyboard.row('/addFles', '/listFles', '/listMix', '/help', '/removeFles')

@bot.message_handler(commands=Validcommands)
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
		for command in Validcommands:
			msg += '/' + command + '\n'
		
		bot.send_message(message.chat.id, msg)
		
	
	elif boodschap == "/removeFles":
		msg = bot.send_message(message.chat.id, "Aaahhhh een drankje verwijderen, komt goed! wat is de naam?")
		bot.register_next_step_handler(msg, handleFlesNameRemove)

	else: 
		bot.reply_to(message, "Onbekend commando gebruik '/help' voor een lijst met commando's")

def handleFlesNameRemove(message):
	nameFlesToRemove = message.text
	#hier 
	BookController.removeFles(nameFlesToRemove)
	msg = nameFlesToRemove + " is uit het systeem verwijderd."
	bot.send_message(message.chat.id, msg)

def handleFlesNameAdd(message):
	nameFlesToAdd = message.text
	BookController.addFles(nameFlesToAdd)

#error handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "gebruik '/' om een commando te sturen, '/help' om een lijst te ontvangen met mogelijke commando's")
	
	

bot.polling()