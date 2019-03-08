import re
import base64
import redis

db_info = {
    'host':'127.0.0.1',
    'port':'6379'
}

def make_session():
    r = redis.Redis(host=db_info['host'], port=db_info['port'])
    return r


def parse_coupon(line):
    return base64.urlsafe_b64decode(line.encode('utf-8'))


def updateDb():
    session = make_session()
    with open('coupon.txt', 'r') as file:
        for line in file.readlines():
            c_id = re.findall(r'.*/.*:(.*)\'', str(parse_coupon(line)))
            # print(c_id.pop() + "..." + line.strip())
            session.set(c_id.pop(), line.strip())


if __name__ == '__main__':
    print('0003')
    updateDb()