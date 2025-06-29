import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin, thing , classify_thing , path_image # Импортируем функции из bot_logic
from aiogram import Bot, Dispatcher, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🌱 *Привет, друг!* Я — EcoHelper, твой персональный помощник в борьбе с глобальным потеплением. Тут ты можешь узнать о глобальном потеплении, как оно влияет на жизнь и планету. Я буду отправлять тебе советы каждый день! Нажми /help чтобы посмотреть команды. ") 


dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

# Список советов
advices = [
    "совет1",
    "совет 2",
    "совет3",
    "совет4"
]

async def send_daily_advice():
    import random
    advice = random.choice(advices)
    await bot.send_message(chat_id=chat_id, text=f"Совет дня: {advice}")

# Запуск планировщика
scheduler.add_job(send_daily_advice, "cron", hour=9, minute=0)  # Каждый день в 9:00
scheduler.start()


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['help'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10) 
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    message.photo[-1]
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info,'C:\Users\admin\Desktop\ai bot\images')
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, f"Скачано")

    




# Запускаем бота
    bot.polling()