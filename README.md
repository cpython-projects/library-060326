# Books

## Запуск на локальной машине

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
source .venv/bin/activate         # macOS / Linux

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Тестовые данные

```bash
python manage.py seed_library          # добавить данные
python manage.py seed_library --clear  # удалить старые данные и заполнить заново
```

## Запуск сервера

```bash
python manage.py runserver
```
