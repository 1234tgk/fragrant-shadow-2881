class Choice(object):

    def __init__(self, keyword_trigger, keyword_advance, client, message):
        self.keyword_trigger = keyword_trigger
        self.keyword_advance = keyword_advance
        self.client = client
        self.message = message

        self.input = ""

    async def mention(self):
        await self.message.channel.send(self.message.author.mention)

    async def prompt_choice(self):
        pass

    async def prompt_options(self):
        pass
