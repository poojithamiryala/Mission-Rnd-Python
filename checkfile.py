str1 =input("")
str2=input("")
count=0
if(len(str1)==len(str2)):
    if(str1==str2):
        count=1
elif(len(str1)>len(str2)):
    for i in range(0, len(str1)):
        if (str1[i] == str2[0]):
            if(str1[i:].startswith(str2)):
                count+=1
else:
    for i in range(0, len(str2)):
        if (str2[i] == str1[0]):
            if(str2[i:].startswith(str1)):
                count+=1
print(count)


