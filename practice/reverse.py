def main():
    string = input()
    print(string[::-1])
    print("Number of Vowels: " + str(countVowel(string)))

#Returns number of vowles in word
def countVowel(word):
    i =0
    Vowels = "aeiouAEIOU"
    for char in word :
        if char in Vowels:
            i = i +1
    return i

main()
