#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Belal Edries <edries.belal.95@edu.bme.hu>


def are_anagrams(word1, word2):
    
    dictionary1 = {}
    dictionary2 = {}
    
    for element in word1:
        if element not in dictionary1:
            dictionary1[element]=0
        dictionary1[element] +=1
    
    for element in word2:
        if element not in dictionary2:
            dictionary2[element]=0
        dictionary2[element] +=1

    return dictionary1 == dictionary2

assert(are_anagrams("abc", "bac") == True)
assert(are_anagrams("aabb", "abab") == True)
assert(are_anagrams("abab", "aaab") == False)
