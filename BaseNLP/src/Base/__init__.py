# -*- coding:utf-8 -*-


import src.wordbreaker as wordbreaker
from src.Base.Term import Term
from src.Base.Text import Text

def ConvertText(sentence, isPOS=False):
    if not isPOS:
        termList = []
        for index, word in enumerate(wordbreaker.wordbreaker(sentence)):
            term = Term(word)
            term.setIndex(index)
            termList.append(term)
        text = Text(sentence, termList)
        return text
    else:
        termList = []
        for index, w in enumerate(wordbreaker.POStagger(sentence)):
            term = Term(w.word)
            term.setPOS(w.flag)
            term.setIndex(index)
            termList.append(term)
        text = Text(sentence, termList)
        return text


if __name__ == "__main__":
    tokens = []
    sentences = "你好，你是谁"

    for item in ConvertText(sentences).Terms:
        print item.getValue()