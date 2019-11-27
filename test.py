s = input()
st = ""
c = 0
for i in range(len(s)):
    if c == 0:
        print(c,i)
        st+=i.upper()
        c += 1
    elif i == " ":
        st+=i
        c=0
    else:
        st+=i
        c+=1
print(st)