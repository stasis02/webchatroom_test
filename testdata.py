url = 'http://127.0.0.1:8000'
username = {
    'normal1': '111',
    'normal2': 'aaa',
    'normal3': 'a@#$%^&*()_+',
    'unnormal1': '(•́へ•́╬)',
    'unnormal2': '12345678901234567890123456789012345678901234567890123456789012345678901234567890',
    'unnormal3': ''
}
# meetingname= {
#     'normal1': '111',
#     'normal2': 'aaa',
#     'normal3': 'a@#$%^&*()_+',
#     'unnormal1': '(•́へ•́╬)',
#     'unnormal2': '12345678901234567890123456789012345678901234567890123456789012345678901234567890',
#     'unnormal3': ''
# }
def get_label(n):
    labels = list(username.keys())  # 将字典的键转换为列表
    return labels[n-1]
def get_name(n):
    names = list (username.values())
    return names[n-1]
def get_label_m(n):
    labels = list(username.keys())  # 将字典的键转换为列表
    return labels[n-1]
def get_name_m(n):
    names = list (username.values())
    return names[n-1]