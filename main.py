
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
def globalx():
    global x 
    x = 1
globalx()