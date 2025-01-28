def get_total_lines(file_path):
    ctr = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                ctr += 1
        return ctr
    except FileNotFoundError as err:
        print(f"{file_path} does not exist!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    file = "demo.txt"
    print(f"Number of lines in {file}: {get_total_lines(file)}")
