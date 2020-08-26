from .Classes.scene import Scene


class LoseScene(Scene):

    async def prompt_scene(self):
        await self.mention()
        await self.message.channel.send("You Lose! Maybe try again?")

    async def play(self):
        await self.prompt_scene()
