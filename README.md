# Severstal тестовое задание
Backend для работы со складом рулонов металла

Реализован только 1 пункт - a, b, c.
Будет обновляться по мере возможностей.

Задание 2
Тебе необходимо создать backend для работы со складом рулонов металла. Это
задание нужно выполнить на Python. Рулон: id, длина, вес, дата добавления, дата удаления.
Обязательные пункты:
1. RESTFull API:
a. добавление нового рулона на склад. Длина и вес — обязательные
параметры. В случае успеха возвращает добавленный рулон;
b. удаление рулона с указанным id со склада. В случае успеха возвращает
удалённый рулон;
c. получение списка рулонов со склада. Рассмотреть возможность
фильтрации по одному из диапазонов единовременно (id/веса/длины/даты
добавления/даты удаления со склада);
d. получение статистики по рулонам за определённый период:
- количество добавленных рулонов;
- количество удалённых рулонов;
- средняя длина, вес рулонов, находившихся на складе в этот период;
- максимальная и минимальная длина и вес рулонов, находившихся на
складе в этот период;
- суммарный вес рулонов на складе за период;
- максимальный и минимальный промежуток между добавлением и
удалением рулона.
2. Данные по рулонам должны храниться в базе данных (желательно
PostgreSQL/SQLite).
3. Должны быть обработаны стандартные кейсы ошибок (например, недоступна
БД, не существует рулон при какой-то работе с ним).
4. Используемый стек: FastAPI, SQLAlchemy, pydantic (версии и до 2.0, и после 2.0
подойдут).

Бонусные баллы:
1. Получение списка рулонов с фильтрацией (п.1, с.) работает по комбинации
нескольких диапазонов сразу.
2. Получение статистики по рулонам (п.1, d.) дополнительно возвращает:
- день, когда на складе находилось минимальное и максимальное
количество рулонов за указанный период;
- день, когда суммарный вес рулонов на складе был минимальным и
максимальным в указанный период.
3. Проект должен быть обёрнут в Docker.
4. Конфигурации к подключению к БД должны быть настраиваемыми через файл
или ENV.
5. Проект должен быть покрыт тестами.
6. Проект должен проходить mypy, flake8 и прочее.
7. Отсутствие глобальных переменных.
  
Идеи для улучшения:
1. Использование абстракций/интерфейсов для возможной замены транспорта.
Например, с PostgreSQL на какое-нибудь хранилище (InMemory / Redis / File).
2. Тесты не должны зависеть от реальной базы данных (т.е. использовать класс,
фальшивку или моки).
Нам очень интересно посмотреть, как ты программируешь. Если что-то не удалось
реализовать — мы смотрим образ мышления, а не конечный результат.


