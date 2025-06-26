import json


with open('users.json', 'r') as f:
    users = json.load(f)


new_user = {"id": 3, "name": "Charlie"}
users.append(new_user)

with open('updated_users.json', 'w') as f:
    json.dump(users, f, indent=4)

print("User added and updated_users.json created.")