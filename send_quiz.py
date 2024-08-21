import asyncio
import json
from telegram import Bot, Poll

bot_token = '7194616295:AAHbkcLHFa58jLuG-tvQ0C91kIhyShHK4Vw'
channel_chat_id = '@sanatancoaching'  # Replace with your channel's username or numeric ID

# Load questions from JSON file
def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Send a quiz to the Telegram channel
async def send_quiz(question_data, bot):
    question = question_data['question']
    options = question_data['options']
    correct_answer = question_data['correct_answer']

    await bot.send_poll(
        chat_id=channel_chat_id,
        question=question,
        options=options,
        type=Poll.QUIZ,
        correct_option_id=correct_answer
    )

async def main():
    bot = Bot(token=bot_token)
    questions = load_questions('questions.json')

    for question_data in questions:
        await send_quiz(question_data, bot)
        await asyncio.sleep(5)  # Sleep for 5 seconds between sends to avoid spamming

# Run the asynchronous function
asyncio.run(main())
