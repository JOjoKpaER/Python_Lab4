lst = input().split(" ")
print(*[int(i)**2 for i in lst])

print(*[int(i)**2 for i in lst if int(i) % 2 == 1 and i[-1] != "9"])
