
#
#Variables
#
# Büyük küçük harfe duyarldıır
# numaralarla başlayamaz
# A-z 9-0 ve _ ile yaza bilirisniz (unutmayın sayı ile başlayamaz)
# bide python kelimeleir olamaz and , if gibi (https://www.w3schools.com/python/python_ref_keywords.asp)

myvar="hello"
my_var="hello"
__myvar="hello"
my23423var="hello"
Myvar="hello"
MYVAR="hello"

print(myvar + " myvar \n" + my_var + " my_var \n" + __myvar + " __myvar \n" + my23423var + " my23423var \n" + Myvar  + " Myvar \n" + MYVAR  + " MYVAR")

#Multi Variables

x, y, z = "How", "Are", "You"
print(x + "\n" + y + "\n" + z )
print(x , y , z)

# All in one 

x = y = z = "Hmm"
print(x + "\n" + y + "\n" + z )
print(x , y , z)

# A pack

vendor = ["Nvidia", "AMD", "INTEL"]
x, y, z = vendor
print(x + "\n" + y + "\n" + z )
print(x , y , z)

# Global Variables
x = 1 # her yede x = 1 olcak eğer başka bir yerde x = 2 yazmas isem 
# bir def'in içinde yaparasak diğer def'lerde çalışmaz bundan dolayı def'lerde aşağıdaki gibi yapmalıyız
def hmm():
    global x 
    x = 1
hmm()

#
#Date types
#
#
# yazı tipine str
# sayılarara int(1,2,3,4), float(1.5,1.8,2.9), complex(karmaşık sayılar[lisede görmüş olmanız gerekiyor zaten])
# sıralama tipleri list, tuple, range
# haritalama tipleri dict
# set tipleri set, frozenset
# Boolean tipi bool
# Binary Tipi bytes, bytearray, memoryview
# yok(hiç) tipi NoneType

# bir tipi öğrnemek
x = 1
y = 1.5
z = 1j
print(type(x))
print(type(y))
print(type(z))
# tipini önden söylemek
x = str(1)
print(type(x))
x = int(1)
print(type(x))

#
#Conditionals
#
#if , elif and else
# hepsi eğer demek if başlangıcataki eğer bundan sonraki eğerler için elif veya else olmalı elif if ile aynı sadece ondan sonra olmak zorunda else ise if ve elif deki eğerler bittikden sonrası için voide düşmemek amacıyla kullanılır
x = 1
if x:
    print("yep")
elif x != 2:
    print("hmm")
else:
    print("!!!")

#
#loop
#
#while or for
while True:
    print("hi")
    break # durdurmak için
x = [ "femboy" , "banana" , "hmm"]
for y in x:
    print(x)
for y in x:
    if y == hmm:
        print(y)
        break # döngüyü kapatmak yoketmek için.


