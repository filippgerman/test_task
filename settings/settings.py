from events.visitSite import VisitSite
from events.purchase import Purchase
from events.call import Call
from events.refusalPurchase import RefusalPurchase
import csv

FILE_NAME = 'journal.csv'
PATH_TO_FILE = '.'
FIELDNAMES = ['Событие',
              'Дата / Время',
              'ID пользователя',
              'Источник',
              'Тип браузера',
              'Кол-во просмотренных страниц',
              'Звонок не успешный',
              'Сумма заказа',
]

LIST_CLASS_EVENT = [
    VisitSite,
    Call,
    Purchase,
    RefusalPurchase,
]

INDEX_CALL = LIST_CLASS_EVENT.index(Call) 
MAX_USERS = 20

SOURCES = ['Яндекс','Гугл','Фейсбук']
TYPES_BROWSER = ['Мобильный','Планшет', 'Десктоп']
MAX_NUMBER_PAGE = 10
MAX_SUM = 1_000_000
MIN_SUM = 10_000



