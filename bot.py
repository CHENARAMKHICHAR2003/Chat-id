from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Function to handle the /start command
def start(update: Update, context: CallbackContext):
    user_first_name = update.message.from_user.first_name
    greeting_message = f"Hello, {user_first_name}! 🎉\nWelcome to the Stylish Bot.\n\nHere are the commands you can use:\n\n"
    greeting_message += "/start - Start interacting with the bot.\n"
    greeting_message += "/send_message - Send a message to a specific user using their chat_id.\n"
    greeting_message += "/help - View all available commands and their descriptions.\n"
    update.message.reply_text(greeting_message)

# Function to send a message to the user using their chat_id
def send_message_to_user(update: Update, context: CallbackContext):
    user_chat_id = 7679286299  # Chat ID of the user you want to send the message to
    message = """✨ *Hello!* ✨
    This is a message from your bot.
    
    I'm here to help you out with cool features. Enjoy! 😎
    
    Use commands like /start to interact with me.
    """
    # Send a stylish message to the user
    context.bot.send_message(chat_id=user_chat_id, text=message, parse_mode='Markdown')

    # Confirm message sent in the bot console
    update.message.reply_text("Your message was sent to the user successfully! 🚀")

# Function to handle the /help command
def help(update: Update, context: CallbackContext):
    help_message = """*Bot Commands:*
    
    /start - Start interacting with the bot. You'll get a greeting and introduction to commands.
    
    /send_message - Send a message to a specific user using their chat_id. The message will be sent directly to the user.
    
    /help - View all available commands with explanations. Use this command anytime you need guidance.
    
    🤖 **Bonus Tips:**
    - Feel free to chat with me! I'll echo any message you send.
    - Use Markdown formatting in your messages to make them more stylish! Try it out! 💬
    """
    update.message.reply_text(help_message, parse_mode='Markdown')

# Function to handle messages (echo the user's text)
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"💬 You said: {update.message.text}\n\nFeel free to try again!")

# Main function to set up the bot
def main():
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    updater = Updater("YOUR_API_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Add command handler for /send_message
    dp.add_handler(CommandHandler("send_message", send_message_to_user))

    # Add command handler for /help
    dp.add_handler(CommandHandler("help", help))

    # Add message handler to echo user messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
