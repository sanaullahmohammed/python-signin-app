lookup = {'user1': 'pass1', 'user2':'pass2'}
isLoggedin = 0


def login_required(func): # func holds the function object. here func = profile() 
    def verify(username):
        if isLoggedin:
            func(username)
        else:
            print("Please sign-in before viewing this page!")
    return verify

@login_required # similar to line 16
def profile(username):
    print("Hello "+username+"!!!")
# profile = login_required(profile)

def login(username, password):
    global isLoggedin # must specify global keyword when re-assigning values to it, no need in case of referencing
    if username in lookup:
        if password == lookup[username]:
            isLoggedin = 1
            print("Successfully signed in!")
        else:
            print("OOPS! incorrect password")
            exit()
    else:
        print("OOPS! incorrect username")
        exit()


if __name__ == "__main__":
    print("Generic Website")
    username = input("Enter username: ")
    password = input("Enter password: ")

    login(username,password)

    profile(username)
