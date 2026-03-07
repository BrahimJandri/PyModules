def ft_water_reminder():
    days = input("Days since last watering: ")
    if int(days) > 2:
        print("Water the plants!")
    else:
        print("The plants are fine.")


if __name__ == "__main__":
    ft_water_reminder()