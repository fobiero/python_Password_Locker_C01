from passwords import Password
import unittest

class TestPasswords(unittest.TestCase):
    def tearDown(self):
        '''
        this test clears the user_passwords array beore every test
        '''
        Password.user_passwords = []

    def setUp(self):
        '''
        this test creates a new instance of the passwords class
        before every test
        '''
        self.new_password = Password('gmail', '12345')

    def test_init(self):
        '''
        this test checks whether the data enterd into the properties if called wll appear
        '''
        self.assertEqual(self.new_password.page, 'gmail')
        self.assertEqual(self.new_password.password, '12345')

    def test_save_page(self):
        '''
        this is a test to check whether the value append to the user_passwords array
        '''
        self.new_password.save_page()
        self.assertEqual(len(Password.user_passwords), 1)

    def test_save_multiple(self):
        '''
        this test like the first now test whether both instances created are appended to the array
        '''
        self.new_password.save_page()
        test_pass = Password('yahoo', '54321')
        test_pass.save_page()
        self.assertEqual(len(Password.user_passwords), 2)

    def test_delete_page(self):
        '''
        this test checks for the delete function that uses the .remove methos
        '''
        self.new_password.save_page()
        test_pass = Password('instagram', '123456')
        test_pass.save_page()
        self.new_password.delete_page()
        self.assertEqual(len(Password.user_passwords), 1)

    def test_display_page(self):
        self.assertEqual(Password.display_page(), Password.user_passwords)

    def test_find_page(self):
        '''
        this test checks whether a password saved can be searched
        '''
        self.new_password.save_page()
        test_pass = Password('instagram', '121314')  # new contact
        test_pass.save_page()
        found_page = Password.find_by_page('instagram')
        self.assertEqual(found_page.page, test_pass.page)

    def page_exists(self):
        '''
        returns a true/false value depending on prescence of the searched password
        '''
        self.new_password.save_page()
        test_pass = Password('instagram', '121314')  # new contact
        test_pass.save_page()
        page_exist = Password.page_exists('instagram')
        self.assertTrue(page_exist)


if __name__ == '__main__':
    unittest.main()
