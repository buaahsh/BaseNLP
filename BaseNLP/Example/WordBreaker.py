# -*- coding:utf-8 -*-


from src import Base
import src.keywordextractor as ke

if __name__ == "__main__":
    tokens = []
    sentences = "王明，你好，你是谁"
    content = """国际在线消息(记者 丁宁、李宇)：23日，习近平飞抵古巴第二大城市圣地亚哥。除了在巴西的福塔莱萨出席金砖领导人会晤之外，这里是习近平拉美之行唯一到访的首都以外的城市，也将为他此行画上一个颇有特殊含义的句号。

　　圣地亚哥是古巴两次革命和独立战争的起源地，很多人说，这里就是古巴的“井冈山”。而这样一座“英雄城市”，中国领导人还是首次到访。83岁的劳尔主席冒着酷暑陪同习主席全程参观。

　　在何塞·马蒂公墓，在打响了古巴革命第一枪的蒙卡达兵营旧址，在宣布革命胜利的圣地亚哥市政府，劳尔向习近平动情讲述着当年斗争的曲折历程。

　　7·26是古巴起义日，习近平说，很高兴能够在这一特殊纪念日前夕来到这里参观：“往事历历在目，古巴人民是英雄的人民。”习近平指出，中古两党两国都有光荣革命历史，革命先烈是不断激励我们前进的宝贵精神财富。相信古巴人民将会在建设符合本国国情的社会主义道路上不断取得新的更大成就。

　　2011年，时任国家副主席的习近平到访古巴，与劳尔主席进行了长时间的深入交谈，晚宴后劳尔还邀请习近平来到著名的哈瓦那老城中心广场散步，偶遇中国留学生。这段出访中的小插曲令习近平至今记忆犹新。

　　盛夏的圣地亚哥碧空如洗。看到习主席身着白色古巴传统服装——瓜亚维拉衫到访，劳尔说，古巴人民一定会感到很亲切。市政府前的中心广场聚集了不少热情的当地民众。劳尔邀请习近平走进欢呼人群中，两位领导人同大家亲切交谈。"""
    # for item in Base.ConvertText(sentences, True).Terms:
    #     print item.getValue(), item.getPOS()
    text = Base.ConvertText(content, isPOS=True)
    for item in ke.ExtractKeyword(text):
        print item.value, item.score, item.pos