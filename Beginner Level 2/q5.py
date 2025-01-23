def get_temp_stats(temps):
    stats = {}
    temps = temps.split(',')
    temps = list(map(int,temps))
    stats['avg'] = sum(temps) / len(temps)
    stats['high'] = max(temps)
    stats['low'] = min(temps)
    return stats


if __name__ == "__main__":
    try:
        temps = input("Enter values(',' seperated): ")
        print(f"Average Temperature: {get_temp_stats(temps)['avg']}")
        print(f"Highest Temperature: {get_temp_stats(temps)['high']}")
        print(f"Lowest Temperature: {get_temp_stats(temps)['low']}")
    except Exception as e:
        print(e)