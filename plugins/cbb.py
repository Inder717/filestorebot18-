from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        # About information ke saath image bhejna
        await query.message.edit_text(
            text = (
                "<b>⟦⟧ Hi there!  \n ┏━━━━━━━❪❂❫━━━━━━━━\n"
                "◈ Creator : <a href=https://t.me/n_flixmovie>n_flixmovie</a>\n"
                "◈ Developer : <a href=https://t.me/netfilix_movie>netfilix_movie</a>\n"
                "┗━━━━━━━❪❂❫━━━━━━━━</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

        # "about" message ke baad image bhejna
        try:
            await query.message.reply_photo(
                photo="https://example.com/path/to/your/image.jpg",  # Yahan apni image ka URL ya file path dalna hai
                caption="(©) netfilix_movie"
            )
        except Exception as e:
            print(f"Error sending photo: {e}")  # Console me error dekhne ke liye

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass
