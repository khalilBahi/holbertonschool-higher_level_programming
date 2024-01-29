#!/usr/bin/python3
def multiple_returns(sentence):
    lenth = len(sentence)
    if not sentence:
        return (lenth, None)
    return (lenth, sentence[0])
