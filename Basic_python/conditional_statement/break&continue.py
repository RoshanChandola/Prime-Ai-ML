# using break and continue statements in loops
# # break statement: Used to exit a loop prematurely when a certain condition is met.     
# continue use to skip the current iteration of a loop and move to the next iteration.
# # continue statement:
for num in range(10):
    if num == 5:
        continue  # Skip the rest of the loop when num is 5
    print(num)
# break example:
print("______")
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)