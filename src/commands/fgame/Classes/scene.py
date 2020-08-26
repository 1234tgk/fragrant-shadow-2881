class Scene(object):

    def __init__(self, client, message):
        self.client = client
        self.message = message
        self.input = ""

    async def break_line(self):
        await self.message.channel.send("-------------")

    async def mention(self):
        await self.message.channel.send(self.message.author.mention)

    async def prompt_scene(self):
        pass

    async def prompt_options(self):
        pass

    async def prompt_inappropriate_answer(self):
        await self.message.channel.send("Inappropriate input. Please input a valid option.")

    async def play(self):
        await self.prompt_scene()
        await self.prompt_options()
