class Credential:
    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_accounts = []

    def save_account(self):
        '''
        save accounts to the accounts array
        '''
        Credential.user_accounts.append(self)

    def delete_account(self):
        '''
        Delete Account
        '''
        Credential.user_accounts.remove(self)
    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        If Username does not exist then returns to account
        '''
        for account in cls.user_accounts:
            if account.user_name == user_name:
                return account

    @classmethod
    def account_exists(cls, user_name):
        '''
        Check for accounts
        '''
        for account in cls.user_accounts:
            if account.user_name == user_name:
                return True
        return False

    @classmethod
    def display_accounts(cls):
        return cls.user_accounts
