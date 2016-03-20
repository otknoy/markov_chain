#!/usr/bin/env python
import random
from ngram import ngram

class MarkovChain:
    def __init__(self):
        self.chains = {}

    def train(self, tokens):
        bigram = ngram(tokens)

        for s1, s2 in bigram:
            self.chains.setdefault(s1, [])
            self.chains[s1].append(s2)

    def generate(self, bos='(BOS)'):
        tokens = []

        node = random.choice(self.chains[bos])
        while node != '(EOS)':
            tokens.append(node)

            node = random.choice(self.chains[node])

        return ' '.join(tokens)


if __name__ == '__main__':
    import sys
    from tokenizer import tokenize
    from preprocess import normalize

    markov_chain = MarkovChain()

    for line in sys.stdin:
        title = normalize(line.strip())
        tokens = tokenize(title)
        
        markov_chain.train(tokens)

    for i in range(100):
        print(markov_chain.generate())
