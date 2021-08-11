from datetime import datetime, timedelta
from random import randint, choice


class BaseForm():
    '''
    Форма для заполнения создания нового пользователя
    '''
    def __init__(self):
        self.user_id = ' '
        self.datetime = datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        self.event = ' '
        self.source = ' '
        self.type_browser = ' '
        self.number_page = ' '
        self.call = ' '
        self.purchase_amount = ' '

    def get_data(self):
        '''
        Получение списка данных
        '''
        return [self.event,
                self.datetime,
                self.user_id,
                self.source,
                self.type_browser,
                self.number_page,
                self.call,
                self.purchase_amount,
        ]
    
    def generation_time(self):
        hours = randint(0,24)
        minutes = randint(0,60)
        seconds = randint(0, 60)
        new_date = datetime.strptime(self.datetime, "%Y-%m-%d-%H.%M.%S")  + timedelta(hours=hours, minutes=minutes, seconds=seconds) 
        return new_date.strftime("%Y-%m-%d-%H.%M.%S")


