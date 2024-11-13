from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        new_text = (
            "<b>⟦⟧ Hi there!  \n ┏━━━━━━━❪❂❫━━━━━━━━\n"
            "◈ Creator : <a href=https://t.me/n_flixmovie>n_flixmovie</a>\n"
            "◈ Developer : <a href=https://t.me/netfilix_movie>netfilix_movie</a>\n"
            "┗━━━━━━━❪❂❫━━━━━━━━</b>"
        )
        
        # Check if the current text is already same as new_text
        if query.message.text != new_text:
            await query.message.edit_text(
                text=new_text,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
                )
            )

        # "about" message ke baad image bhejna
        await query.message.reply_photo(
            photo="https://example.com/path/to/your/image.jpg",
            caption="(©) @n_flixmovie"
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

