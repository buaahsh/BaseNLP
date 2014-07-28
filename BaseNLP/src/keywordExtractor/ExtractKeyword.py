# -*- coding:utf-8 -*-


import os


_curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) )  )
f_name = os.path.join(_curpath,"idf.txt")
content = open(f_name,'rb').read().decode('utf-8')

idf_freq = {}
lines = content.split('\n')
for line in lines:
    word,freq = line.split(' ')
    idf_freq[word] = float(freq)

median_idf = sorted(idf_freq.values())[len(idf_freq)/2]
stop_words= set([
""
])

pos_weight = {"": 1.0, "w": 0.0, "en": 0.0, "num": 0.6, "nr": 2.0, "nrf": 2.0, "nw": 2.0,
            "nt": 2.0, "l": 0.8, "a": 1.2, "nz": 2.0, "v": 1.8, "nrfg":2.0, "ns":2.0, "n":2.0}

class Keyword():

    def __init__(self, value, pos, freq, score):
        self.value = value
        self.pos = pos
        self.score = score
        self.freq = freq
        self.idf = 0.0

def ExtractKeyword(text, topK=20):
    words = text.Terms
    tm = {} #{string:keyword}
    total = float(len(words))
    for w in words:
        value = w.getValue()
        pos = w.getPOS()
        if len(value.strip())<2: continue
        # if w.lower() in stop_words: continue
        if value  not in tm:
            tm[value] = Keyword(value, pos, 0.0, 0.0)
        tm[value].freq = tm[value].freq + 1.0 / total
        # tm[value].freq = tm.get(value, Keyword(value, pos, 0.0, 0.0)).freq + 1.0 / total

    # compute the score
    for item in tm:
        value = tm[item].value
        tm[item].idf = idf_freq.get(value,median_idf)
        tm[item].score = tm[item].freq * tm[item].idf
        tm[item].score *= pos_weight.get(tm[item].pos, 1.0)


    tm = sorted(tm.iteritems(), key=lambda tm:tm[1].score, reverse=True)

    topKeyword= [item[1] for item in tm[:topK]]

    return topKeyword
