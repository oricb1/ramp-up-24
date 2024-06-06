
Sum = 0
list = input().split(" ")
for char in list:
     Sum = Sum + int(char)

print("Sum: "+ str(Sum))
print("Mean: " + str(Sum/len(list)))

list.sort()
print("minimum: " + str(list[0]))

list.reverse()
print("maximum: " + str(list[0]))

