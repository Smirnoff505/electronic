# Electronics_network!

## Установка зависимостей

Для корректной работы программы необходимо установить:

`python = "^3.10"`

`django = "4.2"`

`pillow = "^10.3.0"`

`psycopg2-binary = "^2.9.9"`

`djangorestframework = "^3.15.1"`

`python-dotenv = "^1.0.1"`

`ipython = "^8.24.0"`

`django-filter = "^24.2"`

`flake8 = "^7.0.0"`

## Миграции

Перед запуском приложения выполните миграции

`python manage.py migrate`

## Создание суперпользователя

Чтобы создать суперпользователя, выполните следующую команду: 

`python manage.py createsuperuser`

## Проверка кода с помощью Flake8

`flake8 --max-line-length 120 --exclude=*/migrations/*`

## Заполнение файла .env

Заполните файл `.env` согласно примеру заполнения `env.simple`.