#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
def IPATODEV(word):
    arr={'क्ष्' 	:  u'kʃ' ,
    'त्र्'   	:  u't̪ɾ' ,
    'ज्ञ्' 	:  u'gj' ,
    'श्र्' 	:  u'ɕc' ,
    'ह्व्'     :  u'ʍ' ,

    'क़्' 	:  u'q' ,
    'ख़्' 	:  u'x' ,
    'ग़्' 	:  u'ɣ' ,
    'ज़्' 	:  u'z' ,
    'फ़्' 	:  u'f' ,
    'ड़्'  	:  u'ɽ' ,
    'ढ़्' 	    :  u'ɽʱ' ,

    'ख्' 	:  u'kʰ' ,
    'क्' 	:  u'k' ,
    'घ्' 	:  u'gʰ' ,
    'ग्' 	:  u'g' ,
    'ङ्'  	:  u'ŋ' ,
    'छ्' 	:  u'cʰ' ,
    'च्' 	:  u'c' ,
    'च्' 	:  u'tʃ' ,
    'झ्' 	:  u'ɟʰ' ,
    'ज्' 	:  u'ɟ' ,
    'ज्' 	:  u'dʒ' ,
    'ज्' 	:  u'ʒ' ,
    'ञ्' 	:  u'ɲ' ,
    'ठ्' 	    :  u'ʈʰ' ,
    'ट्'   	:  u'ʈ' ,
    'ढ्'  	:  u'ɖʰ' ,
    'ड्' 	    :  u'ɖ' ,
    'ण्' 	:  u'ɳ' ,
    'थ्' 	:  u't̪ʰ' ,
    'थ्' 	:  u'θ' ,

    'त्'  	:  u't̪' ,
    'ट्'   	:  u't' ,
    'ध्' 	:  u'd̪ʰ' ,
    'द्'  	:  u'd̪' ,
    'ड्' 	    :  u'd' ,
    'द्'  	:  u'ð' ,
    'न्' 	:  u'n' ,
    'फ्' 	:  u'pʰ' ,
    'प्'  	:  u'p' ,
    'भ्' 	:  u'bʰ' ,
    'ब्'  	:  u'b' ,
    'म्' 	:  u'm' ,
    'य्' 	:  u'j' ,
    'र्'  	:  u'r' ,
    'ल्' 	:  u'l' ,
    'व्' 	    :  u'v' ,
    'व्' 	    :  u'w' ,
    'श्' 	:  u'ɕ' ,
    'श्' 	:  u'ʃ' ,
    'ष्' 	    :  u'ʂ' ,
    'स्' 	:  u's' ,
    'ह्'   	:  u'ɦ' ,

    ''      :  u'्ə'  ,     # blank
    ''      :  u'्ʌ'  ,

    "ा" :    u'्ɑː' ,
    'ा' :     u'्ɔː' ,
    'ॉ'   :   u'्ɒ' ,
    "ी"  :  u'्iː' ,
    'ि' :     u'्i' ,
    'ि' :     u'्ɪ' ,
    "ू" :     u'्uː' ,
    'ु' :      u'्u' ,
    'ु' :      u'्ʊ' ,
    'ृ' :      u'्ɹ̩' ,
    "े" :      u'्eː' ,  #long e
    "े" :      u'्eɪ' ,  #long e
    "े" :      u'्ɛ'  ,  #short e
    "ै" :     u'्aːi' ,
    "ै":      u'्æ'  ,
    "ो":      u'्oː' ,
    "ो":      u'्oʊ' ,
    "ौ":      u'्aːu' ,
    'ं' :      u'्ⁿ' ,
    'ः' :      u'्h' ,

    'अ'     :  u'ʌ'  ,
    'आ' 	:  u'ɑː' ,
    'आ'  :     u'ɔː'  ,
    'ऑ'  :     u'ɒ'  ,
    'ई'  	:  u'iː' ,
    'ऊ' 	:  u'uː' ,
    'ऐ' 	    :  u'aːi' ,
    'ऐ'     :  u'æ'  ,
    'ए' 	    :  u'eː' ,
    'ए' 	    :  u'eɪ' ,  #long e
    'ए' 	    :  u'ɛ'  ,
    'औ' 	:  u'aːu' ,
    'ओ' 	:  u'oː' ,
    'ओ'     :  u'oʊ' ,
    'अ' 	:  u'ə' ,
    'इ' 	    :  u'i' ,
    'इ' 	    :  u'ɪ' ,
    'उ'   	:  u'u' ,
    'उ'   	:  u'ʊ' ,

    'ॠ' 	:  u'ɹ̩ː' ,
    'ऋ' 	:  u'ɹ̩' ,
    'ॡ' 	:  u'l̩ː' ,
    'ऌ' 	:  u'l̩' ,

    'अं' 	:  u'ⁿ' ,
    'अः' 	:  u'h' }
    global flag
    flag=0
    global converted
    converted=""
    global cat
    cat=""
    arr2=dict((value,key) for key,value in arr.iteritems())

    n=len(word)
    global temp
    temp=""
    i=0
    print(word)
    while i<n:
        print word[i]
        if(i+3<n):
            temp=word[i]+word[i+1]+word[i+2]+word[i+3]
            if temp in arr2:
                converted+= (arr2[temp])
                i=i+4
                flag=1
                continue
        if(i+2<n):
            temp=word[i]+word[i+1]+word[i+2]
            if temp in arr2:
                converted+= (arr2[temp])
                i=i+3
                flag=1
                continue
        if(i+1<n):
            temp=word[i]+word[i+1]
            if temp in arr2:
                converted+=(arr2[temp])
                i=i+2
                flag=1
                continue
        if(i<n):
            temp=word[i]
            if temp in arr2:
                converted+=arr2[temp]
                i=i+1
                flag=1
                continue
        if not flag:
            i=i+1
        flag=0
    for letter in word:
        print(letter)
    return converted
print(IPATODEV(u"t̪əbbe"))