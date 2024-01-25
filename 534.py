#Given a string, determine whether any permutation of it is a palindrome
"""For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome."""


#fuction to check if chars in the string can form pallindrome

def canFormPalindrome(st):
    l=[]

    for el in st:
        if el in l:
            l.remove(el)
        else:
            l.append(el)

    if(len(st)%2==0 and len(l)==0 or len(st)%2==1 and len(l)==1 ):
        return True
    else:
        return False
    

    
if (canFormPalindrome("geeksforgeeks")):
    print("Yes")
else:
    print("No")
 
if (canFormPalindrome("geeksogeeks")):
    print("Yes")
else:
    print("No")


"""note:
Palindrome word is mentioned to distract you from actual solution 
understand the question dont fall for tricks"""
