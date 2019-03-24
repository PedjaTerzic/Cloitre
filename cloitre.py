'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python cloitre.py
    or if it doesn't work use this one:
        python3 cloitre.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''


from math import *
print("                        ***** CLOITRE *****\n\n\n")
while True:
    n=int(input("Enter the ordinal number n : "))
	
    if n<1:
        print("The ordinal number must be greater than zero")
    else:
    
	
        def lcm(p,q):
            p, q = abs(p), abs(q)
            m = p * q
            if not m: return 0
            while True:
                p %= q
                if not p: return m // q
                q %= p
                if not q: return m // p
			
        b1=2
        mx=2
        k=2
        m=2
        while m<=n:
            b2=b1+lcm(floor(sqrt(k**3)),b1)
            a=b2//b1-1 
            k=k+1
            b1=b2 
            if mx<a:
                mx=a
                m=m+1
    
    
        print("The nth prime number of the form floor(sqrt(k^3)) is : "+str(mx))
    
    try_again = ""
    # Loop until users opts to go again or quit
    while not(try_again == "1") and not(try_again == "0"):
        try_again = input("Press 1 to try again, 0 to exit. ")
        if try_again in ["1", "0"]:
            continue  # a valid entry found
        else:
            print("Invalid input- Press 1 to try again, 0 to exit.") 
    # at this point, try_again must be "0" or "1"
    if try_again == "0":
        break 