import requests

bot_token = '7194616295:AAHbkcLHFa58jLuG-tvQ0C91kIhyShHK4Vw'
channel_chat_id = '1173453067'  # Your numeric chat ID

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    'chat_id': channel_chat_id,
    'text': 'This is a test message.'
}

response = requests.post(url, data=payload)
print(response.json())
