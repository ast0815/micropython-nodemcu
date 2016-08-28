import machine as m

def Pin(nr):
    if nr==0:
        return m.Pin(16)
    if nr==1:
        return m.Pin(5)
    if nr==2:
        return m.Pin(4)
    if nr==3:
        return m.Pin(0)
    if nr==4:
        return m.Pin(2)
    if nr==5:
        return m.Pin(14)
    if nr==6:
        return m.Pin(12)
    if nr==7:
        return m.Pin(13)
    if nr==8:
        return m.Pin(15)
    if nr==9:
        return m.Pin(03)
    if nr==10:
        return m.Pin(1)
