import discord
from discord.ext import commands
import json
import sqlite3
import logging
from core.ai_integration import get_ai_response  # AI integration

# Load configuration
with open('core/config.json', 'r') as f:
    config = json.load(f)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Database setup
def init_db():
    conn = sqlite3.connect('core/omnibot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (user_id TEXT, username TEXT, content TEXT, timestamp TEXT, channel_id TEXT)''')
    conn.commit()
    conn.close()

# Load event handlers
@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user}")
    init_db()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Log message in database
    conn = sqlite3.connect('core/omnibot.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)",
              (str(message.author.id), message.author.name, message.content,
               str(message.created_at), str(message.channel.id)))
    conn.commit()
    conn.close()

    # AI Response Handling
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        ai_response = get_ai_response(message.content)
        await message.reply(ai_response)

    await bot.process_commands(message)

# AI Command
@bot.command()
async def ask(ctx, *, question: str):
    """ AI-powered command to answer user queries. """
    ai_response = get_ai_response(question)
    await ctx.send(ai_response)

# Run the bot
if __name__ == "__main__":
    bot.run(config['token'])
