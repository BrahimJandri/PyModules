def ft_harvest_total():
    harvest1 = input("day 1 harvest: ")
    harvest2 = input("day 2 harvest: ")
    harvest3 = input("day 3 harvest: ")
    total_harvest = int(harvest1) + int(harvest2) + int(harvest3)
    print(f"Total harvest: {total_harvest}")
    
if __name__ == "__main__":
    ft_harvest_total()