#!/usr/bin/env python
def term_frequecy(terms):
    tf = {}

    for t in terms:
        tf.setdefault(t, 0)
        tf[t] += 1

    return tf

if __name__ == '__main__':
    import sys
    from tokenizer import tokenize
    from preprocess import normalize

    tokens = []
    for line in sys.stdin:
        line = normalize(line.strip())
        tokens.extend(tokenize(line, only_noun=True))

    tf = term_frequecy(tokens)

    for t, f in sorted(tf.items(), key=lambda x: -x[1]):
        print(t, f)
    # for t, f in tf.items():
    #     print(t, f)

