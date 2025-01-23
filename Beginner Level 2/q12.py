if __name__ == "__main__":
    try:
        print("Enter login details")
        ctr = 0
        while ctr < 3:
            user = input('username: ')
            pwd = input('password: ')
            if pwd == "password" and user == "admin":
                print("Successful!")
                break
            else:
                print("Try Again!")
                ctr += 1
        if not  ctr < 3:
            print("Try again after later")
    except Exception as e:
        print(e)