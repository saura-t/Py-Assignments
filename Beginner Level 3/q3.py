def replace_jtoi(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        text = text.replace('j','i')
        text = text.replace('J','I')

        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError as err:
        print(f"{file_path} does not exist!")
    except Exception as e:
        print(e)
    return "Text replaced successfully!"

if __name__ == "__main__":
    file = "words.txt"
    print(f"{replace_jtoi(file)}")
    