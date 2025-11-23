import telebot
from telebot import types

# توکن جدید را اینجا بگذار
BOT_TOKEN = "8420099030:AAGijw99H9ejJ1obKR_K7LebLWEv2yMNMww"

bot = telebot.TeleBot(BOT_TOKEN)


# وقتی کاربر /start را بزند
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🧠 کلینیک رفتار")
    btn2 = types.KeyboardButton("🎓 آموزشگاه فرارَفتار")
    btn3 = types.KeyboardButton("📚 انتشارات روانشناسی و هنر")
    btn4 = types.KeyboardButton("💬 پشتیبانی و ارتباط با ما")

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)

    text = (
        "سلام 👋\n"
        "به ربات انستیتو رفتار خوش آمدید.\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
    )

    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    if message.text == "🧠 کلینیک رفتار":
        bot.send_message(
            message.chat.id,
            "بخش کلینیک رفتار:\n"
            "برای رزرو نوبت لطفاً از طریق سامانه نوبت‌دهی اقدام کنید.\n\n"
            "🔗 لینک سامانه نوبت‌دهی:\n"
            "https://my.raftarinstitute.com/site/appointment\n\n"
            "در صورت نیاز می‌تونید با پشتیبانی هم در ارتباط باشید. 🙂"
        )

    elif message.text == "🎓 آموزشگاه فرارَفتار":
        bot.send_message(
            message.chat.id,
            "بخش آموزشگاه فرارَفتار:\n"
            "- اطلاعات کارگاه‌ها و دوره‌ها\n"
            "- شرایط پرداخت\n"
            "- زمان برگزاری\n\n"
            "برای اطلاعات بیشتر به این صفحه مراجعه کنید:\n"
            "https://raftarinstitute.com/academy/"
        )

    elif message.text == "📚 انتشارات روانشناسی و هنر":
        bot.send_message(
            message.chat.id,
            "بخش انتشارات روانشناسی و هنر:\n"
            "- معرفی کتاب‌ها\n"
            "- امکان مشاوره برای انتخاب کتاب\n\n"
            "برای مشاهده و خرید کتاب‌ها:\n"
            "https://raftarinstitute.com/%D8%A7%D9%86%D8%AA%D8%B4%D8%A7%D8%B1%D8%A7%D8%AA-%D8%B1%D9%88%D8%A7%D9%86%D8%B4%D9%86%D8%A7%D8%B3%DB%8C-%D9%88-%D9%87%D9%86%D8%B1/"
        )

    elif message.text == "💬 پشتیبانی و ارتباط با ما":
        bot.send_message(
            message.chat.id,
            "پشتیبانی و ارتباط با ما:\n"
            "📍 آدرس: خیابان جردن، بعد از کوچه هفدهم، پلاک 48، انستیتو رفتار\n"
            "📞 تلفن: 09196881428\n"
            "🌐 سایت: https://raftarinstitute.com\n\n"
            "در صورت نیاز پیام بدهید تا پشتیبان پاسخ دهد."
        )

    else:
        bot.send_message(
            message.chat.id,
            "من متوجه این پیام نشدم 🙂\n"
            "لطفاً از دکمه‌های منو استفاده کنید."
        )


print("ربات روشن شد ...")
bot.infinity_polling()
