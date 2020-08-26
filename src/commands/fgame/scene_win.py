from .Classes.scene import Scene


class WinScene(Scene):

    async def prompt_scene(self):
        await self.mention()
        await self.message.channel.send("Congratulation, {}! You Won!".format(self.message.author))

    async def play(self):
        await self.prompt_scene()
