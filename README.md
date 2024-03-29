# Проект: api_yamdb

Авторы:
- matsabaleuski
- Innis8
- Serge561

# Описание

Проект YaMDb, а также REST API сервис для него.
Приложение позволяет:
- Добавлять новые произведения в базу данных. 
- Присваивать произведениям категорию и жанры и просматривать их.
- Оставлять отзывы к произведению.
- Оставлять комментарии к отзывам.

Часть сервисов доступна только после авторизации по JWT-токену.

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Innis8/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции из папки с файлом manage.py:

```
cd api_yamdb
python manage.py migrate
```

Запустить сервер:

```
python manage.py runserver
```

# Как пользоваться приложением:



# Сервис AUTH

Регистрация пользователей и выдача токенов

1. Регистрация нового пользователя

Получить код подтверждения на переданный email.

Права доступа: Доступно без токена.

Использовать имя 'me' в качестве username запрещено.

Поля email и username должны быть уникальными.

Запрос:
```
 POST /api/v1/auth/signup/
```
```
{
  "email": "string",
  "username": "string"
}
```

Ответ:
```
{
  "email": "string",
  "username": "string"
}
```


2. Получение JWT-токена

Получение JWT-токена в обмен на username и confirmation code.

Права доступа: Доступно без токена.

Запрос:
```
POST /api/v1/auth/token/
```
```
{
  "username": "string",
  "confirmation_code": "string"
}
```

Ответ:
```
{
  "token": "string"
}
```


# Сервис CATEGORIES

Категории (типы) произведений

1. Получение списка всех категорий

Получить список всех категорий

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/categories/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```


2. Добавление новой категории

Создать категорию.

Права доступа: Администратор.

Поле slug каждой категории должно быть уникальным.

Запрос:
```
POST /api/v1/categories/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Ответ:
```
{
  "name": "string",
  "slug": "string"
}
```


3. Удаление категории

Удалить категорию.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/categories/{slug}/
```


# Сервис GENRES

Категории жанров

1. Получение списка всех жанров

Получить список всех жанров.

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/genres/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```


2. Добавление жанра

Добавить жанр.

Права доступа: Администратор.

Поле slug каждого жанра должно быть уникальным.

Запрос:
```
POST /api/v1/genres/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Ответ:
```
{
  "name": "string",
  "slug": "string"
}
```


3. Удаление жанра

Удалить жанр.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/genres/{slug}/
```


# Сервис TITLES

Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

1. Получение списка всех произведений

Получить список всех объектов.

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/titles/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```


2. Добавление произведения

Добавить новое произведение.

Права доступа: Администратор.

Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего).

При добавлении нового произведения требуется указать уже существующие категорию и жанр.

Запрос:
```
 POST /api/v1/titles/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```


3. Получение информации о произведении

Информация о произведении

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/titles/{titles_id}/
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```


4. Частичное обновление информации о произведении

Обновить информацию о произведении

Права доступа: Администратор

Запрос:
```
PATCH /api/v1/titles/{titles_id}/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```


5. Удаление произведения

Удалить произведение.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/titles/{titles_id}/
```



# Сервис REVIEWS

Отзывы

1. Получение списка всех отзывов

Получить список всех отзывов.

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```


2. Добавление нового отзыва

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение.

Права доступа: Аутентифицированные пользователи.

Запрос:
```
 POST /api/v1/titles/{title_id}/reviews/
```
```
{
  "text": "string",
  "score": 1
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


3. Полуение отзыва по id

Получить отзыв по id для указанного произведения.

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


4. Частичное обновление отзыва по id

Частично обновить отзыв по id.

Права доступа: Автор отзыва, модератор или администратор.

Запрос:
```
PATCH /api/v1/titles/{title_id}/reviews/{review_id}/
```
```
{
  "text": "string",
  "score": 1
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


5. Удаление отзыва по id

Удалить отзыв по id

Права доступа: Автор отзыва, модератор или администратор.

Запрос:
```
 DELETE /api/v1/titles/{title_id}/reviews/{review_id}/
```


# Сервис COMMENTS

Комментарии к отзывам

1. Получение списка всех комментариев к отзыву

Получить список всех комментариев к отзыву по id

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```


2. Добавление комментария к отзыву

Добавить новый комментарий для отзыва.

Права доступа: Аутентифицированные пользователи.

Запрос:
```
 POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
```
{
  "text": "string"
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


3. Получение комментария к отзыву

Получить комментарий для отзыва по id.

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


4. Частичное обновление комментария к отзыву

Частично обновить комментарий к отзыву по id.

Права доступа: Автор комментария, модератор или администратор.

Запрос:
```
PATCH /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
```
{
  "text": "string"
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


5. Удаление комментария к отзыву

Удалить комментарий к отзыву по id.

Права доступа: Автор комментария, модератор или администратор.

Запрос:
```
 DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```



# Сервис USERS

Пользователи

1. Получение списка всех пользователей

Получить список всех пользователей.

Права доступа: Администратор

Запрос:
```
 GET /api/v1/users/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
```


2. Добавление пользователя

Добавить нового пользователя.

Права доступа: Администратор

Поля email и username должны быть уникальными.

Запрос:
```
 POST /api/v1/users/
```
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


3. Получение пользователя по username

Получить пользователя по username.

Права доступа: Администратор

Запрос:
```
 GET /api/v1/users/{username}/
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


4. Изменение данных пользователя по username

Изменить данные пользователя по username.

Права доступа: Администратор.

Поля email и username должны быть уникальными.

Запрос:
```
PATCH /api/v1/users/{username}/
```
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


5. Удаление пользователя по username

Удалить пользователя по username.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/users/{username}/
```
