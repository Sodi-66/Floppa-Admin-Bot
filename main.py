import telebot
import callbacks  # Импортируем модуль с колбеками
import content_types  # Импортируем модуль с content_types
import commands  # Импортируем модуль с логикой команд


tg_token = '6111629120:AAGIK6PhWBL6lTLeKhXRTbZ-H55Mg-7Y8Fs'

bot = telebot.TeleBot(tg_token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    commands.start_message(message)


@bot.message_handler(commands=['help'])
def main_help_message(message):
    commands.help_message(message)


@bot.message_handler(commands=['based'])
def main_create_base(message):
    commands.create_base(message)


@bot.message_handler(commands=['users'])
def main_get_users(message):
    commands.get_users(message)


@bot.message_handler(commands=['selfdata'])
def main_self_data(message):
    commands.self_data(message)


@bot.message_handler(commands=['warn'])
def main_warn_user(message):
    commands.warn_user(message)


@bot.message_handler(commands=['unwarn'])
def main_unwarn_user(message):
    commands.unwarn_user(message)


@bot.message_handler(commands=['mute'])
def main_mute_user(message):
    commands.mute_user(message)


@bot.message_handler(commands=['unmute'])
def main_unmute_user(message):
    commands.unmute_user_all(message)


@bot.message_handler(commands=['kick'])
def main_kick_user(message):
    commands.kick_user(message)


@bot.message_handler(commands=['fish'])
def main_fishing(message):
    user_id = message.from_user.id
    commands.fishing(message, user_id)


@bot.message_handler(commands=['rock'])
def rock_game(message):
    commands.play(message)


@bot.message_handler(commands=['random'])
def random_game(message):
    commands.start_game(message)


@bot.message_handler(content_types=['new_chat_members'])
def main_new_memeber(message):
    content_types.welcome_new_members(message)


@bot.message_handler(content_types=['left_chat_member'])
def main_left_member(message):
    content_types.farewell_member(message)


@bot.message_handler(content_types=['text'])
def main_text_message(message):
    content_types.text_message(message)


@bot.callback_query_handler(func=lambda call: call.data in ['камень', 'ножницы', 'бумага'])
def main_callback_rps(call):
    callbacks.callback_rps(call)


@bot.callback_query_handler(func=lambda call: True)
def inline_buttons(call):
    callbacks.handle_inline_buttons(call)


bot.polling(none_stop=True)
