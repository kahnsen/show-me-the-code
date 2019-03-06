import base64
import uuid

coupon= {
    'id':'1111',
    'goods':'0001',
}

def gen_code(param):
    coupon['id'] = param
    coupon['goods'] = param
    raw = '/'.join([ k + ':' + v for k, v in coupon.items()])
    raw_base64 = base64.urlsafe_b64encode(raw.encode('UTF-8'))
    return raw_base64.decode()


def save_coupon(c_code):
    with open('coupon.txt', 'a+') as file:
        file.write(c_code + '\n')

def gen_all():
    print('gen_all')
    for i in range(1000, 1200):
        c_code = gen_code(str(i))
        save_coupon(c_code)
        # print(uuid.uuid4())

def parse_coupon(c_code):
    print('解析优惠吗', base64.urlsafe_b64decode(c_code.encode('UTF-8')))

if __name__ == '__main__':
    print('0001')
    gen_all()