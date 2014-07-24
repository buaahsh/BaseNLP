# -*- coding:utf-8 -*-


import sentencebreaker as sb


def sentencebreaker(sentences):
    sentenceList = sb.split(sentences)
    return sentenceList

if __name__ == "__main__":
    print sentencebreaker("你好，你是？")