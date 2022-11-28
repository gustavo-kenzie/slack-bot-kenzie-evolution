import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


load_dotenv()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))


@app.command("/pergunta")
def ask_question(ack, command):
    ack()
    questioner = command["user_id"]
    destination_channel = "C04C3CBHBPC"
    question_text = command["text"]
    display_text = f"Pergunta enviada por <@{questioner}>\n{question_text}"
    blocks = [
        {"type": "divider"},
        {"type": "section", "text": {"type": "mrkdwn", "text": display_text}},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Reivindicar pergunta", "emoji": True},
                    "value": "click_me_123",
                    "action_id": "claim",
                }
            ],
        },
    ]
    app.client.chat_postMessage(channel=destination_channel, text="UNCLAIMED", blocks=blocks)
    

@app.action("claim")
def claim_question(ack, body):
    ack()
    ts = body["message"]["ts"]
    channel = body["channel"]["id"]
    user_id = body["user"]["id"]
    blocks = body["message"]["blocks"]
    blocks[-1] = {"type": "section", "text": {"type": "mrkdwn", "text": f"Pergunta reivindicada por <@{user_id}>"}}
    app.client.chat_update(channel=channel, text="CLAIMED", blocks=blocks, ts=ts)


handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
handler.start()
