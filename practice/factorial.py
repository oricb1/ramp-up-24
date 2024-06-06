n = 4

#Use for loop to find factoriaal
def main():
    product = 1
    for i in range(1, n+1) : 
        product = i * product
    print(product)

main()

#Use recursion to find factorial
def recursive(m):
    if(m == 1):
        return 1
    else:
        return(m * recursive(m-1))

factorial = recursive(n)
print(factorial)