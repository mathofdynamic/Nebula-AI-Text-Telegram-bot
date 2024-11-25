Nebula Text AI Bot
Welcome to the Nebula Text AI Bot repository! This project provides a versatile Telegram bot designed to process text using advanced AI capabilities. The bot acts as a bridge between Telegram and a local AI server, powered by the Ollama 405B LLM.

Features
Tone Rephrasing: Transform text into various tones:
Friendly
Professional
Creative
Summarization: Generate concise summaries of long texts.
Key Points Extraction: Extract key insights from any given text.
Multi-Language Support: Process text in multiple languages seamlessly.
Local Hosting: Code runs locally, offering greater control and privacy.
Demo
Telegram Bot Link

Watch the bot in action: Demo Video (add link to video)

Prerequisites
Python 3.8 or higher
Libraries: Install dependencies using pip install -r requirements.txt.
Telegram Bot Token: Get a bot token from Telegram's BotFather.
AI Server API: Set up the Ollama 405B LLM or your preferred AI server.
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/nebula-text-ai-bot.git  
cd nebula-text-ai-bot  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Set up environment variables:

Telegram Bot Token:
bash
Copy code
export TOKEN=<your-telegram-bot-token>  
AI Server API Key:
bash
Copy code
export LEPTON_API_TOKEN=<your-api-key>  
Run the bot:

bash
Copy code
python bot.py  
Usage
Add the bot to your Telegram account.
Use the following commands:
/start – Get a welcome message and bot usage instructions.
/friendly [text] – Rephrase text in a friendly tone.
/professional [text] – Rephrase text professionally.
/creative [text] – Add creativity to your text.
/summarize [text] – Generate a concise summary.
/keypoints [text] – Extract key points from the text.
Example
Input:

vbnet
Copy code
/friendly This is a reminder that your payment is overdue. Please settle it soon to avoid penalties.  
Output:

vbnet
Copy code
Hey! Just a quick reminder about your overdue payment. We'd appreciate it if you could settle it soon to avoid any penalties. Thanks! 😊  
Contributions
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Support
If you encounter any issues or have questions, please open an issue or reach out via Telegram.

Crafted with ❤️ by Nebula Design Agency.
