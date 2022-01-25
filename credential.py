class Credential:
    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_credential = []

    def save_account(self):
        '''
        save accounts to the accounts array
        '''
        Credential.user_credential.append(self)

    def delete_account(self):
        '''
        Delete Account
        '''
        Credential.user_credential.remove(self)
    @classmethod
    def find_by_user_name(cr, user_name):
        '''
        If Username does not exist then terminates app
        '''
        for account in cr.user_credential:
            if account.user_name == user_name:
                return account

    @classmethod
    def account_exists(cr, user_name):
        '''
        Check for Created Accounts
        '''
        for account in cr.user_credential:
            if account.user_name == user_name:
                return True
        return False

    @classmethod
    def display_accounts(cr):
        return cr.user_credential
