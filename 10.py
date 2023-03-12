msgs = []


def print_without_duplicates(message):
    if message not in msgs:
        print(message)
        msgs.append(message)
    return


print_without_duplicates("Привет")
print_without_duplicates("Не дозвониться")
print_without_duplicates("Не дозвониться")
print_without_duplicates("Не дозвониться")
print_without_duplicates("Ага")
print_without_duplicates("Ага")
