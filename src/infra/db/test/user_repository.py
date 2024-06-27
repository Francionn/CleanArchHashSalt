import bcrypt

class UserRepositorySpy:
    
    def __init__(self) -> None:
        self.create_user_attributes = {}
        self.user_login_attributes = {}
        self.delete_attributes = {}
        self.get_name_attributes = {}
    
    def create_user(self, name: str, password: str, email: str) -> bool:   
        self.create_user_attributes["name"] = name
        self.create_user_attributes["password"] = password
        self.create_user_attributes["email"] = email
   
    def login(self, email: str, password: str) -> bool:
        self.user_login_attributes["email"] = email
        self.user_login_attributes["password"] = password
        return self.user_login_attributes == {'email': email, 'password': password}
  
    def delete(self, id: int) -> None:
        self.delete_attributes["id"] = id
        return self.delete_attributes == {'id': id }
       
              
    def get_name(self, email: str) -> str:
        self.get_name_attributes["email"] = 'any@teste.com'
        self.get_name_attributes["name"] = 'teste'
        
        if self.get_name_attributes["email"] != email:
            raise Exception('not found name')
        return self.get_name_attributes["name"]
   