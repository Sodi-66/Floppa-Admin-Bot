from telebot import types
import telebot

# Список рыб и мусора для игры "рыбалка"
fishes = ['Коричневая рыба🟫', 'Синяя рыба🐟', 'Жёлтая рыба🐡', 'Золотая рыба🐠']
trash = ['Банки🥫🥫', 'Пакеты🛍', 'Бімба💣💥']


tg_token = '6111629120:AAGIK6PhWBL6lTLeKhXRTbZ-H55Mg-7Y8Fs'

bot = telebot.TeleBot(tg_token)

chat_states = {}  # Словарь для хранения состояний игр пользователей (рандомные числа)
last_play_time_fish = {}  # Словарь для хранения времени последней игры для каждого пользователя(рыбалка)
last_play_time_rps = {}  # Словарь для хранения времени последней игры для каждого пользователя(КНБ)

#  Главное меню бота
main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add(types.KeyboardButton('Моя стата'), types.KeyboardButton('Стата чата'),
                    types.KeyboardButton('Команды'), types.KeyboardButton('Игры'))
