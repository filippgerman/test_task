from random import choice, randint
from settings.settings import LIST_CLASS_EVENT, SOURCES, TYPES_BROWSER, MAX_NUMBER_PAGE, MIN_SUM, MAX_SUM, INDEX_CALL, FILE_NAME, PATH_TO_FILE, FIELDNAMES, MAX_USERS 
from work_file.workFile import WorkFile



class ProgrammJournal():
    '''
    Класс для запуска программы
    '''
    def __init__(self):
        self.settings = {
                'user_id': WorkFile.get_last_index(FILE_NAME),
                'source': choice(SOURCES),
                'type_browser': choice(TYPES_BROWSER),
                'number_page': randint(1, MAX_NUMBER_PAGE),
                'purchase_amount':  randint(MIN_SUM, MAX_SUM),
        }
        self.index_call = INDEX_CALL + 1


    def generation_user_data(self):
        '''
        Метод ганерации событий для одного польз.
        '''
        events_user = randint(1,4)
        result = []
        count = 0
        
        for class_item in LIST_CLASS_EVENT:
            count += 1
                
            if count > events_user:
                break
                
            if count == self.index_call and events_user > self.index_call:
                obj = class_item(self.settings)
                obj.call = 1
                result.append(obj.get_data())
                continue
                
            result.append(class_item(self.settings).get_data())
                
        return result


    def start_generate(self):
        '''
        Метод генерации информации по польз.
        '''
    
        journal=WorkFile(FILE_NAME, PATH_TO_FILE, FIELDNAMES)
        number_users = randint(1,MAX_USERS)

        for _ in range(number_users):
            journal.writing_file(self.generation_user_data())
            self.settings['user_id'] += 1
            self.settings['source'] =  choice(SOURCES)
            self.settings['type_browser'] = choice(TYPES_BROWSER)
            self.settings['number_page'] = randint(1, MAX_NUMBER_PAGE)
            self.settings['purchase_amount'] = randint(MIN_SUM, MAX_SUM)

ProgrammJournal().start_generate()
