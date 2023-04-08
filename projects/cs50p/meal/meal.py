def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


def main():
    time_str = input("Enter a time in 24-hour format (e.g., 7:30): ")
    time = convert(time_str)

    if 7.0 <= time < 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time < 13.0:
        print("It's lunch time!")
    elif 18.0 <= time < 19.0:
        print("It's dinner time!")


if __name__ == "__main__":
    main()
