#Тестовое задание для компании "Тензор"

# Проект автоматизации тестирования с использованием Selenium и Pytest
Проект создан с целью демонстрации навыков в области автоматизации тестирования на языке программирования Python. 
В проекте реализованы автоматизированные тесты для трех сценариев, используя Selenium WebDriver и фреймворк Pytest. 
Один из сценариев реализует возможность скачивания файлов с проверкой успешности загрузки.

В качестве источников используются сайты https://sbis.ru/ и https://tensor.ru/.

Реализовано логирование с использованием встроенной библиотеки logging

## Требования
* Python 3
* Установленные зависимости из `requirements.txt`
* Браузер Firefox

## Использование
### Запуск на локальной машине с установленным Firefox
1. Создайте виртуальное окружение и установите зависимости
2. Скачайте geckodriver в папку с проектом
2. Запуск тестов
```shell
  pytest -sv
```
