def keys_values_and_items():
     S={'a':30, 'b':40, 'c':50, 'd':60}
     S.keys()
     for y in S.keys():
           i=print(y)
           P={'a':120, 'b':340, 'c':650, 'd':860}
           P.values()
           for z in P.values():
                 r=print(z)
                 A={'a':30, 'b':40, 'c':50, 'd':60}
                 A.items()
           for t in A.items():
                 print(t)
            
def keys_values_and_items():
     S={1:20, 2:40, 3:50, 4:60, 5:80, 6:100}
     S.keys()
     for y in S.keys():
           print('keys',y)
     P={'a':120, 'b':340, 'c':650, 'd':860, 'e':80, 'f':100}
     P.values()
     for z in P.values():
           print('values',z)
     A={3:30, 4:40, 9:50, 4:60, 7:78}
     A.items()
     for t in A.items():
           print('items',t)
           
def keys_values_and_items():
     S={'a':20, 'b':40, 'c':50, 'd':60}
     S.keys()
     for y in S.keys():
           print('keys',y)
     P={'a':120, 'b':340, 'c':650, 'd':860}
     P.values()
     for z in P.values():
           print('values',z)
     A={'a':30, 'b':40, 'c':50, 'd':60}
     A.items()
     for t in A.items():
           print('items',t)
           
def keys_values_and_items():
     S={'a':30, 'b':40, 'c':50, 'd':60}
     S.keys()
     for y in S.keys():
           print(y)
     P={'a':120, 'b':340, 'c':650, 'd':860}
     P.values()
     for z in P.values():
           print(z)
     A={'a':30, 'b':40, 'c':50, 'd':60}
     A.items()
     for t in A.items():
           print(t)
            
def counting_number():
      list1=[20,20,10,30,40,50,60,70,10,10,40]
      num=eval(input("enter the number:"))
      count=0
      for i in list1:
            if num ==i:
                  count=count+1
                  print(num,"is present" , count, " number of times")

def salute():
      print("enter you name:")
      name=input()
      print("ok"+name)

def reversible():
      str=input("enter the string:")
      for i in range(-1,-len(str)-1,-1):
            print(str[i],end=' ')

def main():
      a=[50,45,56,19,37,48,56,90,6,7,2,4,3,2,34,4,21,333,66,3,55,32,]
      print("original  list : ",a)
      for i in a:
           j=a.index(i)
           while j>0:
                if a [j-1] > a[j]:
                     a[j-1] ,a[j] = a[j],a[j-1]
                else:
                     break
                j=j-1
      print("list after unsortingsorting : " , a)

def main1():
      a=[50,45,56,19,37,48,56,90,6,7,2,4,3,2,34,4,21,333,66,3,55,32,]
      print("original  list : ",a)
      for i in a:
           j=a.index(i)
           while j>0:
                if a [j-1] > a[j]:
                     a[j-1] ,a[j] = a[j],a[j-1]
                else:
                     break
                j=j-1
      print("list after  sorted  : " , a)
      
def created():
     p=tuple()
     n=int(input("enter the  number of element :"))
     i=1
     while(i>=n):
          a=input("enter the number:")
          i=i+1
     print("tuple created  as:")
     print(i)

def created2():
     p=tuple()
     n=int(input("enter the  number of element :"))
     i=1
     while(i<=n):
          a=input("enter the number:")
          i=i-1
     print("tuple created  as:")
     print(i)

def marks():
     a=int(input("enter the S_NO.:"))
     b=int(input("enter the  Roll no.:" ))
     c=int(input("enter the name:"))
     d=int(input("enter the marks:"))
     print('a','b','c','d')
     for i in range (0,len('a','b','c','d')):
          print((i+'a'),'\t','a','b','c','d'[i][0],'\t','a','b','c','d'[i][1],'\t','a','b','c','d'[i][2])
          
def reverseorder():
     tup= (10,20,30,40,50,60,70,80,90,100)
     print("original tuple is:")
     for i in range(0,len(tup)):
                    print(tup[i])
     print("tuple elements in reverse order:")
     for i in range(len(tup)-1,-1,-1):
            print(tup[i])        
                    
def reverseorder2():
     tup= ('rudra','amit','sonu','brijesh','manish','raja','shubham')
     print("original tuple is:")
     for i in range(0,len(tup)):
                    print(tup[i])
     print("tuple elements in reverse order:")
     for i in range(len(tup)-1,-1,-1):
            print(tup[i])        
                    
   
def  countingthenumber():
     print("enter the numbers  seprated by comma:")
     t1=tuple([int(e) for e in  input().split(',')])
     i=0
     for e in t1:
          if i ==t1.index(e):
               print(e, '  - ',t1.count(e))
          i+=1

def information():
     D={'Name':"Rudra pratap",'Gender':'Male','DOB':'20-10-2009'}
     print(D)
     D_Name=D.setdefault('Name',"Name not Available:")
     D_DOB=D.setdefault('DOB',"Date not Available")
     D_Gender=D.setdefault('Gend')
     D_Mobile=D.setdefault('Mobile')
     print("Name:",D_Name)
     print("DOB:",D_DOB)
     print("Gender:",D_Gender)
     print("Mobile:",D_Mobile)

def employe():
     D1=str(input("enter the name:"))
     D2=str(input("enter the phone number:"))
     D3=str(input("enter the address:"))
     print("Name:",D1)
     print("phone number:",D2)
     print("address:",D3)
     
 
def employe2():
     D={"sonu":9534721166,"rudra":8506837992,"amit":9818525709,"manish":7011189922,"shubham":8076794458}
     print(D)
     D1=str(input("enter the name:"))
     D2=str(input("enter the phone number:"))
     D3=str(input("enter the address:"))
     print("Name:",D1,D)
     print("phone number:",D2,D)
     print("address:",D3,D)
     
''' 
print("This program is made to create and edit various lists and then create a masterlist out of them ")
c='y'
y=1
Masterlist = []
while c=='y' or c=='Y':
    print("For List",y," : ")
    x=input("Enter the name of your list : \n")
    w=[]
    c1='y'
    while c1=='y' or c1=='Y':
        print("MAIN MENU","If you want to add an element type E or e",
                     "If your list is complete type C or c (NOTE: You cannot further change you list)",
                     "If you want to delete an element type D or d", sep = '\n')
        z=input()
        if z=='E' or z=='e' :
            k='y'
            while  k=='Y' or k=='y':
                o=eval(input('Enter the Element you want to add to your list [Note: is str use quotes]'))
                w.append(o)
                print("The list",x," is \n",w,)
                k=input("Do you want to add another element to your list (Y/N) \n")
        elif z=='C' or z=='c':
            c1='n'
        elif z=='d' or 'D':
            k='y'
            while k=='Y' or k=='y':
                i=eval(input("Enter the element you want to remove from your list"))
                if i in w :
                    w.remove(i)
                else :
                    print("You entered an Element not in your list")
                k=input("Do you want to delete another element from your list (Y/N) \n")
    Masterlist.append(w)
    print("Your List",x," is : \n",w,)
    print("Your Masterlist is : \n",Masterlist)
    y+=1
    c=input("Do you want to add another list to your masterlist (Y/N) \n")
print("The Master List is : ",Masterlist,) '''


def time():
     T=int(input("enter the time:"))
     for T in range(T-1):
          print(T)
          
def time2():
     T=int(input("enter the time:"))
     for T in range(T-1,T):
               print(T)
               

def multiply():
     R=int(input("enter the number:"))
     for n in range(R):
          print(n*100)

def sum():
     sum=0
     n=int(input("How many terms:"))
     for a in range(2,n+2):
          term=0
          for b in range(1,a):
               term+=b
          print('term',(a-1),':',term)
          sum+=term
     print('sum of',n,'term is:',sum)      
               
     
def sum2():
     sum=0
     n=int(input("How many terms:"))
     for a in range(-123,n-1):
          term=0
          for b in range(-1,a):
               term+=b
          print('term',(a-1),':',term)
          sum+=term
     print('sum of',n,'term is:',sum)      
               


def sor():
     for i in range(1,4):
          for j in range(1,i+1):
               print(j,end=' ')
          print(j)     





