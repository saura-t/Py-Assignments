class Time:
    def __init__(self, H: int, M: int):
        self.H = H
        self.M = M

    def add_time(self, t2):
        try:
            addMins = self.M + t2.M
            mins = addMins % 60
            hrs = self.H + t2.H + (1 if addMins > 60 else 0)
            return Time(hrs, mins)
        except Exception as e:
            print(e)
    
    def display_time(self):
        return f"{self.H} hours and {self.M} minutes"
    
    def display_mins(self):
        return f"{(self.H*60)+self.M} minutes"


if __name__ == "__main__":
    try:
        time1 = input("Enter hours and minutes(',' seperated): ")
        time2 = input("Enter hours and minutes(',' seperated): ")
        time1 = list(map(int, time1.split(',')))
        time2 = list(map(int, time2.split(',')))
        t1 = Time(time1[0], time1[1])
        t2 = Time(time2[0], time2[1])
        print(
            f"Total hours and minutes: {t1.add_time(t2).display_time()}")
        print(f"Minutes for {time1[0]} hours, {time1[1]} minutes: {t1.display_mins()}")
    except Exception as e:
        print(e)
