from board_driver_simulator import open,close,but,pot,det,led,set_port,get_port

current_led=0
def set_point(position):
    if position==0:
        set_port(1<<13)
    elif position==1:
        set_port(1<<5)
    elif position==2:
        set_port(1<<9)
    elif position==3:
        set_port(1<<17)
    else:
        set_port(0)


def get_key():
    state=get_port()
    if state==1<<18:
        pressed_butt=0
    elif state==1<<12:
        pressed_butt=1
    elif state==1<<15:
        pressed_butt=2
    elif state==1<<20:
        pressed_butt=3
    else:
        pressed_butt=-1
    return pressed_butt


def step(direction,nr_steps):
    global current_led
    steps_ctr=nr_steps
    while(steps_ctr!=0):
        if direction=='left':
            current_led=(current_led-1)%4
        elif direction=='right':
            current_led=(current_led+1)%4
        set_point(current_led)
        steps_ctr-=1

    
    
def get_detector():
    if get_port()==1<<30:
        statement='active'
    else:
        statement='no_active'
    return statement


def wait_for_key():
    while(True):
        if(get_key()!=-1):
            break
    return get_key()



def get_pot():
    potentiom=get_port()
    print('Binary:',f"{potentiom:010b}",'Decimal:',f"{potentiom:04d}")
    
