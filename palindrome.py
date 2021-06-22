def isPalindrome(str1):
    i=0
    d=len(str1)-1
    flag=True
    while(i<=d):
        if str1[i]==str1[d]:
            i+=1
            d-=1
            print("In loop",i,d)#just for testing 
            flag=True
        else:
            flag=False
            break
    if flag:
        return True
    else:
        return False
str1=input("Enter String to check its palindrome or not:")
print(isPalindrome(str1))