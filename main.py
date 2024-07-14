import pickle
print("                           ###WELCOME TO INDIAN TOURISM###                       ")
print("                     !!!Wanna TRAVEL around the SOUTH INDIA!!!                   ")

print("\n\n")
print("Top south Indian states to visit\n")
print("1.Tamil Nadu\n2.Karnataka\n3.Telangana\n4.Andhra Pradesh\n5.Kerala\n")
c=int(input("Enter your choice of place to visit:"))

if c==1:
    f=open("tn.txt","r")
    x=f.read()
    f.close()
    print("\n",x)   
elif c==2:
    f=open("kt.txt","r")
    x=f.read()
    f.close()
    print("\n",x)
elif c==3:
    f=open("ts.txt","r")
    x=f.read()
    f.close()
    print("\n",x)
elif c==4:
    f=open("ka.txt","r")
    x=f.read()
    f.close()
    print("\n",x)
elif c==5:
    f=open("ap.txt","r")
    x=f.read()
    f.close()
    print("\n",x)
else:
    pass

print("### No. of days ###\n")
print("PACKAGES:\n1.5days & 4nights\tPrice:Rs:25,000 per head\n2.8days & 7nights\tPrice:Rs:35,000 per head\n3.12days & 11nights\tPrice:Rs:45,000 per head\n")
b=int(input("Enter the type of package you want to choose:"))

print("Boarding places:\n1.Hyderabad\n2.Chennai\n3.Bombay\n4.Banglore\n5.Delhi\n")
s=input("Choose the station where you want to board the transport:")

if c=='Tamil Nadu':
    print("Departure at",s,"and Destination is Chennai:")  
elif c=='Karnataka':
    print("Departure at",s,"and Destination is Banglore:") 
elif c=='Telangana':
    print("Departure at",s,"and Destination is Hyderabad:") 
elif c=='Kerala':
    print("Departure at",s,"and Destination is Trivandrum:") 
elif c=='Andhra Pradesh':
    print("Departure at",s,"and Destination is Vijayawada:") 
else:
    pass

print("\n\n$$$ MODE OF TRANSPORT $$$")
print("Different modes of transport:\n1.Car Rs:5000 per head\n2.Train Rs:3000 per head\n3.Bus Rs:2000 per head\n4.Flight Rs:10,000\n")
y=int(input("Enter your choice of mode of transport:"))
    
print("\n\n***Details of the passengers***")

n=int(input("Enter the no. of passengers:"))
d={}
for i in range (n):
    x=input("Name:")
    t=[]
    s=int(input("Age:"));t.append(s)
    g=input("Gender:");t.append(g)
    d[x]=tuple(t)

f=open("Details","wb")
pickle.dump(d,f)
f.close()

f=open("Details","rb")
a=pickle.load(f)
f.close()

print("*------*Your Details*------*")
print(a)


amount=0;ap=0;mp=0

if b==1:
    ap+=n*25000
elif b==2:
    ap+=n*35000
elif b==3:
    ap+=n*45000
else:
    pass

print("Amount to be paid for package:Rs.",ap)

if y==1:
    mp+=n*5000
elif y==2:
    mp+=n*3000
elif y==3:
    mp+=n*2000
elif y==4:
    mp+=n*10000
else:
    pass
print("Amount to be paid for transport:Rs.",mp)

print("Total bill:Rs.",ap+mp)

print("------@#$*Have a wonderful vacation*$#@------")
print("THANK YOU")


    
