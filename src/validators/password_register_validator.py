
class PasswordValidator:
    @staticmethod   
    def validate(password: str) -> bool:
        validadors = [
            PasswordValidator.size_pw,
            PasswordValidator.check_num_and_str,
            PasswordValidator.check_special
        ]
        for validator in validadors:
            if not validator(password):
                return False
        return True
    
    @staticmethod
    def size_pw(password):
        return len(password) >= 8
    
    @staticmethod
    def check_num_and_str(password):
        num = any(char.isdigit() for char in password)
        letter = any(char.isalpha() for char in password)
        return num and letter
    
    @staticmethod
    def check_special(password):
        special_characters = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
        return any(char in special_characters for char in password)
    