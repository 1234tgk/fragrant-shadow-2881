from .Classes.scene import Scene
from .Classes.choice import Choice
from .scene_win import WinScene
from .scene_lose import LoseScene
from .scene_abrupt_end import AbruptEndScene


class Choice1(Choice):

    def __init__(self, client, message):
        super().__init__("!win", "!win", client, message)
        # self.keyword_trigger = !win
        # self.keyword_advance = !win
        # self.client = client
        # self.message = message

        self.next_scene = WinScene(self.client, self.message)

    async def prompt_choice(self):
        await self.mention()
        await self.message.channel.send("This is an option that lets you win.")

    async def prompt_options(self):
        await self.message.channel.send("Type '!win' to win the game.\nType '!back' to go back to other options")
        msg = await self.client.wait_for('message', check=lambda message: message.author == self.message.author and message.content.startswith("!"))
        # Maybe add timeout?
        self.input = str(msg.content)


class Choice2(Choice):

    def __init__(self, client, message):
        super().__init__("!lose", "!lose", client, message)

        self.next_scene = LoseScene(self.client, self.message)

    async def prompt_choice(self):
        await self.mention()
        await self.message.channel.send("This is an option that makes you lose the game.")

    async def prompt_options(self):
        await self.message.channel.send(
            "Type '!lose' to automatically lose the game.\nType '!back' to go back to other options"
        )
        msg = await self.client.wait_for('message', check=lambda message: message.author == self.message.author and message.content.startswith("!"))
        # Maybe add timeout?
        self.input = str(msg.content)


class Scene2(Scene):

    def __init__(self, client, message):
        super().__init__(client, message)

        self.choice_1 = Choice1(self.client, self.message)
        self.choice_2 = Choice2(self.client, self.message)

    async def prompt_scene(self):
        await self.mention()
        await self.message.channel.send(
            "You now stand before two options: win, or lose. Your action here will greatly impact your future. There "
            "is no turning back. Choose wisely."
        )

    async def prompt_options(self):
        await self.break_line()
        await self.message.channel.send(
            "Type '!win' to win the game.\nType '!lose' to lose the game."
        )
        msg = await self.client.wait_for('message', check=lambda message: message.author == self.message.author and message.content.startswith("!"))
        # Maybe add timeout?
        self.input = str(msg.content)
        if self.input == self.choice_1.keyword_trigger:
            await self.choice_1.prompt_choice()
            await self.play_choice_1()
        elif self.input == self.choice_2.keyword_trigger:
            await self.choice_2.prompt_choice()
            await self.play_choice_2()
        elif self.input == "!game" or self.input == "!end":
            await AbruptEndScene(self.client, self.message).play()
        else:
            await self.mention()
            await self.prompt_inappropriate_answer()
            await self.prompt_options()

    async def play_choice_1(self):
        await self.break_line()
        await self.choice_1.prompt_options()
        if self.choice_1.input == "!back":
            await self.mention()
            await self.message.channel.send("You back away from the portal.")
            await self.prompt_options()
        elif self.choice_1.input == self.choice_1.keyword_advance:
            await self.choice_1.next_scene.play()
        elif self.choice_1.input == "!game" or self.choice_1.input == "!end":
            await AbruptEndScene(self.client, self.message).play()
        else:
            await self.mention()
            await self.prompt_inappropriate_answer()
            await self.play_choice_1()

    async def play_choice_2(self):
        await self.break_line()
        await self.choice_2.prompt_options()
        if self.choice_2.input == "!back":
            await self.mention()
            await self.message.channel.send("You back away from the abyss for your own sake.")
            await self.prompt_options()
        elif self.choice_2.input == self.choice_2.keyword_advance:
            await self.choice_2.next_scene.play()
        elif self.choice_2.input == "!game" or self.choice_2.input == "!end":
            await AbruptEndScene(self.client, self.message).play()
        else:
            await self.mention()
            await self.prompt_inappropriate_answer()
            await self.play_choice_2()
