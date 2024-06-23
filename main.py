#create a quiz game with admin and players. a user has to login, if player then he can play
#if admin can add quiestions
import json
import users

if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game"
    print(f"{len(welcome_msg) * '='} {welcome_msg} {len(welcome_msg) * '='}")

    users.login()