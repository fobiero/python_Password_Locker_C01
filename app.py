#!/usr/bin/env python3

# from pydoc import pager
from credential import Credential
from passwords import Password


def create_account(first_name, last_name, user_name, password):
    ac = Credential(first_name, last_name, user_name, password)
    return ac


def save_account(ac):
    ac.save_account()


def delete_account(ac):
    ac.delete_account()


def find_accounts(user_name):
    return Credential.find_by_user_name(user_name)


def isexist_accounts(user_name):
    return Credential.account_exists(user_name)


def display_accounts():
    return Credential.display_accounts()


def create_page(page, password):
    passwords = Password(page, password)
    return passwords


def save_page(passwords):
    passwords.save_page()


def find_page(pager):
    return Password.find_by_page(pager)


def is_valid(pager):
    return Password.page_exists(pager)


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()

def main():
    print('WELCOME TO PASSLOCK')
    print('Please Use Options to get you started')
    while True:

        print(" 1) LOGIN \n 2) CREATE ACCOUNT \n 3) ABOUT PASSLOCK \n 4) DISPLAY ACCOUNTS \n 5) LOGOUT")

        select = int(input())
        if select == 1:
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            account = find_accounts(username)
            if account.user_name == username and account.password == password:
                print('LOGIN SUCCESSFUL')
                while True:
                    print(
                        f'Welcome {username},Please select from the Options below')
                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) logout ')

                    log_select = int(input())
                    if log_select == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        page = input()

                        print('password')
                        password = input()

                    # created and saved page
                        save_page(create_page(page, password))

                    elif log_select == 2:
                        print("Enter Page name")

                        page = input()
                        if is_valid(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'I cant find {page}')

                    elif log_select == 3:
                        if display_pages():
                            for log in display_pages():
                                print(f'{log.page}:{log.password}')
                        else:
                            print('NO PASSWORD SAVED YET')
                            print('\n')

                    elif log_select == 4:
                        print('adios')
                        break
            else:
                return False

        if select == 2:
            print('NEW ACCOUNT')
            print('-'*100)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('PASSWORD')
            password = input()

            save_account(create_account(first_name, last_name, user_name, password))
            print('ACCOUNT CREATED')
            while True:

                print(
                    f'Welcome {user_name}, Select from the Options below:')
                print(
                    ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                log_select = int(input())
                if log_select == 1:
                    print('Create page')
                    print('-'*100)

                    print('Page Name: ')
                    page = input()

                    print('password')
                    password = input()

                    # created and saved page
                    save_page(create_page(page, password))

                elif log_select == 2:
                    print("Enter Page Name")

                    page = input()
                    if is_valid(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'PAGE NOT FOUND {page}')

# @TODO: Debug positional arguments to DELETE PAGE
                elif log_select == 3:
                    if display_pages():
                        for pag in display_pages():
                            print(
                                f'{pag.page}:{pag.password}'
                            )
                    else:
                        print('NO PASSWORDS CREATED')

                elif log_select == 4:
                    break

        elif select == 3:
            print('ABOUT PASSLOCK')
            print(
                '''
            PassLock is a scriped based aplication that helps(allows) users to store multiple passwords on different accounts. Using, passlock one is able to track all his/her social media accounts passwords and thus very secure against fraud and hacks  
                ''')

        elif select == 4:
            if display_accounts():
                for account in display_accounts():
                    print(
                        f'{account.user_name}'
                    )
            else:
                print('NO ACCOUNTS')

        elif select == 5:
            print('Untill next time.!GOODBYE :)')
            break


if __name__ == '__main__':
    main()
