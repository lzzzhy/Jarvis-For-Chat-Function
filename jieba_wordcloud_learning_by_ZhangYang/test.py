import os
import re
from os import path

import jieba.posseg as psg
import matplotlib.pyplot as plt
import multidict as multidict
import numpy as np
from PIL import Image
from wordcloud import WordCloud


def getWordWeight(wordflag):
    weight = 1
    # 赋予机构团体名2的权重
    if wordflag == 'nt':
        weight = 2
    # 赋予人名5的权重(排除姓氏)
    elif wordflag in ['nr', 'nr2', 'nrj', 'nrf']:
        weight = 2
    # 赋予英文3的权重(暂时不解决英文词性的问题)
    elif wordflag == 'eng':
        weight = 3
    return weight

# 加载停用词表
with open("stopwords.txt", encoding='utf-8') as f:
    stopwords={}.fromkeys(f.read().split("\n"))

def getFrequencyDict():
    print("[ ]开始生成词频统计词典")
    frequency_dict = {}
    with open('paper.txt') as f:
        for line in f.readlines():
            for word, flag in psg.cut(line):
                # 目前只考虑名词 以及英文单词
                if flag[0] == 'n' or flag == 'en':
                    # 如果是停用词 或者为空字符 或者长度仅为1 忽略
                    if word in stopwords or word==" " or len(word)==1:
                        continue 

                    # print('[ ]{:10} {}'.format(word, flag))

                    old_weight = frequency_dict.get(word, 0)
                    frequency_dict[word] = old_weight + getWordWeight(flag)
    print("[+]词频统计词典生成完成")

    for key in frequency_dict:
        print("{}  {}".format(key, frequency_dict[key]))

    return frequency_dict


def makeImage(frequency_dict):
    map_mask = np.array(Image.open("map.png"))

    wc = WordCloud(background_color="white", max_words=1000, mask=map_mask, font_path='simsun.ttf')
    # generate word cloud
    wc.generate_from_frequencies(frequency_dict)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    makeImage(getFrequencyDict())