for i in range(26):
    letter = chr(ord('a') + i)     
    for j in range(100):
        vars()[letter + str(j)] = i * 100 + j + 1

print(a1)    
print(z99)   