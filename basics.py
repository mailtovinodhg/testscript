#Import module - here the module is datetime
import datetime
x=datetime.datetime.now()
print ('now time is ==> ',x)
x=10
y=49
sum=x+y
print ('sum is ' , sum)
z='vinodh'
a=3.5
#To print what type of datatype
print (type(x), type(z), type(a))

##LIST
student= ['Vinodh','Viji','Sharan']
print (student)
list12 = [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2]
print (list12[1:5])
rainfall = [10.2, 23,'Normal',[1,3]]
print (rainfall[3])

#mysum = sum(list12)
mylen = len(list12)
#myavg = mysum / mylen
print (mylen)

#User "COUNT" function from LIST
print ()
student_grades = [10.0, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
mycount=student_grades.count(10.0)
print ("Count the number of 10.0 from student_grades = " , mycount)

print()

#printing dicitionary keys and values
username = "Python3"
print (username)
abc=username.lower()
print (abc)
fam_mem= {"Vinodh": 33, "Viji": 28, "Sharan": .7}
print (fam_mem.values())
print (fam_mem.keys())


day_temperatures ={"morning":(10.1,11.3,12.4), "noon":(19.8,21.2,24.1), "evening":(16.1,14.3,13.8)}
print (day_temperatures.values())

def lengther(lst):
    num_items=len(lst)
    return num_items


print (lengther([1,2,3,4,5]))


def vc1(volcon):
    volume_converter=volcon*29.57353
    return volume_converter

print ("2 fluid ouncer is equal to ", vc1(2), " milliliter")

def mysqr(mysquare):
    chk_sqr=mysquare*mysquare
    return chk_sqr

print ("Square of 7 is : ", mysqr(7))


def vc(volcon):
    volume_converter=volcon*29.57353
    return round(volume_converter)

print ("3 fluid ouncer is equal to ", vc(3), " milliliter")

x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less or Equal")


#def foo(x, array):
##    if x in array:
#        return True
#    else:
#        return False
 
#print(foo(1, [1, 2, 3]))
#print(foo(1, [2, 3]))
#print(foo(1, ['1', 2, 3]))


def chkpass(cpass):
    if len(cpass) < 8:
        return False
    else:
        return True
    
print (chkpass("vinodhkumar"))

print ("")
def tempchk (tchk):
    if tchk > 25:
        #tempis="Cold"
        return "Hot"
    elif tchk < 15:
        return "Cold"
    else:
        #tempis="Warm"
        return "Warm"

#user_input = input("Enter Tempreature: ")
#print (type(user_input))
#user_input1 = float(user_input)
#print (tempchk(user_input1))
#print (type(user_input1))



name=input ("Enter your name: ")
lastname=input("Enter you lastname: ")
mesg= "Hey %s %s !! How are you doing !!" % (lastname, name)
mesg1= f"Hey {name} {lastname} !! How are you doing !!" 
print (mesg)
print (mesg1)


def ename(name):
    myname=str.title(name)
    return "Hi %s" % myname

chkname=input("Who is this? ")
print (ename(chkname))



mymark=(97, 98, 99, 71, 35)
for tmark in mymark:
    test1=f"This is my mark %s" % tmark
    print (test1)

print ()

colors = [11, 34, 98, 43, 45, 54, 54]
for myc in colors:
    if myc > 50:
        print (myc)

print ()

mycolors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for myco in mycolors:
    if  isinstance(myco, int):
        print (myco)

print ()

usecolor = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for useco in usecolor:
    if  isinstance(useco, int) and useco > 50:
        print (useco)

day_temperatures ={"morning":(10.1,11.3,12.4), "noon":(19.8,21.2,24.1), "evening":(16.1,14.3,13.8)}
for dtemp in day_temperatures.items():
    print (dtemp)

for dtemp in day_temperatures.keys():
    print (dtemp)

for dtemp in day_temperatures.values():
    print (dtemp)

print ()

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

phone_numbers1 = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for valueabc in phone_numbers1.values():
    abc= valueabc.replace( "+", "00")
    print (abc)



temps=[99, 'no data', 95, 94, 'no data']

def temp_func2(number1):
 return [temp for temp in number1 if not isinstance(temp, str)]

print (temp_func2(temps))


temps=[-5, 3, -1, 101, -220, 34]

def temp_func(number1):
 return [temp for temp in number1 if temp > 0]

print (temp_func(temps))


temps=[99, 'no data', 95, 94, 'no data']

def temp_func1(number1):
 return [temp if not isinstance(temp, str) else 0 for temp in number1 ]

print (temp_func1(temps))

tempsa=['1.2', '2.6', '3.3']

def temp_func3(number1):
 return sum([float(temp5) for temp5 in number1 ])

print (temp_func3(tempsa))

def strcon(a, b):
    return a + b 

print (strcon(b="Hi", a="Vinodh"))


def arbiarg(*args):
    return sum(args) / len(args)

print (arbiarg(20,30,21,34,45))


def arbistr(*args):
    args = [x.upper() for x in args]
    return sorted(args)


print (arbistr("snow","glacier","iceberg"))

def arbistra(**kwargs):
    return kwargs


print (arbistra(a="snow",b="glacier",c="iceberg"))


def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=2, b=2, c=5))



###################
## FILE PROCESSING
###################

myfile = open("myfirst_uml_1.wsd")
#print (myfile.read(15))
content=myfile.read()
myfile.close()
#print(content)


def testfile(abc, filepath):
    file=open(filepath)
    conect=file.read()
    return conect.count(abc)

#print (testfile(abc='scale', filepath="myfirst_uml_1.wsd"))

#with open("mpython_notes.txt","r") as myfile1:
 #   rcontent=myfile1.read()

#print(rcontent)

with open("filewrite.txt","w") as myfile1:
    myfile1.write("Hey buddy\nHow are you\n")

myfileabc = open("data.txt")
#print (myfile.read(15))
content=myfileabc.read()
myfileabc.close()
#print (content)

with open("data.txt","a+") as myfilexyz:
    myfilexyz.write('\n' + content + '\n')
    myfilexyz.write(content + '\n')


with open("bear1.txt","a+") as myfilexyz:
    myfilexyz.seek(0)
    mcontent=myfilexyz.read()
    myfilexyz.seek(0)
    myfilexyz.write('\n' + mcontent + '\n')
    myfilexyz.write(mcontent + '\n')



