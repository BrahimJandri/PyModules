def ft_plot_area():
    length = input("Enter length: ") # we use input() to get user input, it returns a string, so we need to convert it to float to perform mathematical operations
    width = input("Enter width: ")
    area = float(length) * float(width)
    print(f"Plot area: {area}")
    
if __name__ == "__main__": # why we use this condition? because when we import this module in another file, we don't want to execute the code inside this block
    ft_plot_area()