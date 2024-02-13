'''This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".'''

def Encode(s):
    s+='0'
    s1=""
    count=1
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
        else:
            s1+=str(count)+s[i]
            count=1
    return s1

def Decode(s):
    s1=""
    for i in range(0,len(s)-1,2):
        count=int(s[i])
        char=s[i+1]
        s1+=count*char
    return s1

Encoded=Encode('AAAABBBCCDAA')
Decoded= Decode(Encoded)
print(Decoded)

