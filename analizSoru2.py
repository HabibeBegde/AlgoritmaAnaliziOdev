dosya=open("tablo1.txt","r")
baslik=dosya.readline().split(",")
girdi=dosya.readlines(1)
boyut=len(baslik)
for i in girdi:
     for k in i.split(","):
         print k,
print "\n"

"""for j in range(0,boyut):
    for i in girdi:
        print i.split(",")[j].replace('\n',''), """

maxOne=0
for j in range(0,boyut):
    maxOne1=0
    for i in girdi:
        deger=i.split(",")[j].replace('\n','')
        if(deger=="1"):
            maxOne1=maxOne1+1
    if(maxOne1>maxOne):
        maxOne=maxOne1
        indis=j
print ("en fazla 1 olan sutun %s ve 1'lerin sayisi:%s" %(baslik[indis],maxOne))

maxOne=0
for k in range (0,boyut-1):
    for j in range(k+1,boyut):
      maxOne1=0
      for i in girdi:
         degerj=i.split(",")[j].replace('\n','')
         degerk=i.split(",")[k].replace('\n','')
        
         if(degerj=="1" and degerk=="1"):
            maxOne1=maxOne1+1
      if(maxOne1>maxOne):
        maxOne=maxOne1
        indisj=j
        indisk=k
print ("en fazla 1 olan ikili sutunlar %s  %s ve 1'lerin sayisi:%s" %(baslik[indisj],baslik[indisk],maxOne))


maxOne=0
for l in range (0,boyut-2):
    for k in range (l+1,boyut-1):
        for j in range(k+1,boyut):
            maxOne1=0
            for i in girdi:
               degerj=i.split(",")[j].replace('\n','')
               degerk=i.split(",")[k].replace('\n','')
               degerl=i.split(",")[l].replace('\n','')
        
               if(degerj=="1" and degerk=="1" and degerl=="1"):
                     maxOne1=maxOne1+1
        if(maxOne1>maxOne):
           maxOne=maxOne1
           indisj=j
           indisk=k
           indisl=l
print ("en fazla 1 olan uclu sutunlar %s %s %s ve 1'lerin sayisi:%s" %(baslik[indisl],baslik[indisk],baslik[indisj],maxOne))

    






