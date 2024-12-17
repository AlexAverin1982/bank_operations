# Домашняя работа 11.1 Генераторы
## Цель проекта
Освоить технологию использования генераторных выражений и их тестирование

## Инструкции по установке
- Скопируйте файл `processing.py` в каталог с вашим кодом
- В модуле, использующем функции, пропишите импорт модуля `processing.py` 
## Реализация функций
### Функция `filter_by_currency(transactions: list[dict], currency: str)`
  + #### принимает на вход 
    + список словарей с данными о банковских операциях; 
    + параметр `currency` - обозначение валюты;
  + #### возвращает
    генератор списка словарей, описывающих операции по указанной валюте
### Функция `transaction_descriptions(transactions: list[dict])`
  + #### принимает на вход 
    + список словарей с данными о банковских операциях; 
  + #### возвращает
     описание очередной операции, по одному за вызов.
### Функция `card_number_generator(start_no: int = 1, end_no: int = 9999999999999999)`
  + #### принимает на вход 
    + опциональные границы диапазона генерируемых номеров; 
  + #### возвращает
    генератор списка номеров карт из опционально указанного диапазона
### Функция `filter_by_state(data_in: list[dict], state: str)` 
  + #### принимает на вход 
    + список словарей с данными о банковских операциях; 
    + параметр `state` (по умолчанию имеет значение 'EXECUTED');
  + #### возвращает
    новый список, содержащий только те словари, у которых ключ `state` содержит переданное в функцию значение.
      
  
### Функция `sort_by_date(data_in: list[dict], desc_order: bool)` 
  + #### принимает на вход 
    + список словарей; 
    + параметр порядка сортировки `desc_order` (по умолчанию 'True', по убыванию)
  + #### возвращает
     новый список, в котором исходные словари отсортированы по дате.

## Примеры использования функций
Вызов `list(card_number_generator(1, 2))` вернет список номеров карт
`"0000 0000 0000 0000 0001" и "0000 0000 0000 0000 0002"`
Для списка словарей 
```commandline
    test_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
```
вызов `filter_by_state(test_data)` вернет список только тех словарей, в которых ключ `state` равен `EXECUTED`.
А вызов `sort_by_date(test_data, desc_order=False)` вернет список словарей, отсортированный по дате по возрастанию (т.е. сначала самые ранние записи).

## Инструкции по тестированию
- Запуск тестирования производится в активированной виртуальной среде, это делается вводом в консоли командой 
  `poetry shell` в корневом каталоге проекта
- Запуск всех тестов производится командой консоли `pytest` в корневом каталоге
- Команда `pytest --cov --cov-report=html` обновляет отчет проверки покрытия кода тестами в подкаталоге `htmlcov` 
 
