# -*- coding:utf-8 -*-


import ExtractKeyword as ek


def ExtractKeyword(text, topK=20):
    keywords = ek.ExtractKeyword(text, topK)
    return keywords