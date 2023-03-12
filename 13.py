def from_string_to_list(string, container):
    container += string.split()


a = [1, 2, 3]
from_string_to_list("1 33 99 52", a)
print(*a)

b = [77, "abc"]
from_string_to_list("", b)
print(*b)
