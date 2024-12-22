from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import ParseMode

# Function to handle the /start command
async def start(update: Update, context):
    user_first_name = update.message.from_user.first_name
    greeting_message = f"Hello, {user_first_name}! 🎉\nWelcome to the Stylish Bot.\n\nHere are the commands you can use:\n\n"
    greeting_message += "/start - Start interacting with the bot.\n"
    greeting_message += "/send_message - Send a message to a specific user using their chat_id.\n"
    greeting_message += "/help - View all available commands and their descriptions.\n"
    await update.message.reply_text(greeting_message)

# Function to handle the /send_message command
async def send_message_to_user(update: Update, context):
    user_chat_id = 7679286299  # Example chat_id, replace with actual chat_id
    message = """✨ *Hello!* ✨
    This is a message from your bot.
    
    I'm here to help you out with cool features. Enjoy! 😎
    
    Use commands like /start to interact with me.
    """
    # Send a stylish message to the user
    await context.bot.send_message(chat_id=user_chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

    # Confirm message sent in the bot console
    await update.message.reply_text("Your message was sent to the user successfully! 🚀")

# Function to handle the /help command
async def help(update: Update, context):
    help_message = """*Bot Commands:*
    
    /start - Start interacting with the bot. You'll get a greeting and introduction to commands.
    
    /send_message - Send a message to a specific user using their chat_id. The message will be sent directly to the user.
    
    /help - View all available commands with explanations. Use this command anytime you need guidance.
    
    🤖 **Bonus Tips:**
    - Feel free to chat with me! I'll echo any message you send.
    - Use Markdown formatting in your messages to make them more stylish! Try it out! 💬
    """
    await update.message.reply_text(help_message, parse_mode=ParseMode.MARKDOWN)

# Function to handle messages (echo the user's text)
async def echo(update: Update, context):
    await update.message.reply_text(f"💬 You said: {update.message.text}\n\nFeel free to try again!")

# Main function to set up the bot
async def main():
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    application = Application.builder().token("YOUR_API_TOKEN").build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Add command handler for /send_message
    application.add_handler(CommandHandler("send_message", send_message_to_user))

    # Add command handler for /help
    application.add_handler(CommandHandler("help", help))

    # Add message handler to echo user messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot with polling
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
