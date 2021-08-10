from .baseForm import BaseForm

class VisitSite(BaseForm):
    def __init__(self, settings):
        super().__init__()
        self.user_id = settings['user_id']
        self.datetime = self.generation_time() 
        self.event = 'Визит на сайт'
        self.source = settings['source']
        self.type_browser = settings['type_browser']
        self.number_page = settings['number_page']
