#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import re


class Lunar(object):
    def __init__(self):
        self.skyname = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        self.landname = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        self.godname = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    # #you must give a str like '2000'#
    # #return a sexagenary cycle#
    # #!!!!only AD!!!#

    def cycle(self, date):
        if  not isinstance(date, str):
            raise Exception('plase give a str like "2000"')
        sky = self.skyname[(int(date)-1984)%10]
        land = self.landname[(int(date)-1984)%12]
        god = self.godname[(int(date)-1984)%12]
        return '%s%s%s'% (sky, land, god)



l=Lunar()
print l.cycle('1883')