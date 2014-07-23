# -*- coding:utf-8 -*-


def split(sentences):

    """
    chinese sentence breaker based rule (http://www.zdic.net/appendix/f3.htm)
    :param sentences:
    :return: sentence list(unicode)
    """

    fullstop = (u"。", u"！", u"？", u"；")
    quote = (u"”", u"’", u"）")
    ellipsis = u"…"

    sentencesList = []

    if not sentences:
        return None

    sentences = sentences.replace("\t", "").replace("\n", "").replace("\r", "")
    sentences = sentences.decode("utf-8")

    preIndex = 0

    for index, word in enumerate(sentences):
        if word in fullstop:
            if index + 1 < len(sentences):
                if sentences[index+1] in quote:
                    continue
            preSen = sentences[preIndex:index+1]
            preIndex = index+1
            sentencesList.append(preSen)
            continue
        if word in quote:
            if index + 1 < len(sentences):
                if sentences[index+1] in fullstop:
                    continue
            preSen = sentences[preIndex:index+1]
            preIndex = index+1
            sentencesList.append(preSen)
            continue
        if word == ellipsis:
            if index + 1 < len(sentences):
                if sentences[index+1] == ellipsis:
                    continue
            preSen = sentences[preIndex:index+1]
            preIndex = index+1
            sentencesList.append(preSen)
            continue
        if index == len(sentences)-1:
            preSen = sentences[preIndex:index+1]
            sentencesList.append(preSen)
    return sentencesList

if __name__ == "__main__":
    for item in  split("用这个仪器前必须至少热身10-15分钟，等身体发热、血液流通后再用，否则你会感觉腹部发痒。"
                       "关于有效性，个人亲身体验：和其他方式减肥一个道理，坚持最重要，如果坚持不了再好的方法、再贵的＂减肥神器＂都没用。"
                       "如果每天能坚持使用短期内效果还是有的，但一段时间不用后还是会反弹。"):
        print item