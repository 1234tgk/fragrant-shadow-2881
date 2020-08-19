async def help_me(message):
    help_str = "Here are the list of commands:" \
               "!help: See the list of commands" \
               "!hi: Bot'Zach will greet you back" \
               "!time: Display the current time in UTC"
    await message.channel.send(help_str)
