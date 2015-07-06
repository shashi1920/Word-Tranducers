#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import devtoipa
def rule1(word):
    word = re.sub(ur'əbə\s*$', u'əbbe', word)

    return word
def rule2(word):
    word = re.sub(ur"kʂ", u'cʰ', word)
    word = re.sub(ur"ɳ", u'n', word)
    return word
def rule3(word):
    word = re.sub(ur"\s*^i", u'e:', word)
    word = re.sub(ur"əkeː\s+$", u'kərə', word)
    return word
def rule4(word):
    word=re.sub(ur"ɕ",u"s",word)
    word=re.sub(ur"ʂ",u"s",word)

    return word
def rule5(word):
    word=re.sub(ur"^\s*u",u"oː",word)
    return word
def rule6(word):
    word=re.sub(ur"^\s*j",u"ɟ",word)
    return word
def rule7(word):
    word=re.sub(ur"^\s*v",u"b",word)
    return word
def rule8(word):
    word=re.sub(ur"ːrj",u"ːɟ",word)
    return word

inp=raw_input("Input a word : ")
inp=devtoipa.converter(inp)

inp= rule1(inp)

inp= rule2(inp)
inp= rule3(inp)
inp= rule4(inp)
inp= rule5(inp)
inp= rule6(inp)
inp= rule7(inp)
inp= rule8(inp)

print(inp)