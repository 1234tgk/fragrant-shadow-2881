from .Classes.scene import Scene


class AbruptEndScene(Scene):

    async def prompt_scene(self):
        await self.mention()
        await self.message.channel.send("Ending the game...")

    async def play(self):
        await self.prompt_scene()
