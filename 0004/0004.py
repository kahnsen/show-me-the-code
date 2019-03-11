import string


def extend_word(text):
    if text.find('\'') > 0:
        old2new = dict()
        words = text.split()
        for word in words:
            if word.find('\'') > 0:
                parts = word.split('\'')
                if parts[1] == 'm':
                    parts[1] = 'am'
                elif parts[1] == 's':
                    parts[1] = 'is'
                elif parts[1] == 're':
                    parts[1] = 'are'
                elif parts[1] == 't':
                    parts[1] = 'not'
                elif parts[1] == 've':
                    parts[1] = 'have'
                elif parts[1] == 'll':
                    parts[1] = 'will'
                elif parts[1] == 'd':
                    if words[words.index(word) + 1] == 'better':
                        parts[1] = 'had'
                    else:
                        parts[1] = 'would'
                if parts[0].endswith('n'):
                    parts[0] = parts[0][:-1]
                old2new[word] = ' '.join(parts)
        _text = text
        for old_word in old2new.keys():
            _text = _text.replace(old_word, old2new[old_word])
        return _text


def return_order_key(record):
    return record[1]

def show_in_order(records):
    # 迭代records.items()，迭代中，需要毕节的元素：key=return_order_key。排序，reverse：True
    items = sorted(records.items(), key=return_order_key, reverse=True)
    for item in items:
        print(item[0], item[1])

def countWords():
    with open('words.txt', 'r') as  file:
        article = file.read()
        no_pun_text = article
        # print(no_pun_text)
        # punctuation为英文字符中的特殊字符 !"#$%&()*+,-./:;<=>?@[\]^_`{|}~
        # 把'符号去除，留下别的特殊字符
        _punctuation = string.punctuation.replace('\'', '')
        print(_punctuation)
        # 循环删除所有特殊字符
        for pun in _punctuation:
            no_pun_text = no_pun_text.replace(pun, '')

        # 把所有英文中的缩写都替换成全拼 例如 I'm didn't
        complete_text = extend_word(no_pun_text)
        print('#################################')
        print(complete_text)
        records = dict()
        # 统计每个单词的数量
        for word in complete_text.lower().split():
            records[word] = records.get(word, 0) + 1

        # 排序
        show_in_order(records)

if __name__ == "__main__":
    print('0004')
    countWords()