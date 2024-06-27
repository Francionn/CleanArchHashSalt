
class EmailValidators:
    @staticmethod
    def validate(email:str):
        validators = [
            EmailValidators.body_validator,
            EmailValidators.valid_at_position,
            EmailValidators.valid_structure
        ]
        return all(validator(email) for validator in validators)
    
    @staticmethod
    def body_validator(email):
        return email.count('@') == 1 and email.count('.') != 0
    
    @staticmethod
    def valid_at_position(email): 
        local = email.find('@')
        return email[local-1].isalnum() and email[local+1].isalnum() 
    
    @staticmethod
    def valid_structure(email):
        local_at = email.find('@')
        name = email[:local_at]
        domain = email[local_at+1:]
        return EmailValidators.valid_name(name) and EmailValidators.valid_domain(domain)
    
    @staticmethod   
    def valid_name(name):
        return len(name) > 0 and all(char.isalnum() or char in ".-_" for char in name)
    
    @staticmethod
    def valid_domain(domain):
        return ('.' in domain and not(domain.endswith('.')) and\
        all(char.isalnum() or char in "._" for char in domain))    
