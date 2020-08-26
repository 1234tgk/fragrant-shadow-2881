from .fgame.scene_1 import Scene1


async def game(client, message):
    await Scene1(client, message).play()
