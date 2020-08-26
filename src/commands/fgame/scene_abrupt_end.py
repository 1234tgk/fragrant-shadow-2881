from .Classes.scene import Scene


class AbruptEndScene(Scene):

    async def prompt_scene(self):
        # await self.message.channel.send("{} Ending the game...".format(self.message.channel.mention))
        pass

    async def play(self):
        await self.prompt_scene()
