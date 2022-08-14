# ������: api_yamdb

������:
- matsabaleuski
- Innis8
- Serge561

# ��������

������ YaMDb, � ����� REST API ������ ��� ����.
���������� ���������:
- ��������� ����� ������������ � ���� ������. 
- ����������� ������������� ��������� � ����� � ������������� ��.
- ��������� ������ � ������������.
- ��������� ����������� � �������.

����� �������� �������� ������ ����� ����������� �� JWT-������.

# ��� ��������� ������:

����������� ����������� � ������� � ���� � ��������� ������:

```
git clone https://github.com/Innis8/api_yamdb.git
```

```
cd api_yamdb
```

C������ � ������������ ����������� ���������:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

���������� ����������� �� ����� requirements.txt:

```
pip install -r requirements.txt
```

��������� ��������:

```
python manage.py migrate
```

��������� ������:

```
python manage.py runserver
```

# ��� ������������ �����������:



# ������ AUTH

����������� ������������� � ������ �������

1. ����������� ������ ������������

�������� ��� ������������� �� ���������� email.

����� �������: �������� ��� ������.

������������ ��� 'me' � �������� username ���������.

���� email � username ������ ���� �����������.

������:
```
 POST /api/v1/auth/signup/
```
```
{
  "email": "string",
  "username": "string"
}
```

�����:
```
{
  "email": "string",
  "username": "string"
}
```


2. ��������� JWT-������

��������� JWT-������ � ����� �� username � confirmation code.

����� �������: �������� ��� ������.

������:
```
POST /api/v1/auth/token/
```
```
{
  "username": "string",
  "confirmation_code": "string"
}
```

�����:
```
{
  "token": "string"
}
```


# ������ CATEGORIES

��������� (����) ������������

1. ��������� ������ ���� ���������

�������� ������ ���� ���������

����� �������: �������� ��� ������

������:
```
 GET /api/v1/categories/
```

�����:
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


2. ���������� ����� ���������

������� ���������.

����� �������: �������������.

���� slug ������ ��������� ������ ���� ����������.

������:
```
POST /api/v1/categories/
```
```
{
  "name": "string",
  "slug": "string"
}
```

�����:
```
{
  "name": "string",
  "slug": "string"
}
```


3. �������� ���������

������� ���������.

����� �������: �������������.

������:
```
 DELETE /api/v1/categories/{slug}/
```


# ������ GENRES

��������� ������

1. ��������� ������ ���� ������

�������� ������ ���� ������.

����� �������: �������� ��� ������

������:
```
 GET /api/v1/genres/
```

�����:
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


2. ���������� �����

�������� ����.

����� �������: �������������.

���� slug ������� ����� ������ ���� ����������.

������:
```
POST /api/v1/genres/
```
```
{
  "name": "string",
  "slug": "string"
}
```

�����:
```
{
  "name": "string",
  "slug": "string"
}
```


3. �������� �����

������� ����.

����� �������: �������������.

������:
```
 DELETE /api/v1/genres/{slug}/
```


# ������ TITLES

������������, � ������� ����� ������ (����������� �����, ����� ��� �������).

1. ��������� ������ ���� ������������

�������� ������ ���� ��������.

����� �������: �������� ��� ������

������:
```
 GET /api/v1/titles/
```

�����:
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


2. ���������� ������������

�������� ����� ������������.

����� �������: �������������.

������ ��������� ������������, ������� ��� �� ����� (��� ������� �� ����� ���� ������ ��������).

��� ���������� ������ ������������ ��������� ������� ��� ������������ ��������� � ����.

������:
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

�����:
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


3. ��������� ���������� � ������������

���������� � ������������

����� �������: �������� ��� ������

������:
```
 GET /api/v1/titles/{titles_id}/
```

�����:
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


4. ��������� ���������� ���������� � ������������

�������� ���������� � ������������

����� �������: �������������

������:
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

�����:
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


5. �������� ������������

������� ������������.

����� �������: �������������.

������:
```
 DELETE /api/v1/titles/{titles_id}/
```



# ������ REVIEWS

������

1. ��������� ������ ���� �������

�������� ������ ���� �������.

����� �������: �������� ��� ������.

������:
```
 GET /api/v1/titles/{title_id}/reviews/
```

�����:
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


2. ���������� ������ ������

�������� ����� �����. ������������ ����� �������� ������ ���� ����� �� ������������.

����� �������: ������������������� ������������.

������:
```
 POST /api/v1/titles/{title_id}/reviews/
```
```
{
  "text": "string",
  "score": 1
}
```

�����:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


3. �������� ������ �� id

�������� ����� �� id ��� ���������� ������������.

����� �������: �������� ��� ������.

������:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/
```

�����:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


4. ��������� ���������� ������ �� id

�������� �������� ����� �� id.

����� �������: ����� ������, ��������� ��� �������������.

������:
```
PATCH /api/v1/titles/{title_id}/reviews/{review_id}/
```
```
{
  "text": "string",
  "score": 1
}
```

�����:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


5. �������� ������ �� id

������� ����� �� id

����� �������: ����� ������, ��������� ��� �������������.

������:
```
 DELETE /api/v1/titles/{title_id}/reviews/{review_id}/
```


# ������ COMMENTS

����������� � �������

1. ��������� ������ ���� ������������ � ������

�������� ������ ���� ������������ � ������ �� id

����� �������: �������� ��� ������.

������:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

�����:
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


2. ���������� ����������� � ������

�������� ����� ����������� ��� ������.

����� �������: ������������������� ������������.

������:
```
 POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
```
{
  "text": "string"
}
```

�����:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


3. ��������� ����������� � ������

�������� ����������� ��� ������ �� id.

����� �������: �������� ��� ������.

������:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

�����:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


4. ��������� ���������� ����������� � ������

�������� �������� ����������� � ������ �� id.

����� �������: ����� �����������, ��������� ��� �������������.

������:
```
PATCH /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
```
{
  "text": "string"
}
```

�����:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


5. �������� ����������� � ������

������� ����������� � ������ �� id.

����� �������: ����� �����������, ��������� ��� �������������.

������:
```
 DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```



# ������ USERS

������������

1. ��������� ������ ���� �������������

�������� ������ ���� �������������.

����� �������: �������������

������:
```
 GET /api/v1/users/
```

�����:
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


2. ���������� ������������

�������� ������ ������������.

����� �������: �������������

���� email � username ������ ���� �����������.

������:
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

�����:
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


3. ��������� ������������ �� username

�������� ������������ �� username.

����� �������: �������������

������:
```
 GET /api/v1/users/{username}/
```

�����:
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


4. ��������� ������ ������������ �� username

�������� ������ ������������ �� username.

����� �������: �������������.

���� email � username ������ ���� �����������.

������:
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

�����:
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


5. �������� ������������ �� username

������� ������������ �� username.

����� �������: �������������.

������:
```
 DELETE /api/v1/users/{username}/
```
