import json

with open('following.json', 'r') as file:
    followingFile = json.load(file)

with open('followers_1.json', 'r') as file:
    followersFile = json.load(file)

following = []
for value in followingFile.values():
    for followingData in value:
        following.append(followingData["string_list_data"][0]["value"])

followers = []
for followersData in followersFile:
    followers.append(followersData["string_list_data"][0]["value"])

result1 = [] #나만 상대를 팔로우하는 계정
for user in following:
    if user not in followers:
        result1.append(user)

result2 = [] #상대만 나를 팔로우하는 계정
for user in followers:
    if user not in following:
        result2.append(user)

print("[나만 상대를 팔로우하는 계정 목록]")
if not(len(result1)):
    print("없음")
else:
    for user in result1:
        print(user)

print("[상대만 나를 팔로우하는 계정 목록]")
if not(len(result2)):
    print("없음")
else:
    for user in result2:
        print(user)