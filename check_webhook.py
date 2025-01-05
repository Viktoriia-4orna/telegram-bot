import requests

BOT_TOKEN = "7909571239:AAGnwMaYVqBBRyZ-bRbnR2Kj1u5SZ4t9UEI"  # Замените на ваш токен
response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo")
print(response.json())

# Если вебхук активен, удалите его
if response.json().get("result", {}).get("url"):
    delete_response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook")
    print("Webhook удалён:", delete_response.json())
else:
    print("Webhook не активен.")
