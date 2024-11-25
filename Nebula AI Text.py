import os
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Set your Lepton API token (environment variable or directly)
LEPTON_API_TOKEN = os.getenv('LEPTON_API_TOKEN')

# Define the bot token (replace with your actual bot token)
TOKEN = '7232776590:AAHg2YB2SoWD5XWQ6ws42I22JapUnICSXgs'

# Initialize the Lepton client
client = openai.OpenAI(
    base_url="https://llama3-1-405b.lepton.run/api/v1/",
    api_key=LEPTON_API_TOKEN
)

# Function to send messages to Lepton API
def send_message_to_lepton(message: str, system_prompt: str) -> str:
    """
    Sends a message to Lepton API with a system prompt.

    Args:
        message (str): The text to process.
        system_prompt (str): Instructions or role for the LLM.

    Returns:
        str: Processed response from the Lepton API.
    """
    try:
        completion = client.chat.completions.create(
            model="llama3.1-405b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=512,
            stream=True,
        )

        response = ""
        for chunk in completion:
            if chunk.choices:
                content = chunk.choices[0].delta.content
                if content:
                    response += content
        return response if response else "No response from Lepton."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🌠 Welcome to Nebula Text AI! Use commands like:\n"
        f"`/friendly [text]` to make text friendly,\n"
        f"`/professional [text]` for a professional tone,\n"
        f"`/creative [text]` to add creativity.\n"
        f"`/summarize [text]` to summarize text, or `/keypoints [text]` for a list of key points.\n"
        f"Type `/help` for more info!",
        reply_to_message_id=update.message.message_id  # Reply to the user's message
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Nebula Text AI Commands:*\n\n"
        "/friendly [text] - Rephrase text in a friendly tone.\n"
        "/professional [text] - Make text sound professional.\n"
        "/creative [text] - Add a creative flair to your text.\n"
        "/summarize [text] - Summarize the given text.\n"
        "/keypoints [text] - Extract key points from the text.\n"
        "\nType the command followed by your text!",
        reply_to_message_id=update.message.message_id  # Reply to the user's message
    )

async def tone_command(update: Update, context: ContextTypes.DEFAULT_TYPE, tone: str):
    if len(context.args) < 1:
        await update.message.reply_text(
            "⚠️ Please provide the text after the command!",
            reply_to_message_id=update.message.message_id  # Reply to the user's message
        )
        return

    text = ' '.join(context.args)
    system_prompts = {
        "friendly": "You are a text rephrasing assistant. Rephrase the given text in a friendly tone while keeping the meaning intact. Respond only with the rephrased text, without additional commentary or conversation.",
        "professional": "You are a text rephrasing assistant. Rephrase the given text in a professional tone while maintaining clarity and the original intent. Respond only with the rephrased text, without additional commentary or conversation.",
        "creative": "You are a text rephrasing assistant. Rephrase the given text in a creative tone, adding engaging language while preserving the original meaning. Respond only with the rephrased text, without additional commentary or conversation.",
        "summarize": "You are a text summarization assistant. Summarize the given text concisely and provide the key message without changing its meaning. Respond only with the summarized text, without additional commentary or conversation.",
        "keypoints": "You are a text analysis assistant. Extract and list the key points from the given text in bullet format. Respond only with the list of key points, without additional commentary or conversation."
    }

    # Send loading emoji message
    loading_message = await update.message.reply_text("✨⏳✨")

    try:
        response = send_message_to_lepton(text, system_prompts[tone])
        # Delete the loading message
        await loading_message.delete()
        # Send the actual response
        await update.message.reply_text(
            response,
            reply_to_message_id=update.message.message_id  # Reply to the user's message
        )
    except Exception as e:
        # Delete the loading message
        await loading_message.delete()
        await update.message.reply_text(
            f"❌ Error: {e}",
            reply_to_message_id=update.message.message_id  # Reply to the user's message
        )

# Wrappers for specific tone commands
async def friendly_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await tone_command(update, context, "friendly")

async def professional_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await tone_command(update, context, "professional")

async def creative_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await tone_command(update, context, "creative")

async def summarize_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await tone_command(update, context, "summarize")

async def keypoints_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await tone_command(update, context, "keypoints")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

# Main
if __name__ == '__main__':
    print('Starting Nebula Text AI bot...')
    app = Application.builder().token(TOKEN).build()

    # Add Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('friendly', friendly_command))
    app.add_handler(CommandHandler('professional', professional_command))
    app.add_handler(CommandHandler('creative', creative_command))
    app.add_handler(CommandHandler('summarize', summarize_command))
    app.add_handler(CommandHandler('keypoints', keypoints_command))

    # Error Handler
    app.add_error_handler(error)

    # Run the bot
    app.run_polling(poll_interval=3)
