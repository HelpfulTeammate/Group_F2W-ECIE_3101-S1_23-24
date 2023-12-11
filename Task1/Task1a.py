from array import array

print("How many elements in the array?")
N = int(input()) #no of input
print("Insert the element(s):")

inputs = array("f")
for i in range (N):
    try:
        element = float(input())
        inputs.append(element)
    except ValueError:
        print("Invalid input is not an integer or float.")

inputs_list = list(inputs) #conv to list
total = sum(inputs_list)
average = total / len(inputs_list)
maximum = max(inputs_list)
minimum = min(inputs_list)
range = maximum - minimum

print("The total value is: ", total)
print("The average value is: ", average)
print("The maximum value is: ", maximum)
print("The minimum value is: ", minimum)
print("The range  is: ", range)