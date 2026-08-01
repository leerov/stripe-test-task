# stripe-test-task

## Онлайн демо
- Ссылка на приложение: [https://stripe-test-task.osfb.dev/](https://stripe-test-task.osfb.dev/)
- Админ-панель: [https://stripe-test-task.osfb.dev/admin/](https://stripe-test-task.osfb.dev/admin/)
- Логин: `admin`
- Пароль: `admin`

## Запуск локально
1. Скопируйте `.env.example` в `.env` и заполните своими ключами Stripe.
2. Запустите контейнеры: `make up`
3. Примените миграции: `make docker-migrate`
4. Создайте суперпользователя: `make docker-createsuperuser`
5. Откройте http://localhost:8080

## Деплой на Render.com
1. Создайте новый **Web Service** на Render, подключив этот GitHub репозиторий.
2. Укажите следующие настройки:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `python manage.py migrate && python manage.py create_default_superuser && gunicorn stripe_test_task.wsgi:application`
3. Добавьте переменные окружения (Environment Variables):
   - `SECRET_KEY`: (сгенерируйте надежный ключ)
   - `DEBUG`: `False`
   - `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_PUBLIC_KEY_EUR`, `STRIPE_SECRET_KEY_EUR`: ваши ключи Stripe
   - `DOMAIN`: `https://<имя-вашего-приложения>.onrender.com`
4. (Рекомендуется) Создайте бесплатную базу данных **PostgreSQL** на Render и добавьте её `Internal Database URL` в переменные окружения как `DATABASE_URL`.
5. Нажмите **Create Web Service**.

> **Важно:** Ошибка 500 при входе в админку возникает из-за того, что не были применены миграции к новой базе данных. Убедитесь, что **Start Command** в настройках Render точно соответствует указанному выше (он запускает `migrate` перед стартом gunicorn).

## Примечание по тестированию
При создании товара (Item) в админ-панели убедитесь, что цена (`price`) составляет не менее **50** (что соответствует $0.50 USD или €0.50 EUR), так как Stripe API требует минимальную сумму платежа $0.50 для успешного создания Checkout Session.

# здесь был леня
