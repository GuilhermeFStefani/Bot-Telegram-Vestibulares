import telebot
import schedule
from threading import Thread
import datetime
from time import sleep
from datetime import timedelta

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

API_KEY = ''
bot = telebot.TeleBot(API_KEY)
some_id = 000000


hoje = datetime.date.today()

def data(dia, mes, ano):
    res = -2
    dataentrada = datetime.date(ano, mes, dia)
  
    if dataentrada >= hoje:
        res = dataentrada - hoje
        return res
    else: 
        return timedelta(res)


################# ENEM ###########################
dataEnemDia1 = data(21,11,2021)
if dataEnemDia1.days >= 1:
  enem1 = "\n\n⭕️ Enem linguagens e Humanas (Dia 21/11). Faltam: x dias!"
  enem1 = enem1.replace('x', str(dataEnemDia1.days))
elif dataEnemDia1.days == 0: 
  enem1 = "\n\nEnem primeiro dia é hoje, boa sorte"
else: 
  enem1 = ""
dataEnemDia2 = data(28,11,2021)
if dataEnemDia2.days >= 1:
  enem2 = "\n\nEnem ciências da natureza e Matemática (Dia 28/11). Faltam: x dias!"
  enem2 = enem2.replace('x', str(dataEnemDia2.days))
elif dataEnemDia2.days == 0: 
  enem2 = "\n\nEnem segundo dia é hoje, boa sorte"
else: 
  enem2 = ""

################# UNICAMP ###########################
dataUnicampDia1 = data(7,11,2021)
if dataUnicampDia1.days >= 1:
  unicamp1 = "\n\nUnicamp primeira fase (07/11). Faltam: x dias!"
  unicamp1 = unicamp1.replace('x', str(dataUnicampDia1.days))
elif dataUnicampDia1.days == 0: 
  unicamp1 = "\n\nUnicamp primeira fase é hoje, boa sorte"
else: 
  unicamp1 = ""
dataUnicampDia2 = data(9,1,2022)
if dataUnicampDia2.days >= 1:
  unicamp2 = "\n\nUnicamp segunda fase (09/01) e (10/01). Faltam: x e y dias!"
  unicamp2 = unicamp2.replace('x', str(dataUnicampDia2.days))
  unicamp2 = unicamp2.replace('y', str(dataUnicampDia2.days + 1))
elif dataUnicampDia2.days == 0 or dataUnicampDia2 == -1: 
  unicamp2 = "\n\nUnicamp segunda fase é hoje, boa sorte"
else: 
  unicamp2 = ""

################# USP ###########################
dataUspDia1 = data(12,12,2021)
if dataUspDia1.days >= 1:
  usp1 = "\n\nFuvest primeira fase (12/12). Fataltam: x dias!"
  usp1 = usp1.replace('x', str(dataUspDia1.days))
elif dataUspDia1.days == 0: 
  usp1 = "\n\nFuvest primeira fase é hoje, boa sorte"
else: 
  usp1 = ""
dataUspDia2 = data(16,1,2022)
if dataUspDia2.days >= 1:
  usp2 = "\n\nFuvest segunda fase (09/01) e (10/01). Faltam: x e y dias!"
  usp2 = usp2.replace('x', str(dataUspDia2.days))
  usp2 = usp2.replace('y', str(dataUspDia2.days + 1))
elif dataUspDia2.days == 0 or dataUspDia2.days == -1: 
  usp2 = "\n\nFuvest segunda fase é hoje, boa sorte" 
else: 
  usp2 = ""

################# UNESP ###########################
dataUnespDia1 = data(15,11,2021)
if dataUnespDia1.days >= 1:
  u1 = "\n\nUnesp primeira fase (15/11). Faltam: x dias!"
  u1 = u1.replace('x', str(dataUnespDia1.days))
elif dataUnespDia1.days == 0: 
  u1 = "\n\nUnesp primeira fase é hoje, boa sorte"
else: 
  u1 = ""
dataUnespDia2 = data(19,12,2021)
if dataUnespDia2.days >= 1:
  u2 = "\n\nUnesp segunda fase (19/12). Faltam: x dias!"
  u2 = u2.replace('x', str(dataUnespDia2.days))
elif dataUnespDia2.days == 0: 
  u2 = "\n\nUnesp segunda fase é hoje, boa sorte"
else: 
  u2 = ""

##strings de print
enem = enem1 + enem2 
unicamp = unicamp1 + unicamp2
usp = usp1 + usp2
unesp = u1 + u2
tudo = unicamp + unesp + enem + usp
help = 'Comandos existentes: /enem, /unicamp, /fuvest, /unesp, /tudo'

# Resposta chat

@bot.message_handler(commands=['enem'])
def vest(message):
    bot.reply_to(message, enem)

@bot.message_handler(commands=['unicamp'])
def vest(message):
    bot.reply_to(message, unicamp)

@bot.message_handler(commands=['fuvest'])
def vest(message):
    bot.reply_to(message, usp)

@bot.message_handler(commands=['unesp'])
def vest(message):
    bot.reply_to(message, unesp)

@bot.message_handler(commands=['tudo'])
def vest(message):
    bot.reply_to(message, tudo)

@bot.message_handler(commands=['help'])
def vest(message):
    bot.reply_to(message, help)

def function_to_run():
    return bot.send_message(some_id, tudo)

#horário que enviará a mensagem
if __name__ == "__main__":
    schedule.every().day.at("17:00").do(function_to_run)
    Thread(target=schedule_checker).start() 

bot.polling()