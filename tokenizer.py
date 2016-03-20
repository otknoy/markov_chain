#!/usr/bin/env python
import MeCab

# noun_posid_list = range(36, 67+1)
noun_posid_list = range(41, 47+1)

def tokenize(text, only_noun=False):
    '''
    tokenize a text using MeCab with mecab-ipadic-neologd
    '''
    m = MeCab.Tagger('-d /Users/otknoy/local/lib/mecab/dic/mecab-ipadic-neologd/')
    m.parse('')

    node = m.parseToNode(text)

    terms = []
    while node:
        if only_noun:
            if node.posid in noun_posid_list:
                terms.append(node.surface)
        else:
            terms.append(node.surface)

        node = node.next

    return terms[1:-1]


if __name__ == '__main__':
    text = "10日放送の「中居正広のミになる図書館」（テレビ朝日系）で、SMAPの中居正広が、篠原信一の過去の勘違いを明かす一幕があった。"

    print(tokenize(text))
