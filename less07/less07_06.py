while True:
    user_string = input("Enter a number")
    try:
        user_num = int(user_string)
    except ValueError as e:
        print(e)
    else:
        print("Good for you")
        break
    finally:
        print("...")