# Wedding Bot

Wedding Bot - это Telegram-бот, созданный для предоставления информации о моей свадьбе 🥂🥂🥂. Бот предоставляет различные команды для получения информации о погоде, оставшихся днях до свадьбы и других деталях мероприятия. Бот доступен по никнейму @LoveStoryGuideBot

***

## Установка

Бот предназначен для личных целей, но вы можете установить его и пользоваться в своих целях. Для этого:

1. Склонируйте репозиторий:
```
git clone https://github.com/your-username/wedding-bot.git
```

2. Создайте виртуальное окружение:
```
python -m venv venv
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

4. Создайте файл .env и добавьте свой токен для Telegram Bot API и ключ OpenWeatherMap API:
```
TOKEN=your_telegram_token
WEATHER_API=your_openweathermap_api_key
```
- для получения токена телеграм, найдите в телеграме BotFather и напишите команду
```
/newbot
```

- для получения API погоды зайдите на сайт [https://openweathermap.org/](https://openweathermap.org/) и следуйте рекомендациям получения API ключа.

5. Исходя из своих предпочтений, измените данные в сообщениях бота в файле messages.py, а также дату свадьбы и координаты места проведения мероприятия в файле main.py

6. Запустите бот:
```
make start
```

***

## Команды
```
/start - Начало общения с ботом.
/info - Получение общей информации о свадьбе.
/weather - Получение текущей погоды в месте проведения свадьбы.
/days_left - Узнать, сколько дней осталось до свадьбы.
```

***
## Контакты
- Автор: Grigoriy Kruchinin
- [GitHub](https://github.com/GrigoriyKruchinin)
- [Email](gkruchinin75@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/grigoriy-kruchinin/)
***