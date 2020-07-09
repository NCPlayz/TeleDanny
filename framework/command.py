from .utils import camel_case


from .context import Context

class Command:
    def __init__(self, bot, func=None, *, owner_only=False):
        self.func = func
        self.name = camel_case(func.__name__)
        self.owner_only = owner_only
        self.bot = bot

    def __call__(self, update, context):
        ctx = Context(self, update, context)
        if ctx.user and self.owner_only and ctx.user.id not in self.bot.owners:
            return ctx.send('not allowed sorry.')
        return self.func(ctx)
