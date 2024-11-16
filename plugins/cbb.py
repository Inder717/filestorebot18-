from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Callback handler function
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        # Define the new about text with HTML formatting
        new_text = (
            "<b>⟦⟧ Hi there!  \n ┏━━━━━━━❪❂❫━━━━━━━━\n"
            "◈ Creator : <a href=https://t.me/n_flixmovie>n_flixmovie</a>\n"
            "◈ Developer : <a href=https://t.me/netfilix_movie>netfilix_movie</a>\n"
            "┗━━━━━━━❪❂❫━━━━━━━━</b>"
        )
        
        # Check if the message text is already same, then update it
        if query.message.text != new_text:
            await query.message.edit_text(
                text=new_text,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔒 Close", callback_data="close")]]
                )
            )

        # Send a photo after the "about" message with a caption
        await query.message.reply_photo(
            photo="https://example.com/path/to/your/image.jpg",  # Replace with actual image URL or file path
            caption="(©) @n_flixmovie"
        )

    elif data == "close":
        # Delete the message when "close" is pressed
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass  # Ignores errors if there's no reply message to delete
