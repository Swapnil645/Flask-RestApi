from user import Users

# users = [
#    User(1,'bob','asdf')
# ]

# username_mapping = {u.username:u for u in users} 
# userid_mapping = {u.id:u for u in users}


# # username_mapping = {'bob':{
# #         'id':1,
# #         'username':'bob',
# #         'password':'asdf'
# #     }}

# # userid_mapping = {1:{
# #         'id':1,
# #         'username':'bob',
# #         'password':'asdf'
# #     }}


def authenticate(username,password):
    #user = username_mapping.get(username,None)
    user = Users.find_by_username(username)
    print(user)
    if user and user.password==password:
        return user

def identity(payload):
    user_id = payload['identity']
    #return userid_mapping.get(user_id,None)
    return Users.find_by_id(user_id)