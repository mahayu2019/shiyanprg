#!/usr/bin/env python
# coding=utf-8

# 炸金花

import random

#  生成扑克牌
hs = ['红桃', '黑桃', '梅花', '方片']  # 花色
sz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # 牌的数字
cards = []  # 存放扑克
for i in hs:
    for j in sz:
        card = [i, j]
        cards.append(card)
# print(cards)


players = ['pA', 'pB', 'pC', 'pD', 'pE']
dic_score = {}
for player in players:
    pcards = random.sample(cards, 3)
    t = [pcards[0][1], pcards[1][1], pcards[2][1]]
    t.sort()  # 按花色牌点降序
    for pcard in pcards:  # 除去已发牌
        cards.remove(pcard)
    print(player + '持牌:', pcards[0], pcards[1], pcards[2])  # 显示各玩家持牌
    if t[0] == t[1] == t[2]:
        card_list = '豹子'
        score_coe = 10000
        score = t[0] + t[1] * score_coe + t[2] * score_coe * 10
    elif pcards[0][0] == pcards[1][0] == pcards[2][0]:
        if t[0] + 1 == t[1] and t[1] + 1 == t[2]:
            card_list = '同花顺'
            score_coe = 1339
            score = t[0] + t[1] * score_coe + t[2] * score_coe * 10
        else:
            card_list = '同花'
            score_coe = 376
            score = t[0] + t[1] * score_coe + t[2] * score_coe * 10
    elif t[0] + 1 == t[1] and t[1] + 1 == t[2]:
        card_list = '顺子'
        score_coe = 130
        score = t[0] + t[1] * score_coe + t[2] * score_coe * 10
    elif t[0] == t[1] or t[1] == t[2]:
        card_list = '对子'
        score_coe = 36
        if t[0] == t[1]:
            score = t[0] * score_coe * 10 + t[1] * score_coe + t[2]
        else:
            score = t[0] + t[1] * score_coe + t[2] * score_coe * 10
    else:
        card_list = '单张'
        score_coe = 5
        score = t[0] + t[1] * score_coe + t[2] * score_coe * 10

    print('牌型为: ' + card_list + ' 分数为: ' + str(score))
    dic_score[player] = score
a = zip(dic_score.values(), dic_score.keys())
print('本次胜出的为' + max(a)[1],'牌型为: '+card_list,'得分: '+str(score))

