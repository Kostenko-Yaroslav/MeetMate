from bot.bot_instance import bot
from users.models import Profile


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'hello user' )
    chat_id = message.chat.id
    telegram_user_id = message.from_user.id
    text = message.text

    token = text.split()[1] if len(text.split()) > 1 else None

    if token:
        try:
            profile = Profile.objects.get(unique_code=token)

            profile.telegram_id = telegram_user_id
            profile.chat_id = chat_id
            profile.save()

            bot.reply_to(message, "Успех!")

        except Profile.DoesNotExist:
            bot.reply_to(message, "Error: неверный токен или профиль не найден")

bot.infinity_polling()