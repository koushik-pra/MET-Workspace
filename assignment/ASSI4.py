users= {
    ("john", "1234"): "admin",
    ("alice", "abcd"): "editor"
        }
username =str(input("enter user id: "))
password =str(input("enter user password: "))
credentials = (username, password)
if credentials in users:
    role = users[credentials]
    print(f"Welcome , {role} ")
else:
    print("invalid login")
