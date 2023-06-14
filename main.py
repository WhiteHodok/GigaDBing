import os
import re
from EdgeGPT import Chatbot, ConversationStyle
import interactions

TOKEN = "" # Тут токен твоего бота
COOKIE_PATH = 'cookie.json'
bot = interactions.Client(token=TOKEN)
EDGES = {}
my_conversation_style = ConversationStyle.balanced

guild_ids = [""]  # Айдишка твоего сервера-канала
#Обязательно заюзай как только включил бота
@interactions.slash_command(
    name="start",
    description="Старт бота"
)
async def _start(ctx: interactions.SlashContext):
    global EDGES
    EDGES[ctx.author.id] = Chatbot(cookie_path=COOKIE_PATH)
    await ctx.send(f"Ку, {ctx.author.name}! Юзай /help для большей информации.")

@interactions.slash_command(
    name="help",
    description="Показать список команд",
)
async def _help(ctx: interactions.SlashContext):
    response = "Введи /help для инфы\nДля смены стиля, введи /switch и следуй: \ncreative (Creative)\nbalanced (Balanced)\nprecise (Strict)"
    await ctx.send(response)

@interactions.slash_command(
    name="switch",
    description="Свитч стиля беседы",
)
async def _switch(ctx: interactions.SlashContext, style: str):
    global my_conversation_style
    styles = {
        "creative": ConversationStyle.creative,
        "balanced": ConversationStyle.balanced,
        "precise": ConversationStyle.precise
    }
    my_conversation_style = styles[style]
    await ctx.send(f"Current style: {style.capitalize()}")

@interactions.slash_command(
    name="ask",
    description="Задай мне вопрос",
)
async def _ask(ctx: interactions.SlashContext, question: str):
    global EDGES
    edge = EDGES.get(ctx.author.id)
    if edge is None:
        await ctx.send("Сначала ты должен запустить бота! Use /start")
        return
    response = edge.chat(question, my_conversation_style)
    await ctx.send(response)

bot.start()

