def get_even_length_strings(file_path):
    res = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                for word in line.split():
                    if len(word) % 2 == 0:
                        res.append(word)
    except FileNotFoundError:
        return "File not found."
    return res


if __name__ == "__main__":
    try:
        [print(f"{word}", end=" ") for word in get_even_length_strings("doc.txt")]
    except Exception as e:
        print(e)
