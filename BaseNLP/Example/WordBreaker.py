# -*- coding:utf-8 -*-


import wordbreaker


if __name__ == "__main__":
    tokens = []
    sentences = "你好，你是谁"

    for item in wordbreaker.wordbreaker(sentences):
        print item