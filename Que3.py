S  =input("Enter a string :")
count = 0
inc =0
for i in range(len(S)):
    if S[i:i+3]=='cat':
        count = count+1
print(count)
for i in range(len(S)):
    if S[i:i+3]=='dog':
        inc = inc+1
print(inc)
if count==inc:
    print("True")
else:
    print("False")