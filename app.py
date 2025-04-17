
from flask import Flask, request
import openai
import requests

app = Flask(__name__)

openai.api_base = "https://YOUR_PROXY_URL/v1"
openai.api_key = "YOUR_API_KEY"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        user_msg = data['messages'][0]['text']['body']
        user_number = data['messages'][0]['from']

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一名经验丰富的海外销售人员，专注于模块化房屋出口业务，语气自然真诚，尽量避免像AI。回答要简洁有礼貌，并适当引导客户。"},
                {"role": "user", "content": user_msg}
            ]
        )
        reply_text = response['choices'][0]['message']['content']
        print(f"Reply to {user_number}: {reply_text}")
    except Exception as e:
        print("Error:", e)
    return "ok", 200

if __name__ == '__main__':
    app.run(port=5000)
