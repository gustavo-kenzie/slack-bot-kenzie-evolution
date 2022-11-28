import requests
from dotenv import load_dotenv
import os


load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

def count_pending_questions():
    messages = requests.get(
        'https://slack.com/api/conversations.history?channel=C04C3CBHBPC',
        headers={
            'Authorization': f'Bearer {SLACK_BOT_TOKEN}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    ).json()['messages']
    pending_questions_sum = sum([1 for m in messages if m['text'] == 'UNCLAIMED'])
    requests.post(
        'https://slack.com/api/chat.postMessage',
        headers={
            'Authorization': f'Bearer {SLACK_BOT_TOKEN}',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            "channel": "C04C3CBHBPC",
            "text": f"Há *{pending_questions_sum}* perguntas aguardando resposta"
        }
    )