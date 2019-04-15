import telebot
import concurrent.futures
import config
import re
import requests
import random
import time
from datetime import datetime
from threading import Thread
from telebot import types

bot = telebot.TeleBot(config.token)

##class TimePauseAdds:
##    def __init__(self):
##        first_entry=datetime.now()
##    first_entry=datetime(1,1,1,1,1,1,1,None)
##    adlvl=int(0)
##    showing_add_first_time=1
##    time_between_adds=list()
##    time_between_adds=[0,0,1]#days,#hours,#minutes
##    #adds=dict
##    def check_timeout(self):
##        #self.showing_add_first_time=1
##        date_time_now_tuple=datetime.now()
##        date_time_now_tuple.timetuple()
##        first_entry_list=self.first_entry.timetuple()
##        firs_entry_list=list(first_entry_list)
##        if (date_time_now_tuple[0]==first_entry_list[0] and date_time_now_tuple[1]==first_entry_list[1] and date_time_now_tuple[2]==first_entry_list[2]+self.time_between_adds[0]
##            and date_time_now_tuple[3]==first_entry[3]+self.time_between_adds[1] and date_time_now_tuple[4]==first_entry_list[4]+self.time_between_adds[2]):
##            if (showing_add_first_time==1):
##                bot.send_photo(sub_chat_id, "https://torrent-igruha.org/uploads/posts/2015-11/1448649956_ss_df69841962a068dbeb740aff9108cb5dde6b3d6c.1920x1080.jpg",'POSTAL2 FOREVER'+ '\n'+'"Guns don`t kill people, I DO!"' +'\n'+ '©Postal Dude')
##                #log(message)
  
ops=int(1)

def adds_waiter(message):
    global ops
    ops=2
    timeout=list()
    timeout=[0,6,30]
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute    
    while True:
        time.sleep(30)
        handle_postal2cit(message)
##        d=datetime.now()
##        l=list()
##        l=[datetime.now().day,datetime.now().hour, datetime.now().minute]
##        d_d=0
##        d_h=0
##        d_m=0
##        if (timeout[0]==l[0] and timeout[1]==l[1] and timeout[2]==l[2]):
##            handle_postal2cit(message)
##            day = datetime.now().day
##            hour = datetime.now().hour
##            minute = datetime.now().minute


@bot.message_handler(commands=['start', 'help','want_random_picture', 'want'])
def handle_help_start(message):
    handle_wantrandompicture(message)
    sub_chat_id=message
    thread = Thread(target = adds_waiter, args = (sub_chat_id,))
    if (ops<=1):
        thread.start()
        log(message)
    #a=TimePauseAdds()
    #bot.send_message(message.chat.id, "Привет, я ТестовыйБот, вот мои команды: /start, /help, /wantrandompicture, /postal2cit"+'\n')
    #year = datetime.date.today().year
    

@bot.message_handler(commands=['wantrandompicture'])
def handle_wantrandompicture(message):
    photo="https://loremflickr.com/"+str(random.randrange(1024, 2048, 16))+'/'+str(random.randrange(1024, 2048, 22))
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_site_link = types.KeyboardButton(text="Хочу посетить ваш сайт")
    keyboard.add(button_site_link)
    bot.send_photo(message.chat.id, photo,'Вот ваше рандомное фото', reply_markup=keyboard)
    #bot.send_message(message.chat.id, )
    log(message)

#def go_our_site(message):
 #    bot.send_video(message.chat.id, 'f:\TelegramBots\site.mp4',caption='http://abiturientik.com',parse_mode='HTML')

@bot.message_handler(commands=['postal2cit'])
def handle_postal2cit(message):
    photo="https://torrent-igruha.org/uploads/posts/2015-11/1448649956_ss_df69841962a068dbeb740aff9108cb5dde6b3d6c.1920x1080.jpg"
    bot.send_photo(message.chat.id, photo,'POSTAL2 FOREVER'+ '\n'+'"Guns don`t kill people, I DO!"' +'\n'+ '©Postal Dude')
    #bot.send_message(message.chat.id, "Здесь могла быть ваша реклама и медиа сообщения", parse_mode=HTML)
    #bot.send_audio(message.chat.id, open('C:/Users/Я/Downloads/uio.mp3','rb'))
    log(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if(message.text=='Хочу посетить ваш сайт'):
         bot.send_document(message.chat.id, open('f:\TelegramBots\site.mp4', 'rb'),caption='http://abiturientik.com')
    else:
        bot.send_photo(message.chat.id, open('C:/Users/Я/Downloads/test_bot.jpg','rb'), caption="Я вас не понял")
    #bot.send_photo(ид_получателя, 'https://example.org/адрес/картинки.jpg');
    log(message)

def log(message):
    f = open('f:\TelegramBots\log.txt','a')
    print("\n ------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст = {3}".format(message.from_user,message.from_user.last_name,str(message.from_user.id), message.text))
    file_log_message_string=str("\n ------"+"Сообщение от "+
                         str(message.from_user)+" "+str(message.from_user.last_name)+' '+ str(message.from_user.id)+ "\nТекст = "+message.text)
    f.write(file_log_message_string)
    f.close()
    
##if __name__ == "__main__":
##    thread = Thread(target = adds_waiter)
##    thread.start()
##    thread.join()

bot.polling(none_stop=True)
