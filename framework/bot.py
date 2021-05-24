from telegram.ext import Updater, CommandHandler

from .command import Command

class Bot:
    def __init__(self, *, token=None, owners=[]):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.owners = owners
        self.commands = {}
        self._handlers = []

    def command(self, *, owner_only=False):
        def wrap(func):
            cmd = Command(self, func, owner_only=owner_only)
            self.commands[cmd.name] = cmd
            return cmd
        return wrap

    def run(self):
        self._handlers = [CommandHandler(n, c) for n, c in self.commands.items()]

        for ch in self._handlers:
            self.dispatcher.add_handler(ch)

        self.updater.start_polling()
        self.updater.idle()
