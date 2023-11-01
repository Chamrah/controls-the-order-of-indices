#Program that controls the order of indices passed as arguments and asks the user if they want to enter a new list
#Function that returns an array with the values of the boxes between the two indexes
def sub_array(T,a,b):
    Tab = []
    for i in range(a,b):
        Tab.append(T[i])
    return Tab

while True:
  Tab = []
  for i in range(10):
    print(f"Enter the element number {i+1} : ")
    x = float(input())
    Tab.append(x)
  a = int(input("Enter the first index :"))
  b = int(input("Enter the second index :"))
  print(sub_array(Tab,a,b))
  choice=input("Do you want repeat another array ? (Enter Y for yes and N for no) :")
#The check of the user if he wishes to enter a new list  
  if(choice!="Y" and choice!="y"):
   break