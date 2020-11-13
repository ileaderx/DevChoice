class Resource:
    def __init__(self, resource_id, name, description, resource_url):
        self.resource_id = resource_id
        self.name = name
        self.description = description
        self.resource_url = resource_url

    @property
    def resource_id(self):
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self, i):
        self._resource_id = i
    
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
    def resource_url(self):
        return self._resource_url
    
    @resource_url.setter
    def resource_url(self, s):
        self._resource_url = s