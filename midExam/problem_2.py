friends = input().split(", ")
blacklisted_count = 0
lost_count = 0

def is_valid_index(index):
    return 0 <= index < len(friends)

while True:
    command = input()
    if command == "Report":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "Blacklist":
        name = command_parts[1]
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
            blacklisted_count += 1
        else:
            print(f"{name} was not found.")

    elif action == "Error":
        index = int(command_parts[1])
        if is_valid_index(index) and friends[index] != "Blacklisted" and friends[index] != "Lost":
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"
            lost_count += 1

    elif action == "Change":
        index = int(command_parts[1])
        new_name = command_parts[2]
        if is_valid_index(index):
            current_name = friends[index]
            print(f"{current_name} changed his username to {new_name}.")
            friends[index] = new_name

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(" ".join(friends))
