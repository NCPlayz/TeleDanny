# TODO: migrate over to new framework
from telegram.ext import Updater, CommandHandler

from config import token

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a robot! Danny#0007 made me.")

start_handler = CommandHandler('hello', hello)
dispatcher.add_handler(start_handler)

tags = {
    'ayysyncio': 'https://cdn.discordapp.com/attachments/84319995256905728/360193276004794378/unknown.png'
}

def tag(update, context):
    if len(context.args) == 1:
        try:
            context.bot.send_message(chat_id=update.effective_chat.id, text=tags[context.args[0]])
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Tag not found.')
    elif context.args[0] == 'create':
        name = context.args[1]
        content = context.args[2:]
        if name in tags:
            return context.bot.send_message(chat_id=update.effective_chat.id, text=f'Tag {name} already exists.')
        tags[name] = ' '.join(content)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Tag {name} successfully created.')

tag_handler = CommandHandler('tag', tag)
dispatcher.add_handler(tag_handler)

updater.start_polling()
