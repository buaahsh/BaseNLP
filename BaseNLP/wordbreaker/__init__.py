# -*- coding:utf-8 -*-


import jieba
import jieba.posseg as ps

def wordbreaker(sentence):
    tokens = []
    for item in jieba.cut(sentence, cut_all=False):
        tokens.append(item)
    return tokens

def POStagger(sentence):
    tokens = []
    for item in ps.cut(sentence):
        tokens.append(item)
    return tokens

if __name__ == "__main__":
    for word in POStagger("你好，你是？"):
        print word
