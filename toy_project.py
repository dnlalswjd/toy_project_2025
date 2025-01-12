import json

with open('following.json', 'r') as file:
    followingFile = json.load(file)

with open('followers_1.json', 'r') as file:
    followersFile = json.load(file)

with open('pending_follow_requests.json', 'r') as file:
    requestFile = json.load(file)

following = []
for value in followingFile.values():
    for followingData in value:
        following.append(followingData["string_list_data"][0]["value"])

followers = []
for followersData in followersFile:
    followers.append(followersData["string_list_data"][0]["value"])

request = [] #내가 팔로우를 요청한, 남의 비공개 계정
for value in requestFile.values():
    for requestData in value:
        request.append(requestData["string_list_data"][0]["value"])

result1 = [] #나만 상대를 팔로우하는 계정
for user in following:
    if user not in followers:
        result1.append(user)

result2 = [] #상대만 나를 팔로우하는 계정
for user in followers:
    if user not in following:
        result2.append(user)

print("[내 계정의 팔로잉 수: {} / 나만 상대를 팔로우하는 계정 수: {}]".format(len(following), len(result1)))
if len(result1):
    for user in result1:
        print(user)

print("[내 계정의 팔로워 수: {} / 상대만 나를 팔로우하는 계정 수: {}]]".format(len(followers), len(result2)))
if len(result2):
    for user in result2:
        print(user)

print("[내가 팔로우를 요청한 비공계 계정 수: {}]".format(len(request)))
if len(request):
    for user in request:
        print(user)