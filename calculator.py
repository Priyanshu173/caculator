import re
print ("MY MAGICAL CALCULATOR")
prev =0
run = True
def perform():
    global run
    global prev
    equation = ""
    if prev == 0:
        equation = input("enter equation:")
    else:
        equation = input(str(prev))

        
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if prev == 0:
            prev = eval(equation)
        else:
            prev = eval(str(prev)+ equation)
        print(prev)
        
while run:
    perform()
