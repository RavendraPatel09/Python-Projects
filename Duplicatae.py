nums = [1,2,2,3,4,4,5]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)