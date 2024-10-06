# 🛠️ API Управления Пользователями


## 🚀Пользователи - APIs

- Регистрация пользователей с подтверждением по электронной почте
- Аутентификация пользователей по электронной почте и паролю
- Сброс пароля с отправкой кода на email
- Управление профилем пользователя


### Базовый URL:
```bash
/api/v1/
```


### Основные конечные точки:

- **POST:** `/api/v1/users/registration/`
- **POST:** `/api/v1/email-confirmation/`
- **POST:** `/api/v1/users/login/`
- **GET:** `/api/v1/profile/`
- **POST:** `/api/v1/users/logout/`
- **POST:** `/api/v1/password-reset-request/`
- **POST:** `/api/v1/password-reset/`
- **GET:** `/api/v1/users/`
- **GET:** `/api/v1/users/<pk>/`
- **PUT:** `/api/v1/users/<pk>/`
- **DELETE:** `/api/v1/users/<pk>/`




####  Регистрация пользователя
- **Метод:** POST
- **URL:** `/api/v1/users/registration/`
- **Описание:** Регистрирует нового пользователя и отправляет письмо для подтверждения электронной почты.

##### Пример запроса
```json
{
  "email": "user@example.com",
  "password": "secure_password",
  "first_name": "Имя",
  "last_name": "Фамилия"
}
```
Успех:
```json
{
    "message": "Пользователь создан успешно. Пожалуйста, подтвердите ваш email."
}
```
Ошибка:
```json
{
    "email": "Пользователь с таким email уже существует."
}
```

####  Подтверждение электронной почты 
- **Метод:** POST
- **URL:** `/api/v1/confirm-email/`
- **Описание:** Подтверждает электронную почту с помощью кода.

##### Пример запроса
```json
{
  "email": "admin@admin.com",
  "confirmation_code": "1234"
}
```
Успех:
```json
{
  "message": "Электронная почта успешно подтверждена. Теперь вы можете войти в систему."
}
```
Ошибка:
```json
{
    "email": [
        "Пользователь с таким email уже существует."
    ]
}
```
####  Вход пользователя
- **Метод:** POST
- **URL:** `/api/v1/users/login/`
- **Описание:** Позволяет пользователю войти в систему, используя свой адрес электронной почты и пароль.

##### Пример запроса
```json
{
  "email": "admin@admin.com",
  "password": "admin"
}
```
Успех:
```json
{
    "token": "1c9be8f8af4e449bde51737095bb5a1e9d201526"
}
```
Ошибка:
```json
{
    "error": "Неверные учетные данные"
}
```
####  Профиль пользователя
- **Метод:** GET
- **URL:** `/api/v1/users/profile/`
- **Описание:**  Этот запрос возвращает информацию о текущем аутентифицированном пользователе.

##### Заголовки
```bash
Authorization: Token your_token_here
```
Успех:
```json
{
    "id": 29,
    "first_name": "Saikal",
    "last_name": "Ulukbekova",
    "email": "saykal.ask@yahoo.com",
    "organization_name": "",
    "legal_address": "",
    "physical_address": "",
    "phone_number": ""
}
```
####  Выход пользователя
- **Метод:** POST
- **URL:** `/api/v1/users/logout/`
- **Описание:** Этот запрос завершает сессию пользователя.
```bash
Authorization: Token your_token_here
```
####  Отправляет код сброса пароля на адрес электронной почты
- **Метод:** POST
- **URL:** `/api/v1/password-reset-request/`
- **Описание:** Этот запрос отправляет код сброса пароля на адрес электронной почты пользователя.

##### Пример запроса
```json
{
  "email": "saykal.ask@yahoo.com"
}
```
```bash
Authorization: Token your_token_here
```
Успех:
```json
{
    "message": "Код сброса пароля отправлен на ваш email."
}
```
Ошибка:
```json
{
    "non_field_errors": [
        "Пользователь с таким адресом электронной почты не найден."
    ]
}
```

####  Изменения пароля
- **Метод:** POST
- **URL:** `/api/v1/password-reset/`
- **Описание:** Этот запрос позволяет пользователю изменить пароль, используя новый пароль и код подтверждения.
##### Пример запроса
```json
{
    "email": "saykal.ask@yahoo.com",
    "new_password": "saikal20022024",
    "reset_code": "3672",
    "confirm_password": "saikal20022024"
}
```
```bash
Authorization: Token your_token_here
```
Успех:
```json
{
    "message": "Пароль успешно изменен."
}
```
Ошибки:
```json
{
    "non_field_errors": [
        "Пароли не совпадают."
    ]
}
```
```json
{
    "non_field_errors": [
        "Неверный адрес электронной почты или код сброса."
    ]
}
```

####  Список всех пользователей
- **Метод:** GET
- **URL:** `/api/v1/users/`
- **Описание:** Этот запрос возвращает список всех пользователей.
```json
[
    {
        "id": 2,
        "first_name": "Alina",
        "last_name": "Alin",
        "email": "asdasd@gmail.com",
        "organization_name": null,
        "legal_address": null,
        "physical_address": null,
        "phone_number": null
    },
    {
        "id": 4,
        "first_name": "Sara",
        "last_name": "Luca",
        "email": "sara@gmail.com",
        "organization_name": null,
        "legal_address": null,
        "physical_address": null,
        "phone_number": null
    },
    {
        "id": 1,
        "first_name": "admin",
        "last_name": "",
        "email": "admin@admin.com",
        "organization_name": null,
        "legal_address": null,
        "physical_address": null,
        "phone_number": null
    },
    {
        "id": 29,
        "first_name": "Saikal",
        "last_name": "Ulukbekova",
        "email": "saykal.ask@yahoo.com",
        "organization_name": "",
        "legal_address": "",
        "physical_address": "",
        "phone_number": ""
    }
]
```
####  Информация о пользователе
- **Метод:** GET
- **URL:** `/api/v1/users/<pk>/`
- **Описание:** Этот запрос возвращает информацию о текущем аутентифицированном пользователе.
##### Заголовки
```bash
Authorization: Token your_token_here
```


####  Обновление информации о конкретном пользователе
- **Метод:** PUT
- **URL:** `/api/v1/users/<pk>/`
- **Описание:** Позволяет обновить информацию о пользователе.
##### Заголовки
```bash
Authorization: Token your_token_here
```
##### Пример запроса
```json
{
  "first_name": "Admin"
}
```
Успех:
```json
{
    "message": "Пользователь успешно обновлен"
}
```
####  Удаление конкретного пользователя
- **Метод:** DELETE
- **URL:** `/api/v1/users/<pk>/`
- **Описание:** Этот запрос удаляет конкретного пользователя по его ID.

##### Заголовки
```bash
Authorization: Token your_token_here
```
Успех:
```json
{
    "message": "Пользователь успешно обновлен"
}
```
## 🚀Категории,продукты  - APIs
- Управление категориями
- Управление производителями
- Управление продуктами
- Создание запросов на цены

### Базовый URL:
```bash
/api/v1/catalog/
```


### Основные конечные точки:

- **GET:** `/api/v1/catalog/categories/`
- **POST:** `/api/v1/catalog/categories/`
- **GET:** `/api/v1/catalog/categories/<pk>/`
- **PUT:** `/api/v1/catalog/categories/<pk>/`
- **DELETE:** `/api/v1/catalog/categories/<pk>/`
- **GET:** `/api/v1/catalog/manufacturers/`
- **POST:** `/api/v1/catalog/manufacturers/`
- **GET:** `/api/v1/catalog/manufacturers/<pk>/`
- **PUT:** `/api/v1/catalog/manufacturers/<pk>/`
- **DELETE:** `/api/v1/catalog/manufacturers/<pk>/`
- **GET:** `/api/v1/catalog/products/`
- **POST:** `/api/v1/catalog/products/`
- **GET:** `/api/v1/catalog/products/<pk>/`
- **PUT:** `/api/v1/catalog/products/<pk>/`
- **DELETE:** `/api/v1/catalog/products/<pk>/`
- **GET:** `/api/v1/catalog/prices/`
- **POST:** `/api/v1/catalog/prices/`
- **GET:** `/api/v1/catalog/prices/<pk>/`
- **PUT:** `/api/v1/catalog/prices/<pk>/`
- **DELETE:** `/api/v1/catalog/prices/<pk>/`


#### Получить все категории
- **Метод:** GET
- **URL:** `/api/v1/catalog/categories/`
- **Описание:** Возвращает список всех категорий.
##### Пример запроса
Успех:
```json
[
    {
        "id": 1,
        "name": "Антибиотики",
        "slug": "antibiotiki"
    }
]
```
####  Создать категорию
- **Метод:** POST
- **URL:** `/api/v1/catalog/categories/`
- **Описание:** Создает новую категорию.

##### Пример запроса
```json
{
  "name": "Product2"
}
```
Успех:
```json
{
    "id": 5,
    "name": "Product2",
    "slug": "product2"
}
```
Ошибка:
```json
{
    "name": [
        "Обязательное поле."
    ]
}
```

####  Получить информацию о конкретной категории
- **Метод:** GET
- **URL:** `/api/v1/catalog/categories/<pk>/`
- **Описание:** Возвращает информацию о конкретной категории.

##### Пример запроса
Успех:
```json
{
    "id": 5,
    "name": "Product2",
    "slug": "product2"
}
```

####  Обновить категорию
- **Метод:** PUT
- **URL:** `/api/v1/catalog/categories/<pk>/`
- **Описание:** Обновляет данные категории.

##### Пример запроса
```json
{
    "name": "Product_3"
}
```
Успех:
```json
{
    "id": 7,
    "name": "Product_3",
    "slug": "product3"
}
```
Ошибка:
```json
{
    "name": [
        "Обязательное поле."
    ]
}
```
####  Удалить категорию
- **Метод:** DELETE
- **URL:** `/api/v1/catalog/categories/<pk>/`
- **Описание:** Удаляет категорию.

##### Пример запроса
Успех:
```json
{
    "message": "Категория была удалена."
}
```
####  Cписок всех производителей
- **Метод:** GET
- **URL:** `/api/v1/catalog/manufacturers/`
- **Описание:** Получить список всех производителей.
Успех:
```json
[
    {
        "id": 1,
        "name": "Италия",
        "slug": "italiya"
    }
]
```

####  Создать нового производителя.
- **Метод:** POST
- **URL:** `/api/v1/catalog/manufacturers/`
- **Описание:** Создать нового производителя.

##### Пример запроса
```json
{
  "name": "Россия"
}
```
Успех:
```json
{
    "id": 2,
    "name": "Россия",
    "slug": ""
}
```
Ошибка:
```json
{
    "name": [
        "Обязательное поле."
    ]
}
```

####  Получить информацию o производителe.
- **Метод:** GET
- **URL:** `/api/v1/catalog/manufacturers/<pk>/`
- **Описание:** Получить информацию о конкретном производителе по его ID.

Успех:
```json
{
    "id": 1,
    "name": "Италия",
    "slug": "italiya"
}
```

####  Обновить существующего производителя
- **Метод:** PUT
- **URL:** `/api/v1/catalog/manufacturers/<pk>/`
- **Описание:** Обновить существующего производителя по его ID.

##### Пример запроса
```json
{
  "name": "россия"
}
```
Успех:
```json
{
    "id": 2,
    "name": "россия",
    "slug": ""
}
```
####  Удалить производителя
- **Метод:** DELETE
- **URL:** `/api/v1/catalog/manufacturers/<pk>/`
- **Описание:** Удалить производителя по его ID.

##### Пример запроса
Успех:
```json
{
    "message": "Производитель был удален."
}
```


####  Получить все продукты
- **Метод:** GET
- **URL:** `/api/v1/catalog/products/`
- **Описание:** Возвращает список всех продуктов.


Успех:
```json
[
    {
        "id": 3,
        "name": "New Product",
        "description": "This is a test product",
        "article": "123",
        "stock_quantity": 100,
        "image": null,
        "slug": "new-product",
        "category": 1,
        "manufacturer": 1
    },
    {
        "id": 2,
        "name": "SENSISpec ELISA Almond 96 лунок",
        "description": "Automated machine for testing",
        "article": "ABC12345",
        "stock_quantity": 10,
        "image": null,
        "slug": "sensispec-elisa-almond",
        "category": 1,
        "manufacturer": 1
    },
    {
        "id": 1,
        "name": "SENSISpec ELISA Алмонд 96 лунок",
        "description": "Description",
        "article": "1111111111",
        "stock_quantity": 10,
        "image": "http://localhost:8000/media/products/18BF04EA-F2A0-439A-A247-196769F2F53E.JPEG",
        "slug": "sensispec-elisa-almond-96-lunok",
        "category": 1,
        "manufacturer": 1
    }
]
```
####  Создать продукт
- **Метод:** POST
- **URL:** `/api/v1/catalog/products/`
- **Описание:** Создает новый продукт.

##### Пример запроса
```json
{
  "name": "PRODUCT1",
  "category": 1,
  "manufacturer": 1,
  "article": "188888",
  "stock_quantity": 10
}

```
Успех:
```json
{
    "id": 4,
    "name": "PRODUCT1",
    "description": null,
    "article": "188888",
    "stock_quantity": 10,
    "image": null,
    "slug": "product1",
    "category": 1,
    "manufacturer": 1
}
```
Ошибка:
```json
{
    "article": [
        "Продукт с таким Артикул уже существует."
    ]
}
```
####  Получить продукт
- **Метод:** GET
- **URL:** `/api/v1/catalog/products/<pk>/`
- **Описание:** Получить продукт по id.

Успех:
```json
{
    "id": 4,
    "name": "PRODUCT1",
    "description": null,
    "article": "188888",
    "stock_quantity": 10,
    "image": null,
    "slug": "product1",
    "category": 1,
    "manufacturer": 1
}
```
####  Обновить продукт
- **Метод:** PUT
- **URL:** `/api/v1/catalog/products/<pk>/`
- **Описание:** Обновить продукт по id.

##### Пример запроса
```json
{
  "name": "PRODUCT4",
  "category": 1,
  "manufacturer": 1,
  "article": "188888",
  "stock_quantity": 10
}

```
Успех:
```json
{
    "id": 4,
    "name": "PRODUCT4",
    "description": null,
    "article": "188888",
    "stock_quantity": 10,
    "image": null,
    "slug": "product1",
    "category": 1,
    "manufacturer": 1
}
```

####  Удалить продукт.
- **Метод:** DELETE
- **URL:** `/api/v1/catalog/prices/<pk>/`
- **Описание:** Удалить продукт по идентификатору.

Успех:
```json
{
    "message": "Продукт был удален."
}
```
####  Cписок цен
- **Метод:** GET
- **URL:** `/api/v1/catalog/prices/`
- **Описание:** Получить список всех цен.

Успех:
```json
[
    {
        "id": 1,
        "name": "Saikal",
        "surname": "Ulukbekova",
        "phone_number": "+996700123456",
        "email": "saykal.ask@yahoo.com",
        "comments": "Хочу узнать цену",
        "request_file": null,
        "slug": "saikal-sensispec-elisa-96",
        "product": 1
    }
]
```
####  Создать цену.
- **Метод:** POST
- **URL:** `/api/v1/catalog/prices/`
- **Описание:** Создать новую цену.

##### Пример запроса
```json
{
        "name": "Ben",
        "surname": "Tims",
        "phone_number": "+999999999",
        "email": "saykal.ask@yahoo.com",
        "product": 1
}
```
Успех:
```json
{
    "id": 3,
    "name": "Ben",
    "surname": "Tims",
    "phone_number": "+999999999",
    "email": "saykal.ask@yahoo.com",
    "comments": null,
    "request_file": null,
    "slug": "ben-sensispec-elisa-96",
    "product": 1
}
```
Ошибка:
```json
{
    "surname": [
        "Обязательное поле."
    ]
}
```

####  Получить цену.
- **Метод:** GET
- **URL:** `/api/v1/catalog/prices/<pk>/`
- **Описание:** Получить цену по id.

Успех:
```json
{
    "id": 1,
    "name": "Saikal",
    "surname": "Ulukbekova",
    "phone_number": "+996700123456",
    "email": "saykal.ask@yahoo.com",
    "comments": "Хочу узнать цену",
    "request_file": null,
    "slug": "saikal-sensispec-elisa-96",
    "product": 1
}
```

####  Обновить цену.
- **Метод:** PUT
- **URL:** `/api/v1/catalog/prices/<pk>/`
- **Описание:** Обновить цену по id.

##### Пример запроса
```json
{
        "name": "BBen",
        "surname": "Tims",
        "phone_number": "+999999999",
        "email": "saykal.ask@yahoo.com",
        "product": 1
    }
```
Успех:
```json
{
    "id": 1,
    "name": "BBen",
    "surname": "Tims",
    "phone_number": "+999999999",
    "email": "saykal.ask@yahoo.com",
    "comments": "Хочу узнать цену",
    "request_file": null,
    "slug": "saikal-sensispec-elisa-96",
    "product": 1
}
```

####  Удалить цену.
- **Метод:** DELETE
- **URL:** `/api/v1/catalog/prices/<pk>/`
- **Описание:** Удалить цену по id.


Успех:
```json
{
    "message": "Цена была удалена."
}
```

## 🚀Корзина - APIs
- Управление корзинами пользователей

### Базовый URL:
```bash
/api/v1/carts/
```
### Основные конечные точки:

- **GET:** `/api/v1/carts/`
- **POST:** `/api/v1/carts/`
- **GET:** `/api/v1/carts/<pk>/`
- **PUT:** `/api/v1/carts/<pk>/`
- **DELETE:** `/api/v1/carts/<pk>/`

####  Список всех корзин.
- **Метод:** GET
- **URL:** `/api/v1/carts/`
- **Описание:** Получить список всех корзин.

Успех:
```json
[
    {
        "id": 1,
        "product_name": "SENSISpec ELISA Алмонд 96 лунок",
        "quantity": 4,
        "status": "pending"
    },
    {
        "id": 2,
        "product_name": "SENSISpec ELISA Алмонд 96 лунок",
        "quantity": 3,
        "status": "pending"
    }
]
```

####  Создать корзину.
- **Метод:** POST
- **URL:** `/api/v1/catalog/carts/`
- **Описание:** Создать новую корзину.

##### Пример запроса
```json
{
    "product_id": 4,
    "quantity": 1,
    "status": "pending"
}
```
Успех:
```json
{
    "id": 3,
    "product_name": "PRODUCT1",
    "quantity": 10,
    "status": "pending"
}
```


####  Получить корзину по id.
- **Метод:** GET
- **URL:** `/api/v1/carts/<pk>/`
- **Описание:** Получить корзину по id.


Успех:
```json
{
    "id": 1,
    "product_name": "SENSISpec ELISA Алмонд 96 лунок",
    "quantity": 4,
    "status": "pending"
}
```
Ошибка:
```json
{
    "detail": "No Cart matches the given query."
}
```

####  Обновить корзину.
- **Метод:** PUT
- **URL:** `/api/v1/carts/<pk>/`
- **Описание:** Обновить корзину по id.

##### Пример запроса
```json
{
    "id": 1,
    "product_name": "SENSISpec ELISA Алмонд 96 лунок",
    "quantity": 5,
    "status": "pending"
}
```
Успех:
```json
{
    "id": 1,
    "product_name": "SENSISpec ELISA Алмонд 96 лунок",
    "quantity": 5,
    "status": "pending"
}
```
Ошибка:
```json
{
    "detail": "No Cart matches the given query."
}
```
####  Удалить корзину.
- **Метод:** DELETE
- **URL:** `/api/v1/carts/<pk>/`
- **Описание:** Удалить корзину по id.


Успех:
```json
{
    "message": "Элемент корзины был удален."
}
```
Ошибка:
```json
{
    "detail": "No Cart matches the given query."
}
```


## 🚀Избранные - APIs

### Базовый URL:
```bash
/api/v1/favorites/
```
### Основные конечные точки:

- **GET:** `/api/v1/favorites/`
- **POST:** `/api/v1/favorites/add/`
- **POST:** `/api/v1/favorites/remove/`



####  Получить список всех избранных товаров.
- **Метод:** GET
- **URL:** `/api/v1/favorites/`
- **Описание:** Получить список всех избранных товаров текущего пользователя.


Успех:
```json
[
    {
        "id": 3,
        "product": {
            "id": 3,
            "name": "New Product",
            "description": "This is a test product",
            "article": "123",
            "stock_quantity": 100,
            "image": null,
            "slug": "new-product",
            "category": 1,
            "manufacturer": 1
        }
    },
    {
        "id": 4,
        "product": {
            "id": 1,
            "name": "SENSISpec ELISA Алмонд 96 лунок",
            "description": "Description",
            "article": "1111111111",
            "stock_quantity": 10,
            "image": "http://localhost:8000/media/products/18BF04EA-F2A0-439A-A247-196769F2F53E.JPEG",
            "slug": "sensispec-elisa-almond-96-lunok",
            "category": 1,
            "manufacturer": 1
        }
    }
]
```
####  Добавить продукт в избранное.
- **Метод:** POST
- **URL:** `/api/v1/favorites/add/`
- **Описание:** Добавить продукт в избранное.

##### Пример запроса
```json
{
    "product_id": 3
}

```
Успех:
```json
{
    "message": "Продукт добавлен в избранное"
}
```
```json
{
    "message": "Продукт уже в избранном"
}
```
####  Удалить продукт в избранном.
- **Метод:** POST
- **URL:** `/api/v1/favorites/remove/`
- **Описание:** Удалить продукт в избранномю

##### Пример запроса
```json
{
    "product_id": 3
}
```
Успех:
```json
{
    "message": "Продукт удален из избранного"
}
```

```json
{
    "error": "Продукт не найден в избранном"
}
```

####  APIs
- **POST:** `/api/v1/users/registration/`
- **POST:** `/api/v1/email-confirmation/`
- **POST:** `/api/v1/users/login/`
- **GET:** `/api/v1/profile/`
- **POST:** `/api/v1/users/logout/`
- **POST:** `/api/v1/password-reset-request/`
- **POST:** `/api/v1/password-reset/`
- **GET:** `/api/v1/users/`
- **GET:** `/api/v1/users/<pk>/`
- **PUT:** `/api/v1/users/<pk>/`
- **DELETE:** `/api/v1/users/<pk>/`
- **GET:** `/api/v1/catalog/categories/`
- **POST:** `/api/v1/catalog/categories/`
- **GET:** `/api/v1/catalog/categories/<pk>/`
- **PUT:** `/api/v1/catalog/categories/<pk>/`
- **DELETE:** `/api/v1/catalog/categories/<pk>/`
- **GET:** `/api/v1/catalog/manufacturers/`
- **POST:** `/api/v1/catalog/manufacturers/`
- **GET:** `/api/v1/catalog/manufacturers/<pk>/`
- **PUT:** `/api/v1/catalog/manufacturers/<pk>/`
- **DELETE:** `/api/v1/catalog/manufacturers/<pk>/`
- **GET:** `/api/v1/catalog/products/`
- **POST:** `/api/v1/catalog/products/`
- **GET:** `/api/v1/catalog/products/<pk>/`
- **PUT:** `/api/v1/catalog/products/<pk>/`
- **DELETE:** `/api/v1/catalog/products/<pk>/`
- **GET:** `/api/v1/catalog/prices/`
- **POST:** `/api/v1/catalog/prices/`
- **GET:** `/api/v1/catalog/prices/<pk>/`
- **PUT:** `/api/v1/catalog/prices/<pk>/`
- **DELETE:** `/api/v1/catalog/prices/<pk>/`
- **GET:** `/api/v1/carts/`
- **POST:** `/api/v1/carts/`
- **GET:** `/api/v1/carts/<pk>/`
- **PUT:** `/api/v1/carts/<pk>/`
- **DELETE:** `/api/v1/carts/<pk>/`
- **GET:** `/api/v1/favorites/`
- **POST:** `/api/v1/favorites/add/`
- **POST:** `/api/v1/favorites/remove/`

