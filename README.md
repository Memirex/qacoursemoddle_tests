[![Build Status](https://app.travis-ci.com/Memirex/qacoursemoddle_tests.svg?branch=testing_required_fields)](https://app.travis-ci.com/github/Memirex/qacoursemoddle_tests/)

# Тесты для приложения "Курсы"
### Установка

- Создайте отдельную директорию на локальном компьютере
- Скачайте все файлы которые расположены в директории: <br>
  git clone https://github.com/Memirex/qacoursemoddle_tests
- Откройте проект
- Установите все пакеты, которые указаны в файле requirements.txt: <br>
  pip install -r /path/to/requirements.txt

## Описание проекта

### Тест проверки формы авторизации

Позитивная проверка:

- проверка на то что мы можем авторизоваться в системе с валидным логином и паролем

Негативные проверки:

- пустой логин
- пустой пароль

Запуск в файле: tests/auth/test_auth.py
### Тест по обновлению персональных данных

Позитивные проверки:

- заполнение всех полей формы валидными данными

Негативные проверки обязательных полей:

- поочередное заполнение обязательных полей формы невалидными данными<br>

Запуск в файле: \tests\profile\test_profile.py

### Тест по добавлению и удалению курсов
Позитивные проверки:

- заполнение всех полей формы курсов валидными данными
- удаление курса

Негативные проверки обязательных полей:

- поочередное заполнение обязательных полей формы курсов невалидными данными<br>

Запуск в файле: \tests\profile\test_courses.py
### Создание отчетов при помощи Allure:

- Установить локально Allure commandline application (посмотреть инструкцию можно [здесь](https://docs.qameta.io/allure/))

- Выполнить в терминале команду pytest --alluredir=allure_reports

- Перезапустить PyCharm

- Выполнить в терминале команду allure serve allure_reports

### testing application:
https://qacoursemoodle.innopolis.university
