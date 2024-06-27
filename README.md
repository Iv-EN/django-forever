<div align="center">
    <h1>django-forever</h1> 
    <p>
    Это учебный проект.
    </p>
</div>

---

## Описание

Этот проект настроен на работу с `PostgreSQL`.
База данных содержит две таблицы.
Данные можно заносить через панель администратора (пользователь `admin`, пароль `admin`)
А так же из файла `fixtures/catalog_data.json` при помощи команды 
```bash
python manage.py import_json
```

Отдаёт в браузер две статичные страницы:    
    - index - заготовка (шаблон) для главной страницы магазина;    
    - contacts - заготовка для контактной информации.    
Так же при заполнении формы на странице с контактами приложение получает внесенную пользователем информацию,
и сахраняет её в корне проекта в файле `сообщение_от_'введённое пользователем имя'.txt`

---

<div align="center">
    <h3 align="center">
        <p>Использовались языки и инструменты:</p>
        <div>
            <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
            <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
        </div>
        </div>
    </h3>
</div>

---

## Локальная установка проекта

1. Склонируйте репозиторий:
```bash
git clone https://github.com/Iv-EN/django-forever.git
```
2.  Создайте и активируйте виртуальное пространство:
```bash
python3 -m venv venv
```
```bash
sourse venv/bin/activate
```
3. Обновите pip и установите зависимости:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```


## Запуск проекта

2. Для запуска проекта из корня проекта выполните команду:
```bash
python3 manage.py runserver
```
___

<h3 align="center">
    <p><img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30" height="30" style="margin-right: 10px;">Автор: Евгений Иванов. </p>
</h3>
<p align="center">

 <div align="center"  class="icons-social" style="margin-left: 10px;">
        <a href="https://vk.com/engenivanov" target="blank" rel="noopener noreferrer">
      <img src="https://img.shields.io/badge/%D0%92%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5-blue?style=for-the-badge&logo=VK&logoColor=white" alt="В контакте Badge"/>
    </a>
    <a href="https://t.me/IvENauto" target="blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
    </a>
  </div>
</p>