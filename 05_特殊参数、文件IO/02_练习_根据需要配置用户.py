def create_user(username, password, is_admin=False, is_active=True, is_verified=False):
    print("创建用户...")
    print("Username: ", username)
    print("Password: ", password)
    print("is_admin: ", is_admin)
    print("is_active: ", is_active)
    print("is_verified: ", is_verified)
    print("用户创建成功!----------------------------------")

create_user("john", "password")
create_user("jane", "password123", is_admin=True)
create_user("alice", "pass123", is_active=False, is_verified=True)