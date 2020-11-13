class Plan:
    def __init__(self, plan_id, name, description, cover_img_url, est_time, intended_level):
        self.plan_id = plan_id
        self.name = name
        self.description = description
        self.cover_img_url = cover_img_url
        self.intended_level = intended_level
        self.est_time = est_time

    @property
    def plan_id(self):
        return self._plan_id
    
    @plan_id.setter
    def plan_id(self, i):
        self._plan_id = i

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, s):
        self._name = s
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, s):
        self._description = s
    
    @property
    def cover_img_url(self):
        return self._cover_img_url
    
    @cover_img_url.setter
    def cover_img_url(self, s):
        self._cover_img_url = s

    @property
    def intended_level(self):
        return self._intended_level
    
    @intended_level.setter
    def intended_level(self, s):
        self._intended_level = s
    
    @property
    def est_time(self):
        return self._est_time
    
    @est_time.setter
    def est_time(self, t):
        self._est_time = t