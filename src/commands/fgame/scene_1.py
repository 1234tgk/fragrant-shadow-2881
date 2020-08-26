from .Classes.scene import Scene
from .Classes.choice import Choice
from .scene_2 import Scene2
from .scene_lose import LoseScene
from .scene_abrupt_end import AbruptEndScene


class Choice1(Choice):

    def __init__(self, client, message):
        super().__init__("!look into the portal", "!go in", client, message)

        self.next_scene = Scene2(self.client, self.message)

    async def prompt_choice(self):
        await self.mention()
        await self.message.channel.send("You stand before a blue portal with unknown destination. You do not know "
                                        "what's beyond this gate, but you have a pretty good feeling about this for "
                                        "some reason. There's also a note on the right side of the gate.")

    async def prompt_options(self):
        await self.message.channel.send(
            "Type '{}' to walk into the portal.\n"
            "Type '!read note' to read the note next to the portal.\n"
            "Type '!back' to go back to other options you have.".format(self.keyword_advance)
        )
        msg = await self.client.wait_for('message', check=lambda
            message: message.author == self.message.author and message.content.startswith("!"))
        # Maybe add timeout?
        self.input = str(msg.content)


class Choice2(Choice):

    def __init__(self, client, message):
        super().__init__("!go closer to the abyss", "!jump in", client, message)

        self.next_scene = LoseScene(self.client, self.message)

    async def prompt_choice(self):
        await self.mention()
        await self.message.channel.send(
            "You can hear a faint howling deep inside whatever dwells in the abyss. It grows louder as you approach "
            "the abyss. Your muscles grow tense as you approach the abyss behind the portal as if your body is "
            "naturally rejecting the aura around you. "
        )

    async def prompt_options(self):
        await self.message.channel.send(
            "Type '{}' to jump into the abyss.\n"
            "Type '!listen' to listen to the faint howling.\n"
            "Type '!back' to back away from the howling.".format(self.keyword_advance)
        )
        msg = await self.client.wait_for('message', check=lambda
            message: message.author == self.message.author and message.content.startswith("!"))
        # Maybe add timeout?
        self.input = str(msg.content)


class Scene1(Scene):

    def __init__(self, client, message):
        super().__init__(client, message)

        self.choice_1 = Choice1(self.client, self.message)
        self.choice_2 = Choice2(self.client, self.message)

    async def prompt_scene(self):
        await self.message.channel.send(
            "Welcome, {}.\n"
            "You are trapped in a close space unfamiliar to you. No one is around you, nothing is around you. "
            "The ominous silence is starting to get under your nerve as you look around the place to find an opening.\n"
            "And then, with blinding rays of lights and an explosion, a portal is opened in front of you. "
            "Also, the ground behind the portal has collapsed. It seems like it's a quite jump from where you are "
            "standing. "
            "Also, the then-silence is not filled with a bit of noise coming from the newly-created "
            "abyss.".format(self.message.author.mention)
        )

    async def prompt_options(self):
        await self.break_line()
        await self.message.channel.send(
            "Type '{}' to look into the portal.\n"
            "Type '{}' to go closer to the abyss.".format(self.choice_1.keyword_trigger, self.choice_2.keyword_trigger)
        )
        msg = await self.client.wait_for('message', check=lambda
            message: message.author == self.message.author and message.content.startswith("!"))
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
            await self.prompt_options()
        elif self.choice_1.input == self.choice_1.keyword_advance:
            await self.choice_1.next_scene.play()
        elif self.choice_1.input == "!read note":
            await self.mention()
            await self.message.channel.send(
                "The note reads as follow:\n"
                "'Will you take the only chance you have?'"
            )
            await self.play_choice_1()
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
            await self.prompt_options()
        elif self.choice_2.input == self.choice_2.keyword_advance:
            await self.choice_2.next_scene.play()
        elif self.choice_2.input == "!listen":
            await self.mention()
            await self.message.channel.send(
                "You cannot make out whatever is coming from the abyss."
            )
            await self.play_choice_2()
        elif self.choice_2.input == "!game" or self.choice_2.input == "!end":
            await AbruptEndScene(self.client, self.message).play()
        else:
            await self.mention()
            await self.prompt_inappropriate_answer()
            await self.play_choice_2()
