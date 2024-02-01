### Hexlet tests and linter status:
[![Actions Status](https://github.com/kalldrek777/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kalldrek777/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ef38dfa1641a529f399/maintainability)](https://codeclimate.com/github/kalldrek777/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6ef38dfa1641a529f399/test_coverage)](https://codeclimate.com/github/kalldrek777/python-project-52/test_coverage)


## Описание

Task Manager – система управления задачами, подобная http://www.redmine.org/. Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация:

## Requirements
- **Python**
- **Git**
- **Poetry**
- **Pip**

### Переменные окружения

Необходимо в корне проекта создать файл .env и записать туда значения переменных.
<pre>
SECRET_KEY =
DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
</pre>
### Установка
<pre>
$ git clone https://github.com/kalldrek777/python-project-52.git
$ cd python-project-52.git
$ make setup
# Сайт станет доступен по адресу http://127.0.0.1:8000/ и http://0.0.0.0:8000/ 
</pre>