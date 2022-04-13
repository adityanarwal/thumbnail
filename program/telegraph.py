from telegraph import upload_file
from pyrogram import filters


@Client.on_message(command(["telegraph"]) & ~filters.edited)
async def help(client: Client, message: Message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("**Getting Telegraph Link Of Your Given Media. Please wait !!**")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'Your telegraph [link]({url})', disable_web_page_preview=True)
