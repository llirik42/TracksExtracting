from os import getenv

from dotenv import load_dotenv


load_dotenv()

# токен авторизации клиента Яндекс-Музыки
# для корректной работы токен должен относиться к аккаунту, имеющему подписку на Яндекс-Музыку
YANDEX_MUSIC_CLIENT_TOKEN = getenv('YANDEX_MUSIC_CLIENT_TOKEN')

# язык, на котором будет осуществляться поиск на Youtube
YOUTUBE_SEARCH_LANGUAGE = 'en'

# регион, из которого будет осуществляться поиск на Youtube
YOUTUBE_SEARCH_REGION = 'US'
