#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    info = (len(sentence), sentence[0])
    return info
