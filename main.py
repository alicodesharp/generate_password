import time
import random
ASALMI = False


def asal_mı(sayi):
  sayac = 0
  bolunebildigi_degerler = []
  for i in range(2,sayi):
    if sayi%i==0:
      sayac+=1
      bolunebildigi_degerler.append(i)
  if not sayac>0:
    return True
  else:
    return False


def ekle(derinlik):#default harf = none
  random_harfler = "abcdefghijklmnopqrstuvwxyzşçöğü"
  #random_rakamlar= range(1,1000)
  random_simgeler = "`~!@#$%^&*()-_=+[]\{}|;':,./<>?"
  passwordd = ""
  if derinlik>0:
    sayitut = random.randint(0,len(random_harfler)-1)
    sayitut2 = random.randint(1,999)
    sayitut3 = random.randint(0,len(random_simgeler)-1)
    for i in range(2):
      if asal_mı(sayitut2):
        passwordd += random_harfler[sayitut]
        passwordd +=str(sayitut2)
        passwordd += random_simgeler[sayitut3]
        
      else:
        passwordd+= ekle(derinlik-1)

  return passwordd
  

def password_olustur():
    random_harfler = "abcdefghijklmnopqrstuvwxyzşçöğü"
    random_simgeler = "`~!@#$%^&*()-_=+[]\{}|;':,./<>?"
    len1 = random.randint(len(random_harfler)-1)
    len2 = random.randint(len(random_simgeler)-1)
    password = ""
    for i in range(15):
        ix = random.randint(0,219)
        while asal_mı(ix):
          password+=random_harfler[len1]
          password+=str(ix)
          password+=random_simgeler[len2]
          ix = random.randint(0,219)
          len1 = random.randint(len(random_harfler)-1)
          len2 = random.randint(len(random_simgeler)-1)

    

    x = time.localtime()
    print ("Date :")
    print (x.tm_year,"/", x.tm_mon,"/",x.tm_mday)
    print ("Hour :")
    print ((x.tm_hour+3)%12,":",x.tm_min,":",x.tm_sec)
    print ("Şifreniz : "+"'"+password+"'")

    return password


