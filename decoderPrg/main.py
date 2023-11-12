from machine import Pin
import time


oc3 = machine.Pin(1, machine.Pin.IN)
oc2 = machine.Pin(2, machine.Pin.IN)
oc1 = machine.Pin(3, machine.Pin.IN)
oc0 = machine.Pin(4, machine.Pin.IN)

ol3 = machine.Pin(5, machine.Pin.IN)
ol2 = machine.Pin(6, machine.Pin.IN)
ol1 = machine.Pin(7, machine.Pin.IN)
ol0 = machine.Pin(8, machine.Pin.IN)

zf = machine.Pin(9, machine.Pin.IN)
of = machine.Pin(10, machine.Pin.IN)
sf = machine.Pin(11, machine.Pin.IN)

sela2 = machine.Pin(14, machine.Pin.OUT)
sela1 = machine.Pin(13, machine.Pin.OUT)
sela0 = machine.Pin(12, machine.Pin.OUT)
selb2 = machine.Pin(17, machine.Pin.OUT)
selb1 = machine.Pin(16, machine.Pin.OUT)
selb0 = machine.Pin(15, machine.Pin.OUT)

ld0 = machine.Pin(18, machine.Pin.OUT)
ld1 = machine.Pin(19, machine.Pin.OUT)
ld2 = machine.Pin(20, machine.Pin.OUT)
ld3 = machine.Pin(21, machine.Pin.OUT)
ldo = machine.Pin(22, machine.Pin.OUT)
ldpc = machine.Pin(26, machine.Pin.OUT)

pm = machine.Pin(27, machine.Pin.OUT)
al = machine.Pin(28, machine.Pin.OUT)

oc = [0, 0, 0, 0]
ol = [0, 0, 0, 0]
flag = [0, 0, 0]

selector = [0, 0, 0, 0, 0, 0]
Load = [1, 1, 1, 1, 1, 1]


alithm = [0, 0]




mov1 = [0, 0, 1, 0]
mov2 = [0, 0, 1, 1]
add1 = [0, 1, 0, 0]
add2 = [0, 1, 0, 1]
sub1 = [0, 1, 1, 0]
sub2 = [0, 1, 1, 1]
nan1 = [1, 0, 0, 0]
nan2 = [1, 0, 0, 1]

jmp =  [0, 0, 0, 1]
jno =  [1, 0, 1, 1]
jze =  [1, 0, 1, 0]
jmi =  [1, 1, 0, 0]
jpl =  [1, 1, 0, 1]
inp =  [1, 1, 1, 0]
outp = [1, 1, 1, 1]
nop =  [0, 0, 0, 0]



def decoder (opeland):
    ret = [1, 1, 1, 1, 1, 1]
    
    if(opeland[0] == 0 and opeland[1] == 0):
        ret[0] = 0
        
    if(opeland[0] == 0 and opeland[1] == 1):
        ret[1] = 0
        
    if(opeland[0] == 1 and opeland[1] == 0):
        ret[2] = 0

    if(opeland[0] == 1 and opeland[1] == 1):
        ret[3] = 0
    
    return ret

while True:
    oc[0] = oc3.value()
    oc[1] = oc2.value()
    oc[2] = oc1.value()
    oc[3] = oc0.value()

    ol[0] = ol3.value()
    ol[1] = ol2.value()
    ol[2] = ol1.value()
    ol[3] = ol0.value()

    flag[0] = zf.value()
    flag[1] = of.value()
    flag[2] = sf.value()

    
    if oc == mov1:
        selector = [0, ol[2], ol[3], 1, 1, 0]
        Load = decoder(ol)
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("mov1")
        
    if oc == mov2:
        selector = [1, 0, 1, 1, 1, 0]
        Load = decoder(ol)
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("mov2")
        
    if oc == add1:
        selector = [0, ol[0], ol[1], 0, ol[2], ol[3]]
        Load = decoder(ol)
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("add1")
        
    if oc == add2:
        selector = [0, ol[0], ol[1], 1, 0, 1]
        Load = decoder(ol)
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("add2")
        
    if oc == sub1:
        selector = [0, ol[0], ol[1], 0, ol[2], ol[3]]
        Load = decoder(ol)
        alithm = [1, 0]
        print(oc)
        print(ol)
        print(flag)
        print("sub1")
        
    if oc == sub2:
        selector = [0, ol[0], ol[1], 1, 0, 1]
        Load = decoder(ol)
        alithm = [1, 0]
        print(oc)
        print(ol)
        print(flag)
        print("sub2")
        
    if oc == nan1:
        selector = [0, ol[0], ol[1], 0, ol[2], ol[3]]
        Load = decoder(ol)
        alithm = [0, 1]
        print(oc)
        print(ol)
        print(flag)
        print("nan1")
        
    if oc == nan2:
        selector = [0, ol[0], ol[1], 1, 0, 1]
        Load = decoder(ol)
        alithm = [0, 1]
        print(oc)
        print(ol)
        print(flag)
        print("nan2")
        
    if oc == jmp:
        selector = [1, 0, 1, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 0]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("jmp")
        
    if oc == jno and flag[1] == 0:
        selector = [1, 0, 1, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 0]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("jno")
        
    if oc == jze and flag[0] == 1:
        selector = [1, 0, 1, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 0]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("jze")
    elif oc == jze and flag[0] == 0:
        selector = [1, 1, 0, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 1]
        alithm = [0, 0]
        
    if oc == jmi and flag[2] == 1:
        selector = [1, 0, 1, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 0]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("jmi")
        
    if oc == jpl and flag[0] == 0 and flag[2] == 0:
        selector = [1, 0, 1, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 0]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("jpl")
        
    if oc == inp:
        selector = [1, 0, 0, 1, 1, 0]
        Load = decoder(ol)
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("inp")
        
        
    if oc == outp:
        selector = [0, ol[0], ol[1], 1, 1, 0]
        Load = [1, 1, 1, 1, 0, 1]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("outp")
        
    if oc == nop:
        selector = [1, 1, 0, 1, 1, 0]
        Load = [1, 1, 1, 1, 1, 1]
        alithm = [0, 0]
        print(oc)
        print(ol)
        print(flag)
        print("nop")
        
    #print(Load)
    
    sela2.value(selector[0])
    sela1.value(selector[1])
    sela0.value(selector[2])
    selb2.value(selector[3])
    selb1.value(selector[4])
    selb0.value(selector[5])
    
    ld0.value(Load[0])
    ld1.value(Load[1])
    ld2.value(Load[2])
    ld3.value(Load[3])
    ldo.value(Load[4])
    ldpc.value(Load[5])
    
    pm.value(alithm[0])
    al.value(alithm[1])
    
    time.sleep(1)
        
        