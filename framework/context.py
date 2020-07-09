import typing

from telegram import Update, Message, Chat, User, Bot, ParseMode
from telegram.ext import CallbackContext


class Context:
    def __init__(self, command, update: Update, context: CallbackContext):
        self.command = command
        self.bot = command.bot
        self.update = update
        self.context = context
        self.update_id: int = update.update_id
        self.message: Message = update.effective_message
        self.channel: Chat = update.effective_chat
        self.user: User = update.effective_user
        self.args: typing.List[str] = context.args
        self.content: str = self.message.text if self.message else None
        self.me: Bot = context.bot
    
    def send(self, text: str='', *, reply: Message=None, html=False, markdown=False, photo=None):
        parse_mode = None
        if html:
            parse_mode = ParseMode.HTML
        elif markdown:
            parse_mode = ParseMode.MARKDOWN_V2
        if reply:
            reply = reply.message_id
        
        if photo:
            return self.me.send_photo(self.channel.id, photo=photo, caption=text, parse_mode=parse_mode, reply_to_message_id=reply)

        return self.me.send_message(self.channel.id, text=text, parse_mode=parse_mode, reply_to_message_id=reply)

    def reply(self, text: str, **kwargs):
        reply = self.message
        self.send(text, reply=reply, **kwargs)
