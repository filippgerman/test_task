from events.baseForm import BaseForm


class Purchase(BaseForm):
    def __init__(self, settings):
        super().__init__()
        self.user_id = settings['user_id']
        self.event = 'Покупка'
        self.purchase_amount = settings['purchase_amount'] 
        self.datetime = self.generation_time()
