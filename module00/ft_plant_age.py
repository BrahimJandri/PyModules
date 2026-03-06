def ft_plant_age():
    age = input("Enter plant age in days: ")
    if int(age) < 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
        
if __name__ == "__main__":
        ft_plant_age()