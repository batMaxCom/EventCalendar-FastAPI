# Календарь событый на базе фреймворка FastAPI
## Описание
Суть проекта заключается разработка API для взаимодействия с календарем событий для авторизованных пользователей.

## Структура
Структура проекта созадна на основе [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)

Имеет следющий вид:
```
│   .env
│   .gitignore
│   alembic.ini
│   docker-compose.yml
│   README.md
│   requirements.txt
│           
├───migration
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│   └───versions
├───src
│   │   config.py
│   │   database.py
│   │   main.py
│   │
│   ├───auth
│   │       config.py
│   │       dependencies.py
│   │       exceptions.py
│   │       models.py
│   │       routers.py
│   │       schemas.py
│   │       service.py
│   │       utils.py
│   │       __init__.py
│   │
│   └───event_calendar
│           config.py
│           dependencies.py
│           exceptions.py
│           models.py
│           routers.py
│           schemas.py
│           service.py
│           utils.py
│           __init__.py
│
├───templates
├───tests
└───venv
```

## Инструменты

- FastAPI - веб-фреймворк
- PostgreSQL - база данных
    - SQLAlchemy - ORM для работы с БД
    - asyncpg - асинхронный драйвер для подключения к БД PostgreSQL
- Alembic - миграции БД
- Pydantic - валидация, сериализация и десериализация файлов