import requests

def send_to_telegram(token, chat_id, message):
    try:
        # URL ارسال پیام به تلگرام
        url = f"https://api.telegram.org/bot{token}/sendMessage"

        # پارامترهای مورد نیاز برای ارسال پیام
        params = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }

        # ارسال درخواست POST به تلگرام
        response = requests.post(url, data=params)

        # چک کردن موفقیت ارسال
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        # در صورت بروز خطا، می‌توانید خطا را چاپ کرده و یا اقدامات دیگری انجام دهید
        print(f"Error sending message to Telegram: {str(e)}")
        return False
