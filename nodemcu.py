import machine as m

# Translate NodeMcu's pin designations to ESP pin numbers
def Pin(name, *args, **kwargs):
    try:
        name = name.lower()
    except AttributeError:
        pass
    if name==0 or name=='d0':
        return m.Pin(16, *args, **kwargs)
    if name==1 or name=='d1':
        return m.Pin(5, *args, **kwargs)
    if name==2 or name=='d2':
        return m.Pin(4, *args, **kwargs)
    if name==3 or name=='d3' or name=='flash':
        return m.Pin(0, *args, **kwargs)
    if name==4 or name=='d4' or name=='led':
        return m.Pin(2, *args, **kwargs)
    if name==5 or name=='d5':
        return m.Pin(14, *args, **kwargs)
    if name==6 or name=='d6':
        return m.Pin(12, *args, **kwargs)
    if name==7 or name=='d7':
        return m.Pin(13, *args, **kwargs)
    if name==8 or name=='d8':
        return m.Pin(15, *args, **kwargs)
    if name==9 or name=='d9' or name=='rx':
        return m.Pin(03, *args, **kwargs)
    if name==10 or name=='d10' or name=='tx':
        return m.Pin(1, *args, **kwargs)
    raise ValueError("Unknown pin!")
