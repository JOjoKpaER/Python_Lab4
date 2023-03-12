friends = {}


def add_friends(name, friend_list):
    if name in friends:
        friends.update({name: friend_list + friends[name]})
    else:
        friends.update({name: friend_list})


def are_friends(name1, name2):
    try:
        return bool(name1 in friends[name2])
    except KeyError:
        try:
            return bool(name2 in friends[name1])
        except KeyError:
            return False


def print_friend(name):
    print(sorted(friends[name]))


add_friends("Алла", ["Марина", "И"])
print_friend("Алла")
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print_friend("Алла")
print(are_friends("Алла", "Мария"))
