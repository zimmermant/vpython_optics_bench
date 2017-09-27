### A quick look at `for` loops

### Run through numbers from 0 to 9
# The range() command starts at zero with step size of 1 and runs until i = 10
for i in range(10):
    print(i)
    print("This is a for loop")   

### Run through numbers 0 to 3.5 in steps of 0.5
for i in range(0,4,0.5):
    print(i)


### Python can iterate through a list of items
# range() actually creates a list of numbers and the for loop iterates through them

list_of_things=["a","b","c","d"] # Creates a list of letters a-d

for j in list_of_things:
    print(j)
