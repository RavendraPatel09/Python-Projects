A= input("Enter the first Anagram: ")
B= input("Enter the second Anagram: ")
A=A.lower()#Convert to lowercase
B=B.lower()
for i in A:#₹
    if A.isalpha():#Check for alphabetic characters
        if A.count(i)!=B.count(i):#Compare the count of each character
            print("Not Anagrams")#If counts don't match, they are not anagrams
            break#Exit the loop
else:
    print("Anagrams")