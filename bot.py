import configparser
import os

from telegram.ext import Updater, MessageHandler, Filters


config = configparser.ConfigParser()
config.read('config.ini')

TG_TOKEN = config['Telegram']['token']
PORT = int(os.environ.get('PORT', '8443'))
EXTERNAL_HOST = config['Telegram']['EXTERNAL_HOST']


def delete_command(bot, update):
    message = update.message
    bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)


if __name__ == '__main__':
    webhook = f'{EXTERNAL_HOST}/{TG_TOKEN}'
    print(webhook)
    updater = Updater(token=TG_TOKEN, workers=32)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.command, delete_command))
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TG_TOKEN)
    updater.bot.set_webhook(webhook)
    updater.idle()
