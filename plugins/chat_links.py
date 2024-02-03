from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from datetime import datetime, timedelta



channels = [-1001658823824] # chat-ids
expiry = 3 # minutes

@Client.on_message(filters.private & filters.command("joinchannels"))
async def joinchannels(client: Client, message: Message):
    
    reply = await message.reply("Please wait..")
    try:
        await reply.edit(
            f"Here's the links\nLinks will **expire in {expiry} minutes**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Chat {i + 1}", url=link)]
            for i, link in enumerate([(await client.create_chat_invite_link(channel, expire_date=datetime.now() + timedelta(minutes=expiry))
            ).invite_link for channel in channels])]))
    except:
        return await reply.edit("Error in generating links")
        
        
    
