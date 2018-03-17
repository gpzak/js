def dodawanie(x,y):
	return x+y

def odejmowanie(x,y):
	return x-y
	
def mnozenie(x,y):
	return x*y
	
def dzielenie(x,y):
	return x/y
	
x=float(input("Pierwsza liczba: "))
y=float(input("Druga liczba: "))

print("Wybór działania")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
print()
dz=input("Numer działania: ")

if(dz=="1"):
	print(x," + ",y," = ",dodawanie(x,y))
elif(dz=="2"):
	print(x," - ",y," = ",odejmowanie(x,y))
elif(dz=="3"):
	print(x," * ",y," = ",mnozenie(x,y))
elif(dz=="4"):
	if(y!=0):
		print(x," / ",y," = ",dzielenie(x,y))
	else:
		print("Nie można wykonać dzielenia przez 0")
else:
	print("Nie wybrano działania")
input()	