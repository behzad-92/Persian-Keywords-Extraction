# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:41:24 2021

@author: behzad
"""

from __future__ import unicode_literals
import numpy as np

######################################################################################################################
labelensani1=["مدیر دان","فرهنگ سازمان"]
labelensani4=["داده","اطلاع","تجربه","دان","مدیر دان","انجمن تجربه"]
labelensani8=["خصوص ساز","بهره ور","کارا","اثر بخش","بیمارس"]
labelensani10=["مدیر دان","تسه دان","موانع","راهکار"]
labelensani12=["مدیر دان","فرهنگ سازمان","ساختار سازمان","استراتژ سازمان","اثربخش سازمان"]
labelensani16=["دان","مدیر دانش","عوامل کلید موفق","سیس خبره فاز"]
labelensani17=["کسب و کار کوچک و متوسط","جوایز صادرات","صادر","نواح صنعت"]
labelensani18=["بازاریاب","استراتژیک","موقع رقابت","عملکرد","کار امتیاز متوازن"]
labelensani19=["ساختار سازمان","نوآور","بروکراتیک","آموز عال"]
labelensani24=["چابکی","منطق فاز","زنجیره تأمین","زنجیره تأمین چابک","رویکرد پایگاه قوانین فاز","شاخص چابک فاز"]
labelensani25=["مشابه درمان","هومیوپات","درمان رفتار شناخت","فزون کنش","درمان مکمل","درمان جایگزین","کودک پ دبستان"]
labelensani28=["حکمران خوب","شفاف","حاکم قانون","اجماع محوری","فساد ادار"]
labelensani29=["مسجد","نظا","ساختار نظا مند","بازمهندس فرهنگ","الگو ساز یادگیرنده","سطح صفر","جمهور اسلام ایر"]
labelensani30=["کار امتیاز متوازن","پویایی سیس","مدیر راهبرد","راهبرد","ارزیاب عملکرد","بهبود عملکرد"]

labelensani=[]
labelensani.append(labelensani1)
labelensani.append(labelensani4)
labelensani.append(labelensani8)
labelensani.append(labelensani10)
labelensani.append(labelensani12)
labelensani.append(labelensani16)
labelensani.append(labelensani17)
labelensani.append(labelensani18)
labelensani.append(labelensani19)
labelensani.append(labelensani24)
labelensani.append(labelensani25)
labelensani.append(labelensani28)
labelensani.append(labelensani29)
labelensani.append(labelensani30)

labelkoli=[]
for i in range(len(labelensani)):
    labelkoli.append(labelensani[i])

labelfani0=[ "موتیف", "تطبیق غیردقیق گراف", "زیرگراف غیرالقا","ویژگی طیف گراف","خوشه‌بند","شبکه وزن‌دار برهم‌کن پروتئین",]
labelfani1=["یکپارچه ساز","تکنولوژ شناسا طریق امواج رادیو","تکنیک داده‌کاو","انباره داده"]
labelfani2=[" پرداز زب طبیع","شی‌گرا","برچسب زن","دستور زب وابستگی"]
labelfani3=["حفظ حر خصوص","کاو سودمند","کاو قوانین انجمن","برنامه‌ریز عدد صحیح","الگور مکاشف","الگوریتم تکامل"]
labelfani4=["مواز ساز","گداختگ شبیه ساز شده","مک ده"]
labelfani5=["معمار سرویس‌گرا","شناسا سرویس","مهندس مدل‌رانده","معیار سنج چسبندگ","معیار سنج پیوستگ"]
labelfani6=["خوشه‌بند تصاویر","استخراج ویژگ","بازخورد ربط","تنوع بصر","مرور مؤثر","موتور جستجو تصاویر"]
labelfani7=["توسعه تقریب معنا","پایگاه‌داده رابطه فاز","وابستگ چندمقدار فاز","وابستگ تابع فاز"]
labelfani8=["امن","کاربردپذیر","مجوز","سیس خبره مبتن بر قانون","کنترل دسترس"]
labelfani9=["دادهکاو","خوشهبند","وبکاو","تبلیغ اینترنت","جذاب","رفتار کاربر"]
labelfani10=["وب سرویس","تطبیق خودکار","شباه عملکرد","خصوص کیف و ترجیح کاربر"]
labelfani11=["تجار الکترونیک","عامل","احساس","مذاکره","تصمیمگیر"]
labelfani12=["پرداز تصویر","آشکارساز شئ","مدل زمینه","همپوشان","رهگیر","فیل کالمن"]
labelfani13=["استخراج الگو","الگو ناهنجار","کلاهبردار","خوشهبند","مدل مارکوف پنه","ادغا دستهبند"]
labelfani15=["شبکه حسگر بی‌س","خوشه‌بند","گره ضعیف","وزن‌ده","انرژ باقیمانده","طول عمر شبکه"]
labelfani16=["خوشه‌بند متن","هستان‌شناس فارس‌ن","رفع اب از معان کلمه","تحلیل معنا","فاکتورگیر نامنف ماتریس"]
labelfani17=["سیس تشخیص چهره","شکل","لبه","باف","رنگ","ویول گابور"]
labelfani19=["عامل متحرک","وب سرویس مرکب","یکپارچگ","محرمانگ"]
labelfani20=["راستی‌آزما ز اجرا","سیس سرویس‌گرا","ماشین حال انتزاع","شبکه ناشر/مشترک","سیس الکترونیک سلام","روش رسم"]
labelfani21=["سیستم بازیاب معنا تصاویر","بازخورد ارتباط","شبکه عصب چندلایه","شبکه عصب شعاع‌مدار"]
labelfani22=["خوشه‌بند طیف","انتخاب بردار ویژه","مسئله بهینه‌ساز مقید آمیخته","تبدیل فضا","توصیف زیرخوشه"]
labelfani23=["محاسب نورمبنا","محاسب نامتداول","مسائل ان‌پ کامل","مسائل ان‌پ سخ"]
labelfani24=["تشخیص بیمار سرط","داده توصیف ژن","استخراج قانون","الگور ممتیک","سیس دسته‌بند فاز"]
labelfani25=["بازیاب تصویر بر اساس محتو","رنگ","باف","سیس فاز","یادگیر ماشین"]
labelfani26=["ذخیره‌ساز داده‌محور","شبکه حسگر بیس","جدول درهم‌ساز جغرافیا","مشکل مک داغ"]
labelfani27=["شبکه حسگر بی‌س","مکانیاب","الگور مکانیاب توزیع‌شده","مقیاس‌پذیر چندبعدی"]
labelfani28=["ارزیاب امن","معمار سرویس گرا","چارچوب ارزیاب امن","پایگاه دان امن","مدیر","نظار امن"]
labelfani29=["خوشه‌بند داده","مجموعه داده بزرگ","ویژگی چندگانه","کلون مورچگ","هو ازدحام","داده‌کاو"]
labelfani30=["مسایل تصمیم‌گیر با محدود","زب مدلساز Zinc","روش جستجو","جستجو A*"]
labelfani31=["تصم گیر هندآف","آگاه از زمینه","کیف دریاف کاربر","هندآف مستقل از رسانه"]
labelfani32=["سازمان مجاز","محیط پرور سازمان مجاز","اعتماد","اعتماد گروهمحور","کلون مورچه"]
labelfani33=["پرس‌وجو اولو کاربر","نزدیک همسایه","پرس‌وجو خط افق","پایگاه داده فضا"]
labelfani34=["پایگاه‌داده سیار","کنترل همروند","ترتیب‌ده بر اساس ز نهایی‌شدن","کنترل همروند خوش‌بینانه","کنترل همروند بدبینانه"]
labelfani35=["تبدیل ویول","تسه راز","تسه راز چندگانه","امن"]
labelfani36=["استنتاج در وب معنا","استنتاج مقیاس‌پذیر","استنتاج استقرا","کدگذار داده"]
labelfani37=["تشخیص ناهنجار","سیستم ایمن مصنوع","تئور خطر","تکنولوژ ناظر"]
labelfani38=["آشکارساز تغییر","ثب تصاویر","معیار شباه","اطلاع متقابل محل وزن‏دار","یادگیر نیمه‏نظارت"]
labelfani39=["رو عامل‌گرا","انعطافپذیر","هوشمند","یادگیر","معمار نرم‌افزار"]
labelfani40=["شبکه حسگر بی‌س","خوشه‌بند","الگور مسیریاب ترکیب","کارآمد انرژ","طول عمر شبکه","خوشه‌بند مجدد"]
labelfani41=["پنه ساز در صو","تبدیل گسسته موجک","تبدیل گسسته کسینوس","پیاده ساز سخ افزار","دیوار آت","حق کپ","مالک معنو"]
labelfani43=["حمله رد سرویس لایه کاربرد","نظریه خطر","همبندساز هشدار"]
labelfani44=["رو عامل‌گرا","انعطافپذیر","هوشمند","یادگیر","معمار نرم‌افزار"]
labelfani45=["شبکه حسگر بی‌س","مسیریاب","الگور مورچه","سیس استنتاج فاز"]
labelfani46=["دسته‌بند","درخ تصم","درخ تصم فاز","معیار توقف","گسسته‌ساز"]
labelfani47=["سیستم گسسته رخداد","سیستم تخصیص منابع","کنترل نظارت","مدلساز فرمال","شبکه پتر"]
labelfani48=["بیومتریک","راه رفتن","شناسا افراد","استخراج ویژگ",]
labelfani50=["شبکه‌‎ نرم‌افزار محور","پروتکل اپن‌فلو","تجمیع جداول جریان","الگور فراابتکار ژنتیک"]
labelfani51=["سیستم تصمیمیار بالین","معمار نر افزار","میکروسرویس","پیشبین","پیوند کلیه","شبکه عصب"]



labelfani=[]
labelfani.append(labelfani0)
labelfani.append(labelfani1)
labelfani.append(labelfani2)
labelfani.append(labelfani3)
labelfani.append(labelfani4)
labelfani.append(labelfani5)
labelfani.append(labelfani6)
labelfani.append(labelfani7)
labelfani.append(labelfani8)
labelfani.append(labelfani9)
labelfani.append(labelfani10)
labelfani.append(labelfani11)
labelfani.append(labelfani12)
labelfani.append(labelfani13)
labelfani.append(labelfani15)
labelfani.append(labelfani16)
labelfani.append(labelfani17)
labelfani.append(labelfani19)
labelfani.append(labelfani20)
labelfani.append(labelfani21)
labelfani.append(labelfani22)
labelfani.append(labelfani23)
labelfani.append(labelfani24)
labelfani.append(labelfani25)
labelfani.append(labelfani26)
labelfani.append(labelfani27)
labelfani.append(labelfani28)
labelfani.append(labelfani29)
labelfani.append(labelfani30)
labelfani.append(labelfani31)
labelfani.append(labelfani32)
labelfani.append(labelfani33)
labelfani.append(labelfani34)
labelfani.append(labelfani35)
labelfani.append(labelfani36)
labelfani.append(labelfani37)
labelfani.append(labelfani38)
labelfani.append(labelfani39)
labelfani.append(labelfani40)
labelfani.append(labelfani41)
labelfani.append(labelfani43)
labelfani.append(labelfani44)
labelfani.append(labelfani45)
labelfani.append(labelfani46)
labelfani.append(labelfani47)
labelfani.append(labelfani48)
labelfani.append(labelfani50)
labelfani.append(labelfani51)


for i in range(len(labelfani)):
    labelkoli.append(labelfani[i])





labelhonar0=["رنگ","تاثیر رو","تبلیغ","تجار"]
labelhonar2=["هنر معاصر ایر","گفتمان","نو سنت گرا","دهه","گسس"]
labelhonar3=["فعال هنر","هنر تجسم","پژوه هنر","پژوه"]
labelhonar4=["کودک","سینما","دهه شص","رو شناس","ژ پیاژه"]
labelhonar5=["کلاس هنر","هنر کودک","مدارس ابتدا","واکاو","شیوه تدریس"]
labelhonar6=["تصویرسازی","تکنیکال","اسباب باز","خلاق"]
labelhonar8=["دود کعبه","عاشورا","مقاتل","تئا","درا","ب قرار","روز که به یاد گذ"]
labelhonar10=["منسوج صفو","رو  تزئین","طرح و نق"]
labelhonar11=["هدا بازیگر","پ بروک","شکسپیر","کارگردان تئا تلویزیون","میزانسن"]
labelhonar12=["اروپا","ایران","چندفرهنگ","جهان","طراح لباس","مانتو","زیبا شناس","برند"]
labelhonar13=["درک حضوردیگر","پرسونا نمایش","سوبژکتیو","روا","نیما یوشیج"]
labelhonar14=["کوله‌پشت","ارگونوم","دانش‌آموز","کاربرمحور"]
labelhonar15=["نق برجسته","فنون سنت","صنایع دست","مصالح شناس سنت ایر"]
labelhonar17=["طراح بانک اطلاعات","پا نامه","ارتباط تصویر","تصویرساز","کارشناس ارشد"]
labelhonar18=["خانواده هسته","خانواده گسترده","خانواده","سینمای‌ایر","بازنما"]
labelhonar20=["گف جنسیت","گف قدر","فوکو","عصر صفوی","نقاش دیوار","چهل‌ستون","عالی‌قاپو"]
labelhonar22=["حراج تهر","گروه مرجع قیم","قیمت‌گذار","رهبر قیم"]
labelhonar23=["تایپوگراف متحرک مذهب"," ایر پس از انقلاب اسلام","موشن گرافیک","تایپوگرافی"]
labelhonar24=["کتاب فرهنگ وهنر","تحلیل محتوا","کلاس هفتم","نظا جدید آموزش"]
labelhonar25=["کودک نوجوان","نمایشنامه","شخص","قهر","واقع‌گرا","فانتز","اجتماع"]
labelhonar26=["ستون دوبل","اتصال خم فولاد","رفتار لرزه ا","مدلساز اجزا محدود"]
labelhonar27=["آموزه  مولانا","مکتب تائویس","ایمان","انس کامل","حقیق مطلق","عرف","تصرف"]
labelhonar28=["زاهد","گرافیک محیط","فرهنگ","دان بصری","طراح شهر","زیباساز شهر"]




labelhonar=[]
labelhonar.append(labelhonar0)
labelhonar.append(labelhonar2)
labelhonar.append(labelhonar3)
labelhonar.append(labelhonar4)
labelhonar.append(labelhonar5)
labelhonar.append(labelhonar6)
labelhonar.append(labelhonar8)
labelhonar.append(labelhonar10)
labelhonar.append(labelhonar11)
labelhonar.append(labelhonar12)
labelhonar.append(labelhonar13)
labelhonar.append(labelhonar14)
labelhonar.append(labelhonar15)
labelhonar.append(labelhonar17)
labelhonar.append(labelhonar18)
labelhonar.append(labelhonar20)
labelhonar.append(labelhonar22)
labelhonar.append(labelhonar23)
labelhonar.append(labelhonar24)
labelhonar.append(labelhonar25)
labelhonar.append(labelhonar26)
labelhonar.append(labelhonar27)
labelhonar.append(labelhonar28)


for i in range(len(labelhonar)):
    labelkoli.append(labelhonar[i])



labelpaye0=["غنی‌شدگ","زرشور","تکاب","زمین‌انباشتگ","عناصر سنگین","رسوب آبراهه"]
labelpaye2=["آب زیر‌زمین","د ملایر","رو وزن‌ده تجمع ساده","رو وزن‌ده معکوس فاصله","سیس اطلاع جغرافیا"]
labelpaye3=["آب زیر زمین"\
            ,"نیترات"\
            ,"نیتر","فلوراید"\
            ,"ملایر"\
            ,"زمین آمار"]
labelpaye4=["مدل جعبه","مدل گوس","فلز سنگین","هواویزها","هواشناس آلودگ هوا"]
labelpaye6=["آموز","سرب","سلامت","بهداشت","مادر","مرکز بهدا"]
labelpaye7=["آموز غیررسم","آگاه محیط زیست","تولید ک","استفاده دوباره","بازیاف"]
labelpaye8=["رود کارون","سیس اطلاع جغرافیا","تصویر ماهواره لندس","اثر زیستمحیط","تغییر مسیر","دایره مماس","پیچ رود"]
labelpaye9=["لایه زیست خاک","میکروکولئوس","ریزاندامگ خاک","تسریع بازساز خاک","کنترل کویرزا","بازساز مصنوع خاک"]
labelpaye14=["دان محیط‏زیست","نگر محیط‏زیست","مهار محیط‏زیست","دوره‏ متوسطه","زنج"]
labelpaye15=["متالوتیونین","کیتوس","جذب فلز سنگین","جاذب فلز سنگین","پلیمر","کادمیو"]
labelpaye16=["پروتئین نوترکیب","بهینه ساز توال","همسانه سازی","وسترن بل"]
labelpaye17=["سرط پس","کاوئول","کاوئولین","رونوشت Cav-۲"]
labelpaye18=["اسکله","ارزیاب اثر توسعه","ماتریس ریاض","بهبود نتایج"]
labelpaye19=["اقلید","شاخص زیست","کیف آب","ماکروبنتوز"]
labelpaye20=["آلودگ هوا","رادن","محیط بسته"]
labelpaye21=["بنتون فعال شده","حذف فلز سنگین","کارخانه رو زنج","رو رویه سطح پاسخ"]
labelpaye23=["عصاره هیدروالکل سیاهدانه","تستوسترون","بلوغ"]
labelpaye25=["پارا کیف","نانوچوب","محیط آب","ایزوترم","سینتیک"]
labelpaye26=["تغییر اقلیم","گاز گلخانه","عوامل محرک","کایا","آمار فضا","جهان"]
labelpaye27=["پسماند خطرناک","فرایند سلسله مراتبی","مدل تحلیل شبکه","مکانیاب"]
labelpaye28=["سامانه لجن فعال","تصفیه فاضلاب","آبیار","دانشگاه سبز","زنج","همبستگ","تحلیل مولفه اصل"]
labelpaye29=["گل قرمز","جذب","رنگزا","آلاینده آلومینیوم","متیلن بلو","اریوکرو بلک"]
labelpaye30=["ارزیاب چرخه حیات","مدیر زباله‏ شهر"]
labelpaye32=["دان زیس محیطی","مسئول پذیر اجتماع زیس محیطی","تجرب پیشین زیس محیطی","دان آموز","رفتار صرفه جو انرژ"]
labelpaye34=["پسماند","بیوگاز","انرژ","زباله‌سوز"]
labelpaye36=["ماهواره لندس","آلودگ خاک","پهنه‌بند","شرک مل سرب و روی"]
labelpaye37=["میکرو پلاستیک","آلودگ سواحل","ارزیاب زیست‌محیط","نرخ تجمع","خلیج چابهار"]
labelpaye39=["زخ","عصاره هیدورالکل","تشنه دار","فن تویئن","تتراسایکلین","پلاسبو"]
labelpaye40=["فلز سنگین","غبار هوا","بندرعباس","اندازه گیر"]
labelpaye41=["فاضلاب","بیمارستان","تصفیه خانه","آلودگ"]
labelpaye42=["مدل‌ساز","آلودگ هوا","مدل AERMOD","ذر معلق","کارخانه س"]



labelpaye=[]
labelpaye.append(labelpaye0)
labelpaye.append(labelpaye2)
labelpaye.append(labelpaye3)
labelpaye.append(labelpaye4)
labelpaye.append(labelpaye6)
labelpaye.append(labelpaye7)
labelpaye.append(labelpaye8)
labelpaye.append(labelpaye9)
labelpaye.append(labelpaye14)
labelpaye.append(labelpaye15)
labelpaye.append(labelpaye16)
labelpaye.append(labelpaye17)
labelpaye.append(labelpaye18)
labelpaye.append(labelpaye19)
labelpaye.append(labelpaye20)
labelpaye.append(labelpaye21)
labelpaye.append(labelpaye23)
labelpaye.append(labelpaye25)
labelpaye.append(labelpaye26)
labelpaye.append(labelpaye27)
labelpaye.append(labelpaye28)
labelpaye.append(labelpaye29)
labelpaye.append(labelpaye30)
labelpaye.append(labelpaye32)
labelpaye.append(labelpaye34)
labelpaye.append(labelpaye36)
labelpaye.append(labelpaye37)
labelpaye.append(labelpaye39)
labelpaye.append(labelpaye40)
labelpaye.append(labelpaye41)
labelpaye.append(labelpaye42)

for i in range(len(labelpaye)):
    labelkoli.append(labelpaye[i])



labelpezeshki0=["جوجه گوشت"\
                ,"کل باسیلوز"\
                ,"اشریشیاکل","پلاسمید"\
                ,"حد"]
labelpezeshki1=["هایپرفسفاتم","نیاسین","قند خون"]
labelpezeshki2=["منظومه طب","تاریخ پزشک","طب سنت ایر"]
labelpezeshki3=["بیمار روان","دارالمجانین","تیمارس","دارالفنون"]
labelpezeshki4=["عملکرد اجرا","آسیب ویژه زبان","بازدار پاسخ","حل مسئله","توجه","روان کلام","فارس"]
labelpezeshki5=["مالتیپل مایلوما","پرده آمنیون","ک سل"]
labelpezeshki6=["اپ کندیل خارج","تزریق کورتیکواستروئید","درمان","آرنج","تاندون","عضل"]
labelpezeshki7=["مایع آمنیوتیک","مالتیپل میلوما","پلاسماسل","تکثیر"]
labelpezeshki12=["پا ازراه دور","آزمون خود گزارش‌ده","افسردگ","مدل‌ساز منطق و فیزیک","سامانه روان‌درمان"]
labelpezeshki13=["سردرد گردن","نقاط ماشه","فیزیوتراپ","التراسونوگرافی","سفت","ضریب یانگ"]
labelpezeshki15=["استئوآرتر","اسانس سیاهدانه","سایتوکین"]
labelpezeshki16=["پریودنت مزمن","چا سبز","عمق پاک","ایندکس خون ریز","ایندکس پلاک"]
labelpezeshki17=["ویروس هپات B","پل مورفیس تک نوکلئوتید","هپات مزمن"]
labelpezeshki18=["اختلال خلق دوقطب نوع یک","آریپیپرازول","نقایص شناخت","توجه مستمر","توجه انتخاب","حافظه دیدار","عملکرد اجرا"]
labelpezeshki19=["ناتوان ذهن اتوزوم مغلوب","ماده سفید","لکودیستروفی","لکوآنسفالوپات"]
labelpezeshki20=["استحکا برش پیوند","س  رزین خود باند شونده"]
labelpezeshki21=["کمپیلوباک","کلامیدوفیلا","مایکوپلاسما","سقط","گوسفند بلوچ","رو مولکول"]
labelpezeshki22=["سقط","گوسفند بلوچ","بروسلا مل تنسیس","کوکسیلا بورنت","سالمونلا آبورتوس اویس"]
labelpezeshki23=["سایتوکاین التهاب","سولفورموستارد","مصدومین شیمیا"]
labelpezeshki24=["سندرو درد میوفاشیال","ماساژ فریکشن","شاک ویو"]
labelpezeshki26=["زعفر","سیلورسولفادیازین","سوختگ"]
labelpezeshki28=["لپتوسپیرا","سگ","گاو","سیس","واکن زنجیره پل مراز"]
labelpezeshki32=["سرط پاپیلر تیروئید","پ آگه","اندازه تومور","متاستاز لنفاو","تهاج کپسول"]
labelpezeshki34=["تحلیل محتوا","سلام معنو","سالمند","طراح مقیاس","ابزارساز"]
labelpezeshki36=["سنکوپ","سنکوپ وازوواگال","بلوک قلب","سندر سینوس بیمار"]



labelpezeshki=[]
labelpezeshki.append(labelpezeshki0)
labelpezeshki.append(labelpezeshki1)
labelpezeshki.append(labelpezeshki2)
labelpezeshki.append(labelpezeshki3)
labelpezeshki.append(labelpezeshki4)
labelpezeshki.append(labelpezeshki5)
labelpezeshki.append(labelpezeshki6)
labelpezeshki.append(labelpezeshki7)
labelpezeshki.append(labelpezeshki12)
labelpezeshki.append(labelpezeshki13)
labelpezeshki.append(labelpezeshki15)
labelpezeshki.append(labelpezeshki16)
labelpezeshki.append(labelpezeshki17)
labelpezeshki.append(labelpezeshki18)
labelpezeshki.append(labelpezeshki19)
labelpezeshki.append(labelpezeshki20)
labelpezeshki.append(labelpezeshki21)
labelpezeshki.append(labelpezeshki22)
labelpezeshki.append(labelpezeshki23)
labelpezeshki.append(labelpezeshki24)
labelpezeshki.append(labelpezeshki26)
labelpezeshki.append(labelpezeshki28)
labelpezeshki.append(labelpezeshki32)
labelpezeshki.append(labelpezeshki34)
labelpezeshki.append(labelpezeshki36)

for i in range(len(labelpezeshki)):
    labelkoli.append(labelpezeshki[i])
 
###############################################################################
######## get Data #######################

filePath=list(np.load('datafilePath.npy'))
########### reading fani #####################
filePath1=list(np.load('datafilePath1.npy'))
########### reading honar #####################
filePath2=list(np.load('datafilePath2.npy'))
########### reading paye #####################
filePath3=list(np.load('datafilePath3.npy'))
############ reading pezeshki #####################
filePath4=list(np.load('datafilePath4.npy'))
############## N-Grams ###########################################
######### preprocess ##########################
def ngrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

########################## load data #########################################
getdocx=list(np.load('datagetdocx.npy'))
sentencestopwords=list(np.load('datasentencestopwords.npy')) 