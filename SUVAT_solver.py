#Original SUVAT equations
#v = u + at
#s = 0.5(u+v)*t
#v^2 = u^2 + 2a*s
#s = ut + 0.5at^2
from cmath import sqrt

def suvatSolver():
    #this will keep track of how many variables are known, since three are required.
    variableCount = 0
    [sKnown,uKnown,vKnown,aKnown,tKnown] = [False,False,False,False,False]
    
    s = raw_input("Do you know distance? If so, what is it (in metres)? If not, write 'n'.")
    #this assumes that the input is actually a number. then it says the variable is known and adds 1 to the variable count.
    if s != "n":
        sKnown = True
        s = float(s)
        variableCount += 1
    
    u = raw_input("Do you know initial velocity? If so, what is it (in metres/second)? If not, write 'n'.")
    if u != "n":
        uKnown = True
        u = float(u)
        variableCount += 1
    
    while variableCount < 1:
        v = raw_input("Do you know final velocity? If so, what is it (in metres/second)? If not, write 'n'.")
        if v != "n":
            vKnown = True
            v = float(v)
            variableCount += 1
        else:
            print "You have not given enough variables so far."
        
    while variableCount < 2:
        a = raw_input("Do you know acceleration? If so, what is it (in metres/second^2)? If not, write 'n'.")
        if a != "n":
            aKnown = True
            a = float(a)
            variableCount += 1
        else: 
            print "You have not given enough variables so far."

    while variableCount < 3:
        t = raw_input("Do you know time? If so, what is it (in seconds)? If not, write 'n'.")
        if t != "n":
            tKnown = True
            t = float(t)
            variableCount += 1
        elif t <= 0:
            print "You cannot have negative or zero time."
        else:
            print "You have not given enough variables so far."
            
    #this next bunch of statements pretty much goes through all possible combinations of three variables and calculates the remaining unknowns (I solved the equations myself)
    if sKnown and uKnown and vKnown:
        a = (v**2-u**2) / (2 * s)
        t = 2 * s / (u + v)
        print ""
        print "Acceleration =",a
        print "Time =",t
        print "For s =",s,", u =",u," & v =",v
        
    elif sKnown and uKnown and aKnown:
        v = sqrt(u**2 + 2 * a * s)
        t1 = -u / a + sqrt(2 * a * s + u**2) / a
        t2 = -u / a - sqrt(2 * a * s + u**2) / a
        print ""
        print "Final velocity =",v, "or ",-v
        print "Time =",t1," or",t2
        print "For s =",s,", u =",u," & a =",a
        
    elif sKnown and uKnown and tKnown:
        v = 2 * s / t - u
        a = 2 * (s - u * t) / t**2
        print ""
        print "Final velocity =",v
        print "Acceleration =",a
        print "For s =",s,", u =",u," & t =",t
        
    elif sKnown and vKnown and aKnown:
        u = sqrt(v**2 - 2 * a * s)
        t1 = 2 * s / (v + sqrt(v**2 - 2 * a * s))
        t2 = 2 * s / (v - sqrt(v**2 - 2 * a * s))
        print ""
        print "Initial velocity =",u,"or",-u
        print "Time =",t1,"or",t2
        print "For s =",s,", v =",v," & a =",a
        
    elif sKnown and vKnown and tKnown:
        u = 2 * s / t - v
        a = (v - u) / t
        print ""
        print "Initial velocity =",u
        print "Acceleration =",a
        print "For s =",s,", v =",v," & t =",t
        
    elif sKnown and aKnown and tKnown:
        u = (s - 0.5 * a * t**2) / t
        v = u + a * t
        print ""
        print "Initial velocity =",u
        print "Final velocity =",v
        print "For s =",s,", a =",a," & t =",t
        
    elif uKnown and vKnown and aKnown:
        s = (v**2 - u**2) / (2 * a)   
        t = (v - u) / a
        print ""
        print "Distance =",s
        print "Time =",t
        print "For u =",u,", v =",v," & a =",a
        
    elif uKnown and vKnown and tKnown:
        s = 0.5 * (u+v) * t
        a = (v - u) / t
        print ""
        print "Distance =",s
        print "Acceleration =",a
        print "For u =",u,", v =",v," & t =",t
        
    elif uKnown and aKnown and tKnown:
        v = u + a * t
        s = u * t + 0.5 * a * t**2
        print ""
        print "Final velocity =",v
        print "Distance =",s
        print "For u =",u,", a =",a," & t =",t
        
    elif vKnown and aKnown and tKnown:
        u = v - a * t
        s = 0.5 * (2 * v - a * t) * t
        print ""
        print "Initial velocity =",u
        print "Distance =",s
        print "For v =",v,", a =",a," & t =",t
        
    print "If you see any values with anything but '0j', these are imaginary numbers and so the values you provided cannot possibly be real."
    print ""
    print ""

while True:  
    suvatSolver()
    
