from .fgame.scene_1 import Scene1


async def game(client, message):
    await message.channel.send(
        "Welcome, and thank you for trying out this feature of Bot'Zach. "
        "If you want to end the game at anytime, type '!end' without quotation marks.\n"
        "Please note that the game itself can be very slow , but rest assure, the game is fully functional. "
        "If the bot freezes during the session, just wait a bit, and it will work as it's intended." 
        " Sorry for the minor inconvenience.\n Also, I apologize that the story itself is very sh*tty as of right now. "
        "This was made to test the game engine within the bot.\n"
        "Thank you for reading this preface. Hope you find this feature interesting.\n"
        "---------"
    )
    await Scene1(client, message).play()
