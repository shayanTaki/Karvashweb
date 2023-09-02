from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Reservation
from .telegram_utils import send_to_telegram

def index(request):


    if request.method == 'POST':
        # دریافت اطلاعات فرم از صفحه HTML
        user_name = request.POST.get('name')
        user_number = request.POST.get('number')
        vehicle_model = request.POST.get('vehicle_model')
        vardati = request.POST.get('varedati')
        # iranichini = request.POST.get('iranichini')
        vehicle_type = "خودروی وارداتی"

        vax = request.POST.get('vax')
        sefrshoii = request.POST.get('sefr-shoii')




        selected_month = request.POST.get('month')
        selected_day = request.POST.get('day')
        selected_time = request.POST.get('time')

        # تشکیل تاریخ و زمان به صورت یک رشته
        selected_date_time = f'1402-{selected_month}-{selected_day} {selected_time}:00:00'

        # چک کردن آیا تاریخ در دیتابیس وجود دارد یا نه
        if not Reservation.objects.filter(date_time=selected_date_time).exists():
            # ذخیره اطلاعات در دیتابیس
            reservation = Reservation(

                phone_number=user_number,
                date_time=selected_date_time
            )
            reservation.save()

            # نمونه توکن و شناسه گفتگوی تلگرام
            telegram_token = '6632318287:AAEgdJZ_VNMomNJ6-1M9Q-IyFhSWqVwJoBs'
            telegram_chat_id = '5744873119'

            if vardati == True:
                vehicle_type = "خودروی وارداتی"
            else:
                vehicle_type = "ایرانی و چینی"

            if vax:
                vax = "دارد"
            else:
                vax ="ندارد"


            if sefrshoii :
                sefrshoii = "دارد"
            else:
                sefrshoii = "ندارد"
            # ایجاد پیام برای ارسال به تلگرام
            message = f'رزرو جدید:\nنام: {user_name}\nشماره تلفن: {user_number}\nمدل ماشین: {vehicle_model}\nنوع خودرو: {vehicle_type}\n وکس: {vax}\n صفر شویی: {sefrshoii}\nتاریخ و زمان: {selected_date_time}'

            # ارسال پیام به تلگرام
            if send_to_telegram(telegram_token, telegram_chat_id, message):
                result_message = 'رزرو با موفقیت به تلگرام ارسال شد.'
            else:
                result_message = 'ارسال رزرو به تلگرام ناموفق بود.'
        else:
            # اگر تاریخ در دیتابیس وجود داشته باشد، به ویو دیگری منتقل می‌شویم
            return render(request, 'Atlas/none.html')

    return render(request, 'Atlas/index.html')