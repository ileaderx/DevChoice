class User:
    def __init__(self, username, password, email, role):
        this.username = username
        this.password = password
        this.email = email
        this.role = role

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, s):
        self._username = s
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, s):
        self._password = s
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, s):
        self._email = s

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, s):
        self._role = s