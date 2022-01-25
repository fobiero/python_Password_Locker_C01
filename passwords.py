class Password:
    def __init__(self, page, password):
        self.page = page
        self.password = password

# all the user passwords stored here 
    user_pass = []

    def save_page(self):
        Password.user_pass.append(self)

    def delete_page(self):
        Password.user_pass.remove(self)

    # @TODO: Check created accounts 
    def display_page(cls):
        return cls.user_pass

    # @classmethod
    def find_by_page(cls, pager):
        for paged in cls.user_pass:
            if paged.page == pager:
                return paged

    # @classmethod
    def page_exists(cls, pager):
        for paged in cls.user_pass:
            if paged.page == pager:
                return paged
        return False
