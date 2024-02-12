'''Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.'''
def calcangle(h,m):
    if(m==60):
        h=h+1
    elif(h>12 and h!=12):
        h=h-12
        angle= abs((h*30)-(m*6))

    angle= abs((h*30 +(m/2))-(m*6))
    return min(angle, 360-angle)


s=input()
h=int(s[:2])
m=int(s[3:])
print(calcangle(h,m))
