import argparse
import getpass
import sys


def create_user(opts):
    from airflow.contrib.auth.backends.password_auth import PasswordUser
    from airflow import models, settings
    

    u = PasswordUser(models.User())
    u.username = opts['username']
    u.email = opts['email']
    u.password = opts['password']
    u.superuser = opts['super_user']
    s = settings.Session()
    s.add(u)
    s.commit()
    s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', dest='email', required=True)
    parser.add_argument('-u', dest='username', default='')
    parser.add_argument('-s', dest='super_user', action='store_true', default=False)
    args = parser.parse_args()

    if args.username == '':
        # Default username is the local part of the email address
        args.username = args.email.split('@')[0]

    args.password = getpass.getpass(prompt="Enter new user password: ")
    confirm = getpass.getpass(prompt="Confirm:  ")

    if args.password != confirm:
        sys.stderr.write("Passwords don't match\n")
        sys.exit(1)
    create_user(vars(args))