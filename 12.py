def mirror(arr):
    mirrored_part = arr.copy()
    mirrored_part.reverse()
    arr += mirrored_part


lst = [1, 2]
mirror(lst)
print(*lst)
