def find_smallest(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Example usage
num1 = 5
num2 = 10
smallest = find_smallest(num1, num2)
print(f"The smallest number between {num1} and {num2} is {smallest}.")
