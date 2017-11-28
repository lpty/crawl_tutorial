# -*- coding: utf-8 -*-
import re
import hashlib


def hash_md5(string):
    md5 = hashlib.md5()
    try:
        md5.update(string.encode('utf-8'))
    except Exception as e:
        md5.update(string)
    return md5.hexdigest()


def parse_tool(content):
    '''
    清除html标签
    :return:
    '''
    if type(content) != str: return content
    sublist = ['<p.*?>', '</p.*?>', '<b.*?>', '</b.*?>', '<div.*?>', '</div.*?>',
               '</br>', '<br />', '<ul>', '</ul>', '<li>', '</li>', '<strong>',
               '</strong>', '<table.*?>', '<tr.*?>', '</tr>', '<td.*?>', '</td>',
               '\r', '\n', '&.*?;', '&', '#.*?;', '<em>', '</em>', '<dt>', '</dt>',
               '<dd>', '</dd>', '<a.*?>', '</a.*?>', '<span.*?>', '</span.*?>',
               '<th.*?>', '</th.*?>', '<label.*?>', '</label.*?>', '<h4.*?>',
               '<font.*?>', '</font.*?>', '<thread.*?>', '</thread.*?>',
               '</tbody.*?>', '<tbody.*?>', '</table.*?>', '</h4.*?>']
    try:
        for substring in [re.compile(string, re.S) for string in sublist]:
            content = re.sub(substring, "", content).strip()
    except Exception as e:
        print('parse_tool:' + str(e))
    finally:
        return content


def extract_str(items):
    content = ''
    for item in items:
        content += str(item.encode('utf-8'))
    content = parse_tool(content)
    return content


def parse_info(r, p, i=0):
    '''
    解析信息
    :return:
    '''
    try:
        pattern = re.compile(p, re.S)
        items = re.findall(pattern, r)
        if not i:
            item = items[i]
        else:
            item = items
    except Exception as e:
        print('parse_info:' + str(e))
        item = ''
    finally:
        return item
