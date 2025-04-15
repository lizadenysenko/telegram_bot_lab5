Component Interaction
=====================

Key components:

1. **User** — sends a command message to the bot.
2. **Telegram Bot API** — forwards the message to the backend logic in `bot.py`.
3. **OMDb API** — performs search queries using parameters (e.g. movie title).
4. **Bot** — receives JSON responses, parses them, and builds messages for the user.

All logic is based on command handlers (`@bot.message_handler`).
