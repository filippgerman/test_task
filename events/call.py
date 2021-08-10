from events.baseForm import BaseForm

class Call(BaseForm):
    def __init__(self, settings):
        super().__init__()
        self.user_id = settings['user_id']
        self.event = 'Звонок'
        self.call = 0
        self.datetime = self.generation_time()
