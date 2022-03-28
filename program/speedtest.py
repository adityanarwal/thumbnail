"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


import wget
import speedtest

from PIL import Image
from config import BOT_USERNAME as bname

from driver.filters import command
from driver.decorators import sudo_users_only
from driver.core import bot as app
from driver.utils import remove_if_exists

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(command(["speedtest", f"speedtest@{bname}"]) & ~filters.edited)

async def run_speedtest(_, message: Message):
    m = await message.reply_text("× 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝗖𝗙𝗖 𝖡𝗈𝗍𝗌 𝖲𝖾𝗋𝗏𝖾𝗋 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 !!")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("× 𝖣𝗈𝗐𝗇𝖫𝗈𝖺𝖽 𝖲𝗉𝖾𝖾𝖽 ⚡️")
        test.download()
        m = await m.edit("× 𝖴𝗉𝖫𝗈𝖺𝖽 𝖲𝗉𝖾𝖾𝖽 ⚡️")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("» 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 𝖱𝖾𝗌𝗎𝗅𝗍𝗌 𝖥𝗋𝗈𝗆 𝖳𝗁𝖾 𝗖𝗙𝗖 𝖲𝖾𝗋𝗏𝖾𝗋 !!")
    path = wget.download(result["share"])
    try:
        img = Image.open(path)
        c = img.crop((17, 11, 727, 389))
        c.save(path)
    except BaseException:
        pass

    output = f"""**» 𝗖𝗙𝗖 Bᴏᴛ Sᴇʀᴠᴇʀ Sᴘᴇᴇᴅ !!**
    
<u>**Client:**</u>
**• 𝙸𝚂𝙿 »** {result['client']['isp']}
**• 𝙲𝚘𝚞𝚗𝚝𝚛𝚢 »** {result['client']['country']}
  
<u>**Server:**</u>
**• 𝙽𝚊𝚖𝚎 »** {result['server']['name']}
**• 𝚂𝚎𝚛𝚟𝚎𝚛 »** {result['server']['country']}, {result['server']['cc']}
**• 𝚂𝚙𝚘𝚗𝚜𝚘𝚛 »** {result['server']['sponsor']}
**• 𝙻𝚎𝚝𝚎𝚗𝚌𝚢 »** {result['server']['latency']}

⚡️ **• 𝙿𝚒𝚗𝚐 »** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    remove_if_exists(path)
    await m.delete()
