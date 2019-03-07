import base64
import re

def parse(base64Str):
    return base64.urlsafe_b64decode(base64Str.encode('utf-8'))

if __name__ == '__main__':
    str1 = parse('Z29vZHM6NTg5L2lkOjExNzg=')
    str2 = str1.decode()
    print(str1)
    print(str2)
    reStr = re.findall(r'(.*):(.*)/(.*):(.*)', str(str2))
    reStrArr = reStr.pop()
    print(reStrArr)
    # print(reStrArr[0] + '  ' + reStrArr[1])
    # print(reStrArr[2] + '  ' + reStrArr[3])
