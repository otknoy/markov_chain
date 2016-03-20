#!/usr/bin/env python

def ngram(tokens, n=2):
    tokens = tokens[:]
    tokens.insert(0, '(BOS)')
    tokens.append('(EOS)')

    ret = []
    for i in range(0, len(tokens)-n+1):
        ret.append(tokens[i:i+n])
    return ret

if __name__ == '__main__':
    tokens = ['今日', 'は', 'いい', '天気', 'だ' '。']
    print(ngram(tokens))
    print(ngram(tokens, n=3))
