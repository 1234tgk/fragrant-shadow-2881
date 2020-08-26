from datetime import datetime


async def time(message):
    current_time = datetime.now().astimezone(tz=None)
    date_str = current_time.strftime('%m/%d/%Y %H:%M:%S')
    user_tz = current_time.strftime('%Z')
    msg = "Current date and time ({}) is:\n{}"
    await message.channel.send(message.author.mention)
    await message.channel.send(msg.format(user_tz, date_str))
