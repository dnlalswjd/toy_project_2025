import json

#나만 팔로우한 계정은 팔로워에는 없고 팔로잉에만 있음
#(내 팬이 있는 게 아닌 이상) 이론상 팔로잉 > 팔로워
#즉 팔로잉을 기준으로 팔로워 목록에 있나없나 판단

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