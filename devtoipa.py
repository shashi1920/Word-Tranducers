#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from django.contrib.gis.geometry import regex
import re
from uniseg.db import grapheme_cluster_break
from uniseg.graphemecluster import grapheme_cluster_breakables
global arr

arr= {u'क' 	:  'kə' ,
    u'ख' 	:  'kʰə' ,
    u'ग' 	:  'gə' ,
    u'घ' 	:  'gʰə' ,
    u'ङ' 	:  'ŋə' ,
    u'च' 	:  'cə' ,
    u'छ' 	:  'cʰə' ,
    u'ज' 	:  'ɟə' ,
    u'झ' 	:  'ɟʰə' ,
    u'ञ' 	:  'ɲə' ,
    u'ट' 	:  'ʈə' ,
    u'ठ' 	:  'ʈʰə' ,
    u'ड' 	:  'ɖə' ,
    u'ढ' 	:  'ɖʰə' ,
    u'ण' 	:  'ɳə' ,
    u'त' 	:  't̪ə' ,
    u'थ' 	:  't̪ʰə' ,
    u'द' 	:  'd̪ə' ,
    u'ध' 	:  'd̪ʰə' ,
    u'न' 	:  'nə' ,
    u'प' 	:  'pə' ,
    u'फ' 	:  'pʰə' ,
    u'ब' 	:  'bə' ,
    u'भ' 	:  'bʰə' ,
    u'म' 	:  'mə' ,
    u'य' 	:  'jə' ,
    u'र' 	:  'rə' ,
    u'ल' 	:  'lə' ,
    u'व' 	:  'və' ,
    u'श' 	:  'ɕə' ,
    u'ष' 	:  'ʂə' ,
    u'स' 	:  'sə' ,
    u'ह' 	:  'ɦə' ,
    u'क्ष' 	:  'kʃə' ,
    u'त्र' 	:  't̪ɾə' ,
    u'ज्ञ' 	:  'gjə' ,
    u'श्र' 	:  'ɕcə' ,
    u'क़' 	:  'qə' ,
    u'ख़' 	:  'xə' ,
    u'ग़' 	:  'ɣə' ,
    u'ज़' 	:  'zə' ,
    u'फ़' 	:  'fə' ,
    u'ड़' 	:  'ɽə' ,
    u'ड़'	:  'ɽə' ,
    u'ढ़' 	:  'ɽʱə' ,
    u'ढ़'	:  'ɽʱə' ,

    u'ə्'           :  ''  ,     #blank

    u"əा"   :  'ɑː' ,
    u"əि"  : 'i' ,
    u"əी"  :   'iː' ,
    u'əु' :    'u' ,
    u"əू" :     'uː' ,
    u'əृ' :      'ɹ̩' ,
    u"əे":     'eː' ,
    u"əै":      'aːi' ,
    u"əो":    'oː' ,
    u"əौ":  'aːu' ,
    u'əं' :    'ⁿ' ,
    u'əँ' :    'ⁿ' ,
    u'ं' :       'ⁿ' ,
    u'ँ' :        'ⁿ' ,
    u'əः' :     'h' ,


    u'अ' 	:  'ə' ,
    u'आ' 	:  'ɑː' ,
    u'इ' 	:  'i' ,
    u'ई' 	:  'iː' ,
    u'उ' 	:  'u' ,
    u'ऊ' 	:  'uː' ,
    u'ए' 	:  'eː' ,
    u'ऐ' 	:  'aːi' ,
    u'ओ' 	:  'oː' ,
    u'औ' 	:  'aːu' ,

    u'ऋ' 	:  'ɹ̩' ,
    u'ॠ' 	:  'ɹ̩ː' ,
    u'ऌ' 	:  'l̩' ,
    u'ॡ' 	:  'l̩ː' ,

    u'अं' 	:  'ⁿ' ,
    u'अः' 	:  'h' ,
    }
def DEVTOIPA(word):

    global converted
    converted=u""

    l=len(word)

    i=0;
    j=0
    for letter in word:

        if letter in arr:
            converted+=unicode(arr[letter],'utf-8')
        else:
            converted+=letter

    return (converted)

def DEVTOIPA2(word):
    global converted
    converted=u""

    l=len(word)
    i=0
    while i<l:
        if(i+1<l):
            current=word[i]+word[i+1]

            if current in arr:
                converted+=unicode(arr[current],'utf-8')
                i+=1
            else:
                converted+=word[i]
        i+=1
        if(i==l-1):
            converted+=word[l-1]

    return converted
def converter(inp):
    inp=unicode(inp,'utf-8')
    a= (DEVTOIPA(inp))
    return DEVTOIPA2(a)

