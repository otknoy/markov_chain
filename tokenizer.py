#!/usr/bin/env python
import MeCab

def tokenize(text):
    '''
    tokenize a text using MeCab with mecab-ipadic-neologd
    '''
    m = MeCab.Tagger('-d /Users/otknoy/local/lib/mecab/dic/mecab-ipadic-neologd/')
    m.parse('')

    node = m.parseToNode(text)

    terms = []
    while node:
        terms.append(node.surface)

        node = node.next

    return terms[1:-1]


if __name__ == '__main__':
    text = "10日放送の「中居正広のミになる図書館」（テレビ朝日系）で、SMAPの中居正広が、篠原信一の過去の勘違いを明かす一幕があった。"

    print(tokenize(text))
