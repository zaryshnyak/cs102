import telebot
import socket
import socks

access_token = '765607476:AAFXOtg2IR8VIWpsGThMSs_DPZUX8i03gH8'
telebot.apihelper.proxy = {'https':'socks5h://91.221.70.248:9100'}
bot = telebot.TeleBot(access_token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling()