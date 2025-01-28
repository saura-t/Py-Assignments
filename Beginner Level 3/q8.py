def parse_str(s):
    details = s.split('000')

    return {'first_name': details[0], 'last_name': details[1], 'id': details[2]}


if __name__ == "__main__":
    try:
        s = input("Enter input str: ")
        print(f"{parse_str(s)}")
    except Exception as e:
        print(e)
