
### Описание

Сервис, который получает данные контакта (ID, Имя) из Битрикс24 по Webhook, проверяет имя контакта на наличие его в БД (PostgreSQL).
Далее, если нашлось имя в БД, передаем данные по гендеру обратно в контакт по ID.

Код программы, обновляющей гендер, находится в файле 
/bitrix_task/bitrix_webhook_handler/bitrix_webhook_handler/update_gender.py

### Стек

- Flask
- psycopg2
- alembic
- unittest

### Тесты

В тестах симмитирован http запрос, отработано два позитивных сценария с мужским и женским именем и один негативный сценарий, когда имени в обеих таблицах БД нет.

### Запуск
 
 Установка зависимостей
 ```
 pip install -r requirements.txt
 ```
 Миграция базы данных
  ```
  python3 migrate.py
   ```
   Запуск тестов
   ```
   python3 -m pytest
   ```
   Откат миграции
   ```
   alembic downgrade -1
   ```
   или
   ```
   alembic -c /path/to/your/alembic.ini downgrade -1
   ```