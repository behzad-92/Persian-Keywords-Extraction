# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:36:10 2021

@author: behzad
"""
from __future__ import unicode_literals
import numpy as np
import math
from collections import Counter 
from getinput import getdocx,  sentencestopwords, ngrams, labelkoli


lenth=len(getdocx)

ngram1=[]
for i in range(lenth):
    ngram1.append([' '.join(x) for x in ngrams(sentencestopwords[i], 1)])
####################################################################
################# tf-idf ####################
############ Tf ################################
def computeReviewTFDict(review):

    #Counts the number of times the word appears in review
    reviewTFDict = {}
    for word in review:
        if word in reviewTFDict:
            reviewTFDict[word] += 1
        else:
            reviewTFDict[word] = 1
    #Computes tf for each word           
    for word in reviewTFDict:
        reviewTFDict[word] = reviewTFDict[word] / len(review)
    return reviewTFDict

nametf=[]
for h in range(lenth):
    nametf.append(computeReviewTFDict(ngram1[h]))
######################################
####### new way #################################
def dfCount(review):
    DF = {}
    for i in range(len(review)):
        tokens = review[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}
    for i in DF:
        DF[i]= len(DF[i])
    return DF
idfkoli=dfCount(ngram1)
idfcounttest=[]
def devide(review):
    z1={}
    for word in idfkoli:
        if word in review:
            z1[word] = idfkoli[word]
    return z1

idfcounttest=[]
for i in range(lenth):
    idfcounttest.append(devide(nametf[i]))

#####################################################
def computeIDFDict(review):
    idfDict = {}
    for word in review:
        idfDict[word] = math.log(lenth / review[word])
    return idfDict

idfDict=[]
for q in range(lenth):
    idfDict.append(computeIDFDict(idfcounttest[q]))
tfid=[]
for i in range(lenth):
    tfid.append(np.multiply(list(idfDict[i].values()),list(nametf[i].values())))
z=[]
for o in range(lenth):
    z.append(list(idfcounttest[o].keys()))

tfidf=[]
for i in range(lenth):
    tfidf.append(dict(zip(z[i], tfid[i])))
########### shomarande ######################################
shomarande1=[]
for i in range(lenth):
    shomarande1.append(len(tfidf[i]))
##########################################################
tcounter=[]
for t in range(lenth):
    tcounter.append(Counter(tfidf[t])) 
  
### Finding 5 highest values ####
hightfidf=[]
for s in range(lenth):
    hightfidf.append(tcounter[s].most_common(50))
    
hightfidf1=[]
for i in range(lenth):
    hightfidf1.append(dict(hightfidf[i]))
############ Finding tfidf highest values##################
##########################################
def tfkoli(review1,review2):
    klo={}
    for word in review1:
        if word in review2:
            klo[word]=review2[word]
    return klo
tfidfkoli1=[]
for i in range(lenth):
    tfidfkoli1.append(tfkoli(labelkoli[i],tfidf[i]))

for i in range(lenth):
    hightfidf1[i].update(tfidfkoli1[i])
#################################################
mergetfidf={}
for t in range(lenth):
    mergetfidf.update(hightfidf1[t])
##############################################    
####### most frequent ########################
def computeMostFrequent(review):
 
    mostfrequent = {}
    # Run through each review's tf dictionary and increment countDict's (word, doc) pair
    for word in review:
            if word in mostfrequent:
                mostfrequent[word] += 1
            else:
                mostfrequent[word] = 1
     
    return mostfrequent 
mostfrequent=[]
for y in range(lenth):
    mostfrequent.append(computeMostFrequent(ngram1[y]))  
############################# merge mf #####################
mergemf={}
for t in range(lenth):
    mergemf.update(mostfrequent[t])
########### compare hightfidf and most frequent ############
def high(review1,review2):
    mf={}
    for word in review1:
        if word in review2:
            mf[word]=review2[word]
        else:
            mf[word]=0
     
    return mf

highmostfrequent11=high(mergetfidf,mergemf)   
############# tf_isf #################################
def df1Count(review):
    DF = {}
    for i in range(len(review)):
        tokens = review[i]
        for w in tokens:
            try:
                DF[w] += 1
            except:
                DF[w] = 1
    return DF
isfkoli=df1Count(ngram1)
def devideisf(review):
    z6={}
    for word in isfkoli:
        if word in review:
            z6[word] = isfkoli[word]
    return z6
isfcounttest=[]
for i in range(lenth):
    isfcounttest.append(devideisf(nametf[i]))
###############################################################################
def computeISFDict(review):
    isfDict = {}
    for word in review:
        isfDict[word] = math.log(lenth / review[word])
    return isfDict

isfDict=[]
for q in range(lenth):
    isfDict.append(computeISFDict(isfcounttest[q]))
tfis=[]
for i in range(lenth):
    tfis.append(np.multiply(list(isfDict[i].values()),list(nametf[i].values())))
z=[]
for o in range(lenth):
    z.append(list(isfcounttest[o].keys()))

tfisf=[]
for i in range(lenth):
    tfisf.append(dict(zip(z[i], tfis[i])))      
################ merge tfisf ##################################
mergetfisf={}
for t in range(lenth):
    mergetfisf.update(tfisf[t])
############# compare3 hightfidf and hightfisf ################
hightfisf11=high(mergetfidf,mergetfisf)   
######################################################
#################### 2ngram ##########################
ngram2=[]
for i in range(lenth):
    ngram2.append([' '.join(x) for x in ngrams(sentencestopwords[i], 2)])
nametff=[]
for h in range(lenth):
    nametff.append(computeReviewTFDict(ngram2[h]))
########################################
####### new way #################################
idfkolii=dfCount(ngram2)
def devide1(review):
    z1={}
    for word in idfkolii:
        if word in review:
            z1[word] = idfkolii[word]
    return z1

idfcounttestt=[]
for i in range(lenth):
    idfcounttestt.append(devide1(nametff[i]))

#####################################################
idfDictt=[]
for q in range(lenth):
    idfDictt.append(computeIDFDict(idfcounttestt[q]))
tfidd=[]
for i in range(lenth):
    tfidd.append(np.multiply(list(idfDictt[i].values()),list(nametff[i].values())))
z=[]
for o in range(lenth):
    z.append(list(idfcounttestt[o].keys()))

tfidff=[]
for i in range(lenth):
    tfidff.append(dict(zip(z[i], tfidd[i])))
########### shomarande ######################################
shomarande2=[]
for i in range(lenth):
    shomarande2.append(len(tfidff[i]))
############## Finding 5 tfidf highest values##################
tcounterr=[]
for t in range(lenth):
    tcounterr.append(Counter(tfidff[t])) 
  
# Finding 5 highest values 
hightfidff=[]
for s in range(lenth):
    hightfidff.append(tcounterr[s].most_common(50))  

hightfidff1=[]
for i in range(lenth):
    hightfidff1.append(dict(hightfidff[i]))
##################################################
tfidfkoli2=[]
for i in range(lenth):
    tfidfkoli2.append(tfkoli(labelkoli[i],tfidff[i]))

for i in range(lenth):
    hightfidff1[i].update(tfidfkoli2[i])     
######## merge tfidf 2gram #########################
mergetfidff={}
for t in range(lenth):
    mergetfidff.update(hightfidff1[t])
###############################################
######## most frequent ######################## 
mostfrequentt=[]
for y in range(lenth):
    mostfrequentt.append(computeMostFrequent(ngram2[y]))
############################## merge mf #####################
mergemff={}
for t in range(lenth):
    mergemff.update(mostfrequentt[t])
########### compare hightfidf and most frequent ############
highmostfrequentt11=high(mergetfidff,mergemff)   
############## tf_isf #################################
############# tf_isf #################################
isfkolii=df1Count(ngram2)
def devideisf1(review):
    z6={}
    for word in isfkolii:
        if word in review:
            z6[word] = isfkolii[word]
    return z6
isfcounttestt=[]
for i in range(lenth):
    isfcounttestt.append(devideisf1(nametff[i]))
###############################################################################
isfDictt=[]
for q in range(lenth):
    isfDictt.append(computeISFDict(isfcounttestt[q]))
tfiss=[]
for i in range(lenth):
    tfiss.append(np.multiply(list(isfDictt[i].values()),list(nametff[i].values())))
z=[]
for o in range(lenth):
    z.append(list(isfcounttestt[o].keys()))

tfisff=[]
for i in range(lenth):
    tfisff.append(dict(zip(z[i], tfiss[i])))    
################ merge tfisf ##################################
mergetfisff={}
for t in range(lenth):
    mergetfisff.update(tfisff[t])  
############# compare3 hightfidf and hightfisf ################
hightfisff11=high(mergetfidff,mergetfisff)
###############################################################################
######## 3 Grams #############################
ngram3=[]
for i in range(lenth):
    ngram3.append([' '.join(x) for x in ngrams(sentencestopwords[i], 3)])
################### tf-idf ####################################################
############# Tf ################################
nametfff=[]
for h in range(lenth):
    nametfff.append(computeReviewTFDict(ngram3[h]))
#######################################
############countDict##################
####### new way #################################
idfkoliii=dfCount(ngram3)
def devide2(review):
    z1={}
    for word in idfkoliii:
        if word in review:
            z1[word] = idfkoliii[word]
    return z1

idfcounttesttt=[]
for i in range(lenth):
    idfcounttesttt.append(devide2(nametfff[i]))
#####################################################
idfDicttt=[]
for q in range(lenth):
    idfDicttt.append(computeIDFDict(idfcounttesttt[q]))
tfiddd=[]
for i in range(lenth):
    tfiddd.append(np.multiply(list(idfDicttt[i].values()),list(nametfff[i].values())))
z=[]
for o in range(lenth):
    z.append(list(idfcounttesttt[o].keys()))

tfidfff=[]
for i in range(lenth):
    tfidfff.append(dict(zip(z[i], tfiddd[i])))
########### shomarande ######################################
shomarande3=[]
for i in range(lenth):
    shomarande3.append(len(tfidfff[i]))
######################################
tcounterrr=[]
for t in range(lenth):
    tcounterrr.append(Counter(tfidfff[t])) 
  
### Finding 5 highest values 
hightfidfff=[]
for s in range(lenth):
    hightfidfff.append(tcounterrr[s].most_common(50))
    
hightfidfff1=[]
for i in range(lenth):
    hightfidfff1.append(dict(hightfidfff[i]))
############# Finding tfidf highest values##################
###########################################
tfidfkoli3=[]
for i in range(lenth):
    tfidfkoli3.append(tfkoli(labelkoli[i],tfidfff[i]))

for i in range(lenth):
    hightfidfff1[i].update(tfidfkoli3[i])
##################################################
mergetfidfff={}
for t in range(lenth):
    mergetfidfff.update(hightfidfff1[t])
###############################################    
######## most frequent ########################
mostfrequenttt=[]
for y in range(lenth):
    mostfrequenttt.append(computeMostFrequent(ngram3[y]))   
############################## merge mf #####################
mergemfff={}
for t in range(lenth):
    mergemfff.update(mostfrequenttt[t])
############ compare hightfidf and most frequent ############
highmostfrequenttt11=high(mergetfidfff,mergemfff)
############# tf_isf #################################
############# tf_isf #################################
isfkoliii=df1Count(ngram3)
def devideisf2(review):
    z6={}
    for word in isfkoliii:
        if word in review:
            z6[word] = isfkoliii[word]
    return z6
isfcounttesttt=[]
for i in range(lenth):
    isfcounttesttt.append(devideisf2(nametfff[i]))
###############################################################################
isfDicttt=[]
for q in range(lenth):
    isfDicttt.append(computeISFDict(isfcounttesttt[q]))
tfisss=[]
for i in range(lenth):
    tfisss.append(np.multiply(list(isfDicttt[i].values()),list(nametfff[i].values())))
z=[]
for o in range(lenth):
    z.append(list(isfcounttesttt[o].keys()))

tfisfff=[]
for i in range(lenth):
    tfisfff.append(dict(zip(z[i], tfisss[i])))   
################ merge tfisf ##################################
mergetfisfff={}
for t in range(lenth):
    mergetfisfff.update(tfisfff[t])
############# compare3 hightfidf and hightfisf ################
hightfisfff11=high(mergetfidfff,mergetfisfff)