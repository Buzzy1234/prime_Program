import math
import time
def prime(a,b):
 ar=[]
 print("\n----")
 for x in range(a,b+1):
  
    
    
       if x>1:
    
            if x==2:
               print(f"{x} is prime")
               print("-----------")
               ar.append("-")
               time.sleep(0.1)
               continue
         
        
            elif x%2==0:
                #print("{} isn't a prime".format(x))
                #print("----")
                continue 
       
       
            for y in range(3,1+math.floor(math.sqrt(x)),2):
               if x%y==0:
                  #print("{} isn't a prime".format(x))
                  #print("----")
                  break
                  
     
     
            else:
        
               print("{} is a prime".format(x)) 
               print("-----------")
               ar.append("-")
               continue 
         
         
         
         
         
         
         
       '''elif x<0:
          
              print("not defined for {}".format(x))
              print("----")
              continue 
      
                
        
        
        
        
        
       else:
          
              print("{} isn't a prime".format(x))
              print("----")
              time.sleep(0.1)'''
    


 if a==b:
   print("\n\n")
   if len(ar)==1:
     print("----")
     print("You have found a prime!!")
     print("-----\n\n\n\n")
   return None
   
 lenght=len(ar)
 print("\n\n----------------------- \n")
 time.sleep(3) 
 displaylenght="so, there are {} primes on intervals:[{},{}]"
 print(displaylenght.format(lenght,a,b))
 print("\n----------------------- \n") 
 print("-----------------------------\n\n\n\n")
 
















def primality_test():
  try:
     
     print("\n------------------------------ \n\n\n")
     print("----")
     print("PRIMALITY TEST") 
     print("-----\n\n")
     
 
     print("----\n")
     print("number/range?:")
     print("\n----")
     
     print("\n----")
     inp=input("")
     print("-------\n\n\n")
     
     
     
   
     if inp.lower()=="number":
              print("----")
              print("The number:")
              print("----")
              num=input("")
              print("------")
              num=int(num) 
              prime(num,num)
              
 
     elif inp.lower()=="range":
       
       
              print("----")
              print("lowerbound: ")
              
              print("----")
              l=input("")
              print("----{0}{0}".format("\n"))
              
              
              print("----")
              print("upperbound: ")
              
              print("----")
              u=input("")
              print("----{0}{0}{0}".format("\n"))
              
              
              l=int(l)
              u=int(u)
              
              
              if l<u:                      
                  prime(l,u) 
                  
                  
              else:
                  print("\ninvalid\n\n\n")
                  
              
     else:
              print("\ninvalid\n\n\n")
     

  except Exception as re:
     print("\ninvalid\n\n\n")
     print(re)
     print()

  
    
   
   
   
   
true0=True 

print("-----------------------")
print("Initiate?:")
print("-------------------------")

inp0=input("")

print("----\n\n\n")
     
 
if inp0.lower() != "yes":
         print("\n\n---")
         print("Exiting..")
         print("-----\n")
         
         true0 = False
         
         

while true0:
 
 
 
 primality_test()
 
 
 
 print("----------------------- \n")
 print("Restart the program?:")
 print("\n-----------------------\n")
 print("----")
 inp2=input("").lower()
 print("------\n")
 
 
 if inp2 != "yes":
              print("\n---")
              print("Exiting..")
              print("-----\n")
          
              true0 = False
   