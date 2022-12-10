import os
import telebot
import requests
import json
import csv

os.environ['yourkey'] ="12345"
os.environ['bot_id'] ="5914004281:AAF7ycfn3PsD5Ipb--lgV0AN9bYqOvad_NA"
# TODO: 1.1 Get your environment variables 
yourkey = os.getenv('yourkey')
bot_id = os.getenv('bot_id')

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    os.remove(f'movies{message.chat.id}.csv')
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    a= message.text.split(' ')
    word = ''
    for abc in a:
        if abc !='/movie':
            word = word + abc + ' '
    bot.reply_to(message,'Getting movie info...')
    response = requests.get(f'http://www.omdbapi.com/?t={word}&apikey=2a44865a')
    mm = response.json()
    base_url = "https://api.telegram.org/bot5914004281:AAF7ycfn3PsD5Ipb--lgV0AN9bYqOvad_NA/sendPhoto"
    if mm['Response'] == 'False':
        bot.reply_to(message,'Movie not found!,Please try again')
    else:
        bot.send_message(message.chat.id,"Movie found!")
        parameters = {
        "chat_id" : f'{message.chat.id}',
        "photo" : mm['Poster'],
        "caption" : f"Title = {mm['Title']}\nYear= {mm['Year']}\nReleased = {mm['Released']}\nIMDb Rating= {mm['imdbRating']}"
        }

    resp = requests.get(base_url, data = parameters)
    print(resp.text)
    print(response.json())
    with open(f'movies{message.chat.id}.csv', 'a') as csvfile:
        name_list =['Title','Year','Released','IMDb Rating' ]
        impo = csv.DictWriter(csvfile, fieldnames = name_list)
        if os.path.getsize(f'movies{message.chat.id}.csv') == 0:
            impo.writeheader()
        impo.writerow({'Title':mm['Title'],'Year':mm['Year'],'Released':mm['Released'],'IMDb Rating':mm['imdbRating']})
    
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    files ={'document':open(f'movies{message.chat.id}.csv','rb')}
    resp = requests.post(f"https://api.telegram.org/bot5914004281:AAF7ycfn3PsD5Ipb--lgV0AN9bYqOvad_NA/sendDocument?chat_id={message.chat.id}",files=files)

    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()

