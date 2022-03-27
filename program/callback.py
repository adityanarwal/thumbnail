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


from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""**Hello !! I am Izumi player to help group owner , admins and members with my super advance features, 
For reporting any issues regarding me kindly report in my support chat so my developers can Fix me out for your needs.
- - - - - - - - - - - - - - - - - - - - - - - 
ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- [𝗖𝗙𝗖](https://t.me/CloseFriendsCommunity)
- - - - - - - - - - - - - - - - - - - - - - -
Use inline buttons given below to know more about me.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Commands❓", callback_data="command_list"),
                    InlineKeyboardButton("About 💬", callback_data="user_guide")
                ],[
                    InlineKeyboardButton("✚ Add Me To Your Group ✚", url="https://t.me/{me_bot.username}?startgroup=true")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""ℹ️ Quick use Guide bot, please read fully !

👩🏻‍💼 » /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

👩🏻‍💼 » /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

👩🏻‍💼 » /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

❓ Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="user_guide")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""**Izumi Music Bot is the bot designed by some noobs team for playing a high quality and unbreakable music in your groups voice chat.

This bot helps you to play music to search music from youtube and to download music and video from youtube server and many more features related to telegram voice chat.

Thanks !!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Network 📡", url=f"https://t.me/CloseFriendsCommunity"),
                    InlineKeyboardButton("Owner 🧑‍💻", url=f"https://t.me/PhoenixWarmed")
                ],[
                    InlineKeyboardButton("Support 📨", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton("Updates 📨", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton("Developer™", url="https://t.me/Its_romeoo")
                ],[
                    InlineKeyboardButton("🔙 𝗕𝖺𝖼𝗄 𝗛𝗈𝗆𝖾", callback_data="home_start")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Heyy [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» Check out the menu below to read the module information & see the list of available Commands !
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝗖𝗆𝖽𝗌 𝗙𝗈𝗋 𝗚𝗋𝗈𝗎𝗉 𝗔𝖽𝗆𝗂𝗇𝗌", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("𝗖𝗆𝖽𝗌 𝗙𝗈𝗋 𝗚𝗋𝗈𝗎𝗉 𝗠𝖾𝗆𝖻𝖾𝗋𝗌", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("🔙 𝗕ack 𝗛𝗈𝗆𝖾", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✨ 𝗖𝗺𝗱𝘀 𝗙𝗼𝗿 𝗚𝗿𝗼𝘂𝗽 𝗠𝗲𝗺𝗯𝗲𝗿𝘀.

» /play (song name/youtube link) - play the music from youtube
» /stream (m3u8/youtube live link) - play youtube/m3u8 live stream music
» /playlist - view the queue list of songs and current playing song
» /lyric (query) - search for song lyrics based on the name of the song
» /song (query) - download song from youtube
» /repo - Get The Bot Repo !!
» /search (query) - search for the youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""✨ 𝗖𝗺𝗱𝘀 𝗙𝗼𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗱𝗺𝗶𝗻𝘀.

» /pause - pause the current track being played
» /resume - play the previously paused track
» /skip - goes to the next track
» /stop - stop playback of the track and clears the queue
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /refresh - refresh the bot server and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group
» /startvc - start/restart the group call
» /stopvc - stop/discard the group call""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.

» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /speedtest - run the bot server speedtest
» /sysinfo - show the system information
» /logs - generate the current bot logs
» /eval - run an code
» /sh - run an code""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» /gban (`username` or `user_id`) - for global banned people, can be used only in group
» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» /restart - restart your bot server
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» /broadcast (`message`) - send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
