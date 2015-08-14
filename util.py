# coding=utf-8
"""
空格前面是中文就移除该空格
"""
import re


def mstrip(line=u"优米 X1  官方恢复教程兼救砖教程|优米|教程"):
    line, num = re.subn('\s+', ' ', line)
    newline = []
    preWordChinese = False
    for uchar in line:
        if (uchar > u'\u4e00') and (uchar < u'\u9fa5'):
            newline.append(uchar)
            preWordChinese = True
        elif len(uchar.encode('utf-8').strip()) == 0 and preWordChinese:
            preWordChinese = False
            pass
        else:
            preWordChinese = False
            newline.append(uchar)
    # print ''.join(newline).encode('utf-8')
    return ''.join(newline)


if __name__ == "__main__":
    mstrip()
