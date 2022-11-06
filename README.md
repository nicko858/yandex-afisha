# Аналог Яндекс.Афиши

Сайт-блог об интересных местах, которые можно посетить в Москве

![image](https://user-images.githubusercontent.com/35272808/200195508-a09b4822-4f5d-4f6f-bd26-5922d23b26de.png)


## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).

В частности, репозиторий используется:

- В задаче "Оптимизируем сайт" модуля [Знакомство с Django: ORM](https://dvmn.org/modules/django-orm/).
- В туториале [Превью для ImageField в админке](https://devman.org/encyclopedia/django/how-to-setup-image-preview/)
