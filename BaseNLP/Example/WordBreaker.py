# -*- coding:utf-8 -*-


from src import Base


if __name__ == "__main__":
    tokens = []
    sentences = "王明，你好，你是谁"

    for item in Base.ConvertText(sentences, True).Terms:
        print item.getValue(), item.getPOS()