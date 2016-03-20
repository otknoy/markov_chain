#!/usr/bin/env python
import unicodedata

def normalize(s):
    return unicodedata.normalize('NFKC', s)

if __name__ == '__main__':
    print(normalize('ﾌｶﾞホゲ-%*@AＢＣ−％＊＠１２3'))
