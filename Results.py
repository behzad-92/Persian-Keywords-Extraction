# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:12:14 2021

@author: behzad
"""

import pandas as pd
from getinput import getdocx,  sentencestopwords
from Statisticalfeatures import ngram1, ngram2, ngram3, lenth, hightfidf1, labelkoli, high, tfidf, tfisf
from Statisticalfeatures import mergetfisf, mergemf, hightfidff1, mergetfisff, mergemff, hightfidfff1
from Statisticalfeatures import mergetfisfff, mergemfff, mostfrequent,tfidff, tfisff, mostfrequentt
from Statisticalfeatures import tfidfff, tfisfff, mostfrequenttt


x=int(input("Enter a number: "))
textx1= getdocx[x]
textx2= sentencestopwords[x]
textx3= ngram1[x]
f1=int(len(textx3)*5/100)
textx3=textx3[:f1]
textx4= ngram2[x]
f2= int(len(textx4)*10/100)
textx4= textx4[:f2]
textx9= ngram3[x]
f9= int(len(textx9)*5/100)
textx9=textx9[:f9]
################ label and make dataframe and excel file ######################### 
def DocNumber(review,v): 
    docnum={}
    for word in review:
        docnum[word]=v
    return docnum

hightfidfnew1= []
for i in range(lenth):
    if i != x:
        hightfidfnew1.append(hightfidf1[i])
lenth1=len(hightfidfnew1)
mergetfidf={}
for t in range(lenth1):
    mergetfidf.update(hightfidfnew1[t])

labelkoli1= []
for i in range(lenth):
    if i !=x:
        labelkoli1.append(labelkoli[i])

tlabel={}
for i in range(lenth1):
    for word in hightfidfnew1[i]:
        if word in labelkoli1[i]:
            tlabel[word]=1
        else:
            tlabel[word]=0
hightfisf11=high(mergetfidf,mergetfisf)
highmostfrequent11=high(mergetfidf,mergemf)
d = mergetfidf
df = pd.DataFrame.from_dict(d, orient="index")
df.insert(1,"tfisfvalue",hightfisf11.values()) 
df.insert(2,"mfvalues",highmostfrequent11.values())
df.insert(3,"label",tlabel.values())
df.columns = ['tfidf', 'tfisfvalue', 'mfvalues','label']

export_excel = df.to_excel (r'path', index = all, header=True) #Don't forget to add '.xlsx' at the end of the path
####### excel for 2 grams ###################################
hightfidffnew1= []
for i in range(lenth):
    if i != x:
        hightfidffnew1.append(hightfidff1[i])
mergetfidff={}
for t in range(lenth1):
    mergetfidff.update(hightfidffnew1[t])


hightfisff11=high(mergetfidff,mergetfisff)
highmostfrequentt11=high(mergetfidff,mergemff)

tlabell={}
for i in range(lenth1):
    for word in hightfidffnew1[i]:
        if word in labelkoli1[i]:
            tlabell[word]=1
        else:
            tlabell[word]=0

dd = mergetfidff
dff = pd.DataFrame.from_dict(dd, orient="index")
dff.insert(1,"tfisfvalue",hightfisff11.values()) 
dff.insert(2,"mfvalues",highmostfrequentt11.values())
dff.insert(3,"label",tlabell.values())
dff.columns = ['tfidf', 'tfisfvalue', 'mfvalues','label']


export_excell = dff.to_excel (r'path', index = all, header=True)
##########################################
hightfidfffnew1= []
for i in range(lenth):
    if i != x:
        hightfidfffnew1.append(hightfidfff1[i])
lenth3=len(hightfidfffnew1)
mergetfidfff={}
for t in range(lenth3):
    mergetfidfff.update(hightfidfffnew1[t])

labelkoli3= []
for i in range(lenth):
    if i !=x:
        labelkoli3.append(labelkoli[i])

tlabel={}
for i in range(lenth3):
    for word in hightfidfffnew1[i]:
        if word in labelkoli3[i]:
            tlabel[word]=1
        else:
            tlabel[word]=0
hightfisfff11=high(mergetfidfff,mergetfisfff)
highmostfrequenttt11=high(mergetfidfff,mergemfff)
d = mergetfidfff
df = pd.DataFrame.from_dict(d, orient="index")
df.insert(1,"tfisfvalue",hightfisfff11.values()) 
df.insert(2,"mfvalues",highmostfrequenttt11.values())
df.insert(3,"label",tlabel.values())
df.columns = ['tfidf', 'tfisfvalue', 'mfvalues','label']

export_excel = df.to_excel (r'path', index = all, header=True)
##########################################
# filenames
excel_names = [r"path", r"path", r'path']
# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)
# write it out
combined.to_excel(r"path", header=False, index=False)
############### data test ############################
#########################
hightfisftest=high(tfidf[x],tfisf[x])
highmostfrequenttest=high(tfidf[x],mostfrequent[x])

hightfisfftest=high(tfidff[x],tfisff[x])
highmostfrequentttest=high(tfidff[x],mostfrequentt[x])

tlabeltest={}
for word in tfidf[x]:
    if word in labelkoli[x]:
        tlabeltest[word]=1
    else:
        tlabeltest[word]=0

d = tfidf[x]
df = pd.DataFrame.from_dict(d, orient="index")
df.insert(1,"tfisfvalue",hightfisftest.values()) 
df.insert(2,"mfvalues",highmostfrequenttest.values())
df.insert(3,"label",tlabeltest.values())
df.columns = ['tfidf', 'tfisfvalue', 'mfvalues','label']


export_excel = df.to_excel (r'path', index = all, header=True)

tlabelltest={}
for word in tfidff[x]:
    if word in labelkoli[x]:
        tlabelltest[word]=1
    else:
        tlabelltest[word]=0

dd = tfidff[x]
dff = pd.DataFrame.from_dict(dd, orient="index")
dff.insert(1,"tfisfvalue",hightfisfftest.values()) 
dff.insert(2,"mfvalues",highmostfrequentttest.values())
dff.insert(3,"label",tlabelltest.values())
dff.columns = ['tfidf', 'tfisfvalue', 'mfvalues','label']

export_excell = dff.to_excel (r'path', index = all, header=True)
#########################
hightfisftesttt=high(tfidfff[x],tfisfff[x])
highmostfrequenttesttt=high(tfidfff[x],mostfrequenttt[x])

tlabeltesttt={}
for word in tfidfff[x]:
    if word in labelkoli[x]:
        tlabeltesttt[word]=1
    else:
        tlabeltesttt[word]=0

d = tfidfff[x]
df = pd.DataFrame.from_dict(d, orient="index")
df.insert(1,"tfisfvalue",hightfisftesttt.values()) 
df.insert(2,"mfvalues",highmostfrequenttesttt.values())
df.insert(3,"label",tlabeltesttt.values())
df.columns = ['tfidf', 'tfisfvalue', 'mfvalues','label']

export_excel = df.to_excel (r'path', index = all, header=True)
############
# filenames
excel_names = [r"path", r"path", r'path']
# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)
# write it out
combined.to_excel(r"path", header=False, index=False)

################################## classifier #################################
from sklearn.metrics import classification_report, confusion_matrix ,accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import seaborn as sns; sns.set()
############## naive baysian ##############################
datatrain = pd.read_excel(r"path")  
datatrain.head()
number1 = LabelEncoder()
datatest = pd.read_excel(r"path")  
datatest.head()
number2 = number1

datatrain['tfidf'] = number1.fit_transform(datatrain['tfidf'])

datatrain['tfisfvalue'] = number1.fit_transform(datatrain['tfisfvalue'])

datatrain['mfvalues'] = number1.fit_transform(datatrain['mfvalues'])

datatrain['label'] = number1.fit_transform(datatrain['label'])

datatest['tfidf'] = number2.fit_transform(datatest['tfidf'])

datatest['tfisfvalue'] = number2.fit_transform(datatest['tfisfvalue'])

datatest['mfvalues'] = number2.fit_transform(datatest['mfvalues'])

datatest['label'] = number2.fit_transform(datatest['label'])

#features = ["tfidf", "tfisfvalue", "mfvalues"]
features = ["mfvalues"]
target = "label"


features_train= datatrain[features]
features_test= datatest[features]
target_train= datatrain[target]
target_test = datatest[target]

model = GaussianNB()
model.fit(features_train, target_train)
model.partial_fit(features_train, target_train)

pred = model.predict(features_test)
accuracy = accuracy_score(target_test, pred)
print(accuracy)
print(confusion_matrix(target_test, pred))  
print(classification_report(target_test, pred))
model.partial_fit(features_train, target_train)
####################################################################
x_test1 = dict(features_test)
ez= features_test.mfvalues.tolist()
ez1= target_test.values.tolist()
y_test1 = datatest['Unnamed: 0'].tolist()
y_pred1 = dict(enumerate(pred.flatten(), 1))
ddd = y_pred1
dfff = pd.DataFrame.from_dict(ddd, orient="index")
dfff.insert(1,"label1",ez1)
dfff.insert(2,"word",y_test1)
dfff.insert(3,"mf",ez)

dfff.columns = ['label', 'label1', 'word','mf']
export_excelll = dfff.to_excel (r'path', index = all, header=True)  
#################################### 1gram ####################
datatrain = pd.read_excel(r"path")  
datatrain.head()
datatrain= datatrain[datatrain.label != 0]
datatrain= datatrain.drop('label', axis=1)

z1=dict(zip(datatrain["word"],datatrain["mf"]))
z2=dict(zip(datatrain["word"],datatrain["label1"]))
stop1=("برا","میکنند","ممکن","میتواند","بسیار","بالا","برای","گفته","برخ","عنو","میباشد","گفته","سایر","جمله","دیگر","نیز","قرار","مانند","شده","وجود","شامل","نظر","تفاو","مورد","بین","استفاده","بررس","پاسخ","زیاد","غیر","داخل","کاه","واحد","کار","تأثیر","کند","گیر","خود","نتایج","افزا","ایجاد","محیط","باید","قابل","ارائه","تعریف","پذیر","تولید","تصم","نیاز","مطالعه","منظور","گونه","مربوط","تأیید","آور","عبارتند","بکارگیر","مشخص","مستق","بنابراین","موضوع","اصل","زیر","شیوه","واقع","درصد","وضع","کننده","همه","گرفته","بیشتر","تلا","لاز","داد","چنین","تأکید","یافته","برابر","واسطه ا","لذا","ویژه","عبار اس","صور","ساز","ساختار","افراد","تغییر","خلاق","نظا","طور","جدید","زمینه","اساس","اهدافاهداف","حال","عمل","دارا","یعن","نتیجه","رشد","نیس","بخش","اهم","بودن","روش","باز","موجود","اگر","انس","اینکه","نوع","اهداف","هدف","عال","تحقیق","رابطه","علم","بر اساس","عوامل","مناسب","فراه","میکند","میشود","سال","نوجو","کودک نوجو","میگوید","نسب","فکر","میشوند","مختلف","فرد","دور","میگیرد","همین","خان","کردن","پیدا","آقا","پیا","میتو","مسائل","بلکه","شناخ","شرایط","خصوص","کمک","ادامه","ن میدهد","پرور","بزرگ","اول","پژوه","تعداد","مراحل","باعث","اثر","تئا","اولیه","طبیع","طبیعی","گروه","اجرا","آزمون","بر رو","میباشند","همچنین","سطوح","سطح","همچنین","بهمنظور","یکدیگر","مسئله","پیشنهاد","تشکیل","فصل","بهعنو مثال","پیشین","یافتن","مبتن بر","مورد نیاز","موجود م","نزدیک","چند","امک","برقرار","هیچ","مجموع","نزدیک","قادر","هر ساز","اعتماد م","م سازمان","همکار","اعضا","روابط","ساز مجاز","ن داد","معن دار","معن","دار","روز","بر کیلوگر","میز","اس بر","مطالب","جنبه","میدهد","گذار","قیم","مثال","خاص","کرده","حاوحاو","نواح","مبتن","دلیل","ابتدا","کوچک","موجب","آمده","بدون","دس آمده","حذف","محل","چرا","علاوه","علاوه بر","اینرو","هریک","ذکر","بوده","تاثیر","مید","متوال","غیره","حاو","طور کل","استفاده قرار","نتایج حاصل","مورد استفاده","ذکر شده","صور گرفته","ارائه شده","شده توسط","مورد بررس","بررس قرار","مورد نظر","نظر گرفته","عنو مثال","صور زیر","نتایج دس","بررس میز","تغییر بر","رو ارائه","رو پیشنهاد","نموده","توسط","آزما","تمام","برا پیشبین","ساخ","مناسب برا","فقط","آنرا","داشته","ساله","یاف","معمول","اندازه","موردمطالعه","فراوان","قطع","بعد","عبار","سوال","فرع","بدس","شرح","برا مثال","شدهاند","کاربر بر","قبل","آنکه","بدس آمده","عامل بر","هنگا","وسایل","همراه","میتوانند","مشکل","چندین","ضمن آنکه","هر کدا","استفاده رو","طول","اشاره","موارد","فعال","م کند","متفاو","آنجا","بیننده","آنچه","پیشنهاد شده","شده برا","ساخته شده","برا هر","تولید شده","تما","چهار","ورود","جمع","امر","ممکن اس","گستر","اولین","مهم","موثر","مفهو","پایین","ایر","هنر ایر","آگاه","بهدا","بهدا ر","قرار گرفتن","کنندگ","گزار","ر تاثیر","ه طور","بین دو","ل چو","گرا","مثل","سؤال","پرداخته","آورده","اطمین","بحث","معمولا","شدن","چگونه","چیز","وارد","موفق","عامل","کردهاند","لاز اس","هر مشتر","هر مشتر","براساس","لاز اس","ازا","مینماید","اینجا","جمعآور","مینمایند","نمود","میپردازد","مییابد","سو دیگر","میپرداز","میگیرند","ارائهشده","میپذیرد","ر ک","حرک","حاک","البته","حسب","بر حسب","بر مبنا","مبنا","تاکنون","لحاظ","خواسته","برا تأمین","نر افزار","بدین","برا ساخ","طریق","فعالیت","هماهنگ","تأکید بر","ساز اس","زیرا","گرف","تقس","بعنو","محدود","تخمین","میانگین","بر قیم","تعیین","معرف","عرضه","ازنظر","نکته","سابقه","حاصل","هر فرد","هر شخص","فاصله بین","رو پایگاه","وسیله","ابزار","شدهاس","کاربر ن","داده میشود","آورده شدهاس","همهجاحاضر","ن دادهاند","حین","خیل","برا بررس","استفاده داده","برا مدیر","قرار گرفته","قرار داده","بسیار زیاد","تجرب","پرس","مال","ضمن","قرار میگیرد","پرسوجو","هر دو","نوشته","آیا بین","نق مهم","آیا","بهعنو","تشخیص","نقطه","فاصله","ترکیب","محاسبه","تصویر","سلام","معنو","مقیاس","عملکرد","ویژگی","ویژگ","فاز","کاربر","تصاویر","استفاده میشود","دول","زندگ","مرد","شخص","بر اثربخش","مدیر","")
z3 = {}  
for key, value in z1.items():
    if len(key) >=3:
        z3[key] = value 

z33={}         
for key, value in z3.items():
    if key in textx3:
        z33[key] = value 
z333={}
for key, value in z33.items():
    if key not in stop1:
        z333[key] = value         


z4={}
for key, value in z2.items():
    if len(key) >=3:
        z4[key] = value 
z44={}
for key, value in z4.items():
    if key in textx3:
        z44[key] = value 
z444={}
for key, value in z44.items():
    if key not in stop1:
        z444[key] = value   

dfff = pd.DataFrame.from_dict(z333, orient="index")
dfff.insert(1,"label",z444.values())

dfff.columns = ['mf','label']
export_excelll = dfff.to_excel (r'path', index = all, header=True)   
####################################################
datatrain = pd.read_excel(r"path")  
datatrain.head()
datatrain= datatrain[datatrain.label != 0]
datatrain= datatrain.drop('label', axis=1)

z1=dict(zip(datatrain["word"],datatrain["mf"]))
z2=dict(zip(datatrain["word"],datatrain["label1"]))
z3 = {}  
for key, value in z1.items():
    if len(key) >=3:
        z3[key] = value 

z33={}         
for key, value in z3.items():
    if key in textx4:
        z33[key] = value 
z333={}
for key, value in z33.items():
    if key not in stop1:
        z333[key] = value         


z4={}
for key, value in z2.items():
    if len(key) >=3:
        z4[key] = value 
z44={}
for key, value in z4.items():
    if key in textx4:
        z44[key] = value 
z444={}
for key, value in z44.items():
    if key not in stop1:
        z444[key] = value   


        
dfff = pd.DataFrame.from_dict(z333, orient="index")
dfff.insert(1,"label",z444.values())

dfff.columns = ['mf','label']
export_excelll = dfff.to_excel (r'path', index = all, header=True)       
##########################################################
datatrain = pd.read_excel(r"path")  
datatrain.head()
datatrain= datatrain[datatrain.label != 0]
datatrain= datatrain.drop('label', axis=1)

z1=dict(zip(datatrain["word"],datatrain["mf"]))
z2=dict(zip(datatrain["word"],datatrain["label1"]))
z3 = {}  
for key, value in z1.items():
    if len(key) >=3:
        z3[key] = value 

z33={}         
for key, value in z3.items():
    if key in textx9:
        z33[key] = value 
z333={}
for key, value in z33.items():
    if key not in stop1:
        z333[key] = value         


z4={}
for key, value in z2.items():
    if len(key) >=3:
        z4[key] = value 
z44={}
for key, value in z4.items():
    if key in textx9:
        z44[key] = value 
z444={}
for key, value in z44.items():
    if key not in stop1:
        z444[key] = value   

        
dfff = pd.DataFrame.from_dict(z333, orient="index")
dfff.insert(1,"label",z444.values())
dfff.columns = ['mf','label']
export_excelll = dfff.to_excel (r'path', index = all, header=True) 
##################################################################################################################
