###
### Author: Simran Sall
### Course: CSc 110
### Description: This program evaluates the performance levels of different CPUs.
###              There are three input values that will determine the level of
###              performance for the CPU: gigahertz, core_count, and hyperthreading.
###              Depending on the numbers inputted for each value, the program will
###              give an output that defines what level of performance the CPU is at.
###              This was primarily created using if and elif statements, but also
###              features boolean values.


gigahertz = float(input("Enter CPU gigahertz: \n"))
core_count = int(input("Enter CPU core count: \n"))
hyperthreading = (input("Enter CPU hyperthreading (True or False):\n"))

if core_count >= 20:
    print("\nThat is a high-performance CPU.")
    #a CPU core count that is greater than 20 is automatically considered
    #to be high-performance and does not rely on hyperthreading
elif hyperthreading == "True": #conditions for if hyperthreading is true
    if gigahertz >=2.7 and core_count >=6:
        print("\nThat is a high-performance CPU.")
    elif gigahertz >= 2.4 and core_count >= 4:
        print("\nThat is a medium-performance CPU.")
    elif gigahertz >= 1.9 and core_count >= 2:
        print("\nThat is a low-performance CPU.")
    else: #this is if gigahertz is < 1.9 and core_count < 2
        print("\nThat CPU could use an upgrade.")
else: #conditions for if hyperthreading is false
    if gigahertz >= 3.2 and core_count >= 8:
        print("\nThat is a high-performance CPU.")
    elif gigahertz >= 2.8 and core_count >= 6:
        print("\nThat is a medium-performance CPU.")
    elif gigahertz >= 2.4 and core_count >= 2:
        print("\nThat is a low-performance CPU.")
    else: #this is if gigahertz is < 2.4 and core_count < 2
        print("\nThat CPU could use an upgrade.")