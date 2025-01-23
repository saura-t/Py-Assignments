def get_stone_piles(n):
    piles = [n]
    for i in range(n-1):
        piles.append(piles[i]+2)
    return piles       

if __name__ == "__main__":
    try:
        n = int(input("Enter value: "))
        print(f"Stone piles: {get_stone_piles(n)}")
    except ValueError as err:
        print(err)
    except Exception as e:
        print(e)