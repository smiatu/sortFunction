
l2 = [32, -9560000, 21, -9999999912, 11, 1, -9000, -9000, -890000]
for i in range(len(l2)):
    l2.append(l2.pop(l2.index(min(l2[0:len(l2)-i]))))

print(l2)