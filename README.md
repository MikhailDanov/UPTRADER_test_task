# Django Tree Menu

Реализация древовидного меню. Задание сделано в качестве тестового задания для компании UpTrader.

## Задача:
Сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, 
и нарисовать на любой нужной странице меню по названию. 
 
Пример: {% draw_menu 'main_menu' %}

## Стек

1. Python
2. Django

## Инструкция по запуску приложения:

1. Клонировать репозиторий и перейти в каталог проекта.
2. Собрать докер-контейнеры командой:
```
docker-compose up --build
```
2.5. Если происходит ошибка при запуске контейнера main-app, нужно остановить контейнеры
командой CTRL+C и заново запустить командой
```
docker-compose up
```
Это происходит из-за неправильного порядка запуска зависимых сервисов.
Исключение не критично, просто требует перезапуска.

3. Перейти по адресу http://127.0.0.1:8000/

Логин и пароль для суперюзера:
- admin
- 123
