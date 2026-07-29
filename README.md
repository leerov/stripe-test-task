# stripe-test-task

## Онлайн демо
- Ссылка на приложение: [http://your-domain.com](http://your-domain.com)
- Админ-панель: [http://your-domain.com/admin](http://your-domain.com/admin)
- Логин: `admin`
- Пароль: `your_admin_password`

## Запуск локально
1. Скопируйте `.env.example` в `.env` и заполните своими ключами Stripe.
2. Запустите контейнеры: `make up`
3. Примените миграции: `make docker-migrate`
4. Создайте суперпользователя: `make docker-createsuperuser`
5. Откройте http://localhost:8080## Примечание по тестированию
При создании товара (Item) в админ-панели убедитесь, что цена (`price`) составляет не менее **50** (что соответствует $0.50 USD или €0.50 EUR), так как Stripe API требует минимальную сумму платежа $0.50 для успешного создания Checkout Session.
