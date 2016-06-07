import itertools

dosya=open("tablo1.txt","r")
baslik=dosya.readline().split(",")
girdi=dosya.readlines(1)
boyut=len(baslik)
for i in girdi:
    for k in i.split(","):
         print k,
print "\n"


for sutun in range(1,boyut+1):
    kombinasyon=list(itertools.combinations(range(0,boyut), sutun))
    maxOne=0
    for komb in kombinasyon :
         maks=0
         for i in girdi:
               test=1
               for k in komb:
                     deger=i.split(",")[k].replace('\n','')
                     if(deger=='0'):
                          test=0
               if test==1:
                     maks=maks+1
         if(maks>maxOne):
               maxOne=maks
               basliklar=komb
                     
    b=""
    for i in basliklar:
          b=b+baslik[i].replace('\n','')
    print("karsilastirilacak sutun sayisi : %s" %sutun)
    print("%s : %s tane 1 var"%(b,maxOne))
    print("")                
        
