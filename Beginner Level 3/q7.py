def parse_list(d1, d2):
    names = d1.split(',')
    subjects = d2.split(',')
    if not len(names) == len(subjects):
        return "number of students and subject does not match"
    res = {}
    for i in range(len(subjects)):
        res[names[i]] = subjects[i]

    return res


if __name__ == "__main__":
    try:
        names = input("Enter names of students(',' seperated): ")
        subjects = input("Enter subjects of each student(',' seperated): ")
        print(f"{parse_list(names, subjects)}")
    except Exception as e:
        print(e)
