from .Classes.scene import Scene


class LoseScene(Scene):

    async def prompt_scene(self):
        await self.message.channel.send("{} You Lose! Maybe try again?".format(self.message.author.mention))

    async def play(self):
        await self.prompt_scene()
