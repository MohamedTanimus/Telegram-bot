import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=['start'])
def boten(message):
	key = types.InlineKeyboardMarkup()
	b2=types.InlineKeyboardButton(text='CHANEEL', url='https://t.me/Freeintrnn')
	key.row_width = 1
	key.add(b2)
	bi='4536'
	bb='0987654321'
	ya=['2023','2024','2025','2026','2027','2028','2029']
	ex=['01','02','03','04','05','06','07','08','09','10','11','12']
	while True:
		b1 = random.choice(bi)
		bin = b1+random.choice(bb)+random.choice(bi)+random.choice(bb)+random.choice(bi)+random.choice(bb)
		exy=random.choice(ya)
		exp=random.choice(ex)
		ccv=random.choice(bb)+random.choice(bb)+random.choice(bb)
		cgen=random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)+random.choice(bb)
		cn = bin+cgen
		cc = bin+cgen+'|'+exp+'|'+exy+'|'+ccv
		try:
			apibinlist = requests.get("https://lookup.binlist.net/"+bin).json()
			try:
				emoji = apibinlist["country"]["emoji"]
			except:
				emoji=''
			try:
				name = apibinlist["country"]["name"]
			except:
				name=''
			try:
				binType = apibinlist["type"]
			except:
				binType=''
			try:
				bank_name = apibinlist["bank"]["name"]
			except:
				bank_name=''
			try:
				bank_phone = apibinlist["bank"]["phone"]
			except:
				bank_phone=''
			try:
				bank_url = apibinlist["bank"]["url"]
			except:
				bank_url=''
			try:
				brand = apibinlist["brand"]
			except:
				brand=''
			try:
				scheme = apibinlist["scheme"]
			except:
				scheme=''
			
			respo= f"""
┏━━━━━━━━━━━━━━
┣ 🍂 𝑪𝑪 𝑺𝑺𝑪𝑹𝑨𝑷𝑷𝑬𝑹 🍂 ┗━━━━━━━━━━━━━━
════════════════════                   ╠𝑪𝑪: {cc}
┏━━━━━━━━━━━━━━
┣ 🍁 𝑩𝑰𝑵 {bin} 𝑫𝑨𝑻𝑨 🍁
┗━━━━━━━━━━━━━━
╠𝑩𝒊𝒏 𝑫𝒆𝒕𝒂𝒊𝒍𝒔:{name} -{emoji} -{bank_name}{binType} -{scheme}
╠𝑩𝒂𝒏𝒌: {brand}
┏━━━━━━━━━━━━━━
┣ 🍁 𝑀𝑌 𝐼𝑁𝐹𝑂 🍁
┗━━━━━━━━━━━━━━
🧑🏻‍💻| 𝑫𝐸𝑉:  @Mosalahxyz 
🥷🏻| 𝑪𝑯:@Freeintrnn """
			bot.send_message(message.chat.id,text=respo,parse_mode='html',reply_markup=key)
		except:pass
		
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://tgbbbit.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
