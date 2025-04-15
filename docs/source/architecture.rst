Project Architecture
====================

The bot is built using a modular structure:

- `bot.py` — main file containing the Telegram bot logic.
- OMDb API is used to fetch movie information.
- Telegram bot handles user commands, processes input, and sends responses.
- Functions are isolated and structured by responsibility: input parsing, API requests, and message formatting.

Technologies used:

- Python 3.12
- Telegram Bot API (`pyTelegramBotAPI`)
- OMDb API
- Sphinx (for documentation)
