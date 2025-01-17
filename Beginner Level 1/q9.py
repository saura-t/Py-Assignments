from collections import Counter

def get_freq(s):
    elements = s.split(',')
    elements = Counter(elements)
    return elements

if __name__ == "__main__":
    try:
        elements = input("Enter elements into list (',' seperated): ")
        print(f"Frequency Count: {get_freq(elements)}")
    except Exception as e:
        print(e)