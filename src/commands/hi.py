async def hi(message):
    await message.channel.send('Hello, ' + str(message.author) + "!")
