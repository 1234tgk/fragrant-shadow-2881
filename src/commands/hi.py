async def hi(message):
    await message.channel.send('Hello, ' + message.author.mention + "!")
