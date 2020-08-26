async def help_me(message):
    help_str = "Here are the list of commands:\n" \
               "!help: See the list of commands\n" \
               "!hi: Bot'Zach will greet you back\n" \
               "!time: Display the current time in UTC\n" \
                "!game: Start your adventure!"
    await message.channel.send(message.author.mention)
    await message.channel.send(help_str)
