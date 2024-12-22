from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Function to send a message to a user using their chat_id
def send_message_to_user(update: Update, context: CallbackContext):
    # Replace with the actual chat_id you want to send a message to
    user_chat_id = 123456789  # Example chat_id, replace with actual chat_id

    # Send a message to the user
    context.bot.send_message(chat_id=user_chat_id, text="Hello! This is a message from your bot.")

    # Optional: Confirm message sent in the bot console
    update.message.reply_text("Message sent to the user!")

# Define the start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I can send messages to users using their chat_id.')

# Define the main function to set up the bot
def main():
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    updater = Updater("YOUR_API_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for '/start'
    dp.add_handler(CommandHandler("start", start))

    # Add command handler to send a message to the user (replace chat_id manually)
    dp.add_handler(CommandHandler("send_message", send_message_to_user))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
