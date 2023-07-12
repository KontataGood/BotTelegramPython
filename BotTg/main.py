import telebot
import wikipedia
from wikipedia import re
from telebot import types
#import python weather

#new bot
bot = telebot.TeleBot("6173788749:AAHL6trtZV_4GTZ12-hm8iVb4_jvteCVYt4")#token

crossIcon = u"\u274C"#1

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        clear = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=clear.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2

    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return ('Я че знаю чтоли?')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('sticker/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

 #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кто ты?")
    item2 = types.KeyboardButton("Давай поиграем")
    
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
     if message.chat.type == 'private':
        if message.text == 'Кто ты?':
            bot.send_message(message.chat.id, 'Я бот, созданный чтобы дать какую-либо информацию, развлечь, и многое другое')
        elif message.text == 'Давай поиграем':
            bot.send_message(message.chat.id, 'Напиши игру для начала')
        else:
            bot.send_message(message.chat.id, getwiki(message.text))
            
bot.polling(none_stop=True, interval=0)

#new function(new answers) #2




