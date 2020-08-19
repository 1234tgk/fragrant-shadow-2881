from datetime import datetime, timezone


async def time(message):
    current_time = datetime.now().astimezone(tz=None)
    date_str = current_time.strftime('%m/%d/%Y %H:%M:%S')
    user_tz = current_time.strftime('%Z')
    msg = "{}'s current date and time ({}) is:\n{}"
    await message.channel.send(msg.format(str(message.author), user_tz, date_str))
