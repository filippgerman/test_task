from events.baseForm import BaseForm

class RefusalPurchase(BaseForm):
    def __init__(self, settings):
        super().__init__()
        self.user_id = settings['user_id']
        self.event = 'Отказ от покупки'
        self.datetime = self.generation_time()    


