#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:58:46 2015
@author: msutton1
"""

import pandas as pd
import random as rd




namesList = pd.read_excel('SecretSanta.xlsx', sheetname = 'list')

i=0
usedlist = []
while (i<8):
    rand =  rd.randint(0,7)
    if namesList.couple[i] == namesList.couple[rand] or rand in usedlist:
        continue
    else:
        namesList.recipient[i] = namesList.Recipientlist[rand]
        usedlist.append(rand)
        i=i+1       
print namesList
print usedlist

