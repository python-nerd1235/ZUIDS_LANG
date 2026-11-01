#ZUIDS lang 0.1
#by python-nerd1235

#genrate data
data=[]
for i in range(0,256):
    data.append(i)
print(len(data))

#setup vars
DEBUG=False
off=0
ip=0
error=False
KEYWORDS=["_OFF", "_IN", "_OFFDAT"]
temp=None

#get code
with open(input("filename: "), "r") as f:
    code=f.read().splitlines()

#start main loop
while ip<len(code) and not error:
    op=code[ip]
    if DEBUG:print("Before parceing: "+op)
    #parce kaywords

    if KEYWORDS[2] in op:
        error=True
        print("Exit on bad index")
        #first time useing continue!
        continue
        op=op.replace(KEYWORDS[2], str(data[off]))

    
    if KEYWORDS[0] in op:
        op=op.replace(KEYWORDS[0], str(off))

    
    if KEYWORDS[1] in op:
        while temp==None:
            try:temp=int(input(">"))
            except:print("Not an int.")
        op=op.replace(KEYWORDS[1], str(temp))
        temp=None

    

    if DEBUG:print("After parceing: "+op)
    #run commands
    if op[:6]=="offset":
        try:
            off = int(op[7:]) % 256
        except:
            error=True
            print("offset: error at "+str(ip)+":"+op[7:]+" is not an int")


    elif op[:2]=="if":
        try:
            if eval(op[3:]):
                ip-=5
        except:
            error=True
            print("if: error at "+str(ip)+":"+op[3:]+" not an exp.")


    elif op[:9]=="ExpOffset":
        try:off = eval(op[10:]) % 256
        except:
            error=True
            print("ExpOffset: error at "+str(ip)+":"+op[11:]+" not an exp.")


    elif op[:4]=="!NOP":pass
    else:
        print("error at "+str(ip)+":"+op+" is bad syntax")
    if DEBUG:print(f"offset: {off}, IP: {ip}")
    ip+=1
if not error:
    print("Exit on code end")
