def ft_count_harvest_iterative():
    count = int(input("Days until harvest: "))
    while count >= 1:
        count -= 1
        print(f"Days: {count}")
    print("Harvest time!")

if __name__ == "__main__":
    ft_count_harvest_iterative()