# -*- coding:utf-8 -*-


import wordbreaker
from Base.Term import Term
from Base.Text import Text


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