import serial

myUART = serial.Serial(port = "COM1", baudrate=9600, bytesize = 8,
                           timeout = 1, stopbits = serial.STOPBITS_ONE)


def Led(LedIndex):
    WriteMsg(f"led 0x{LedIndex};")

def Button():
    WriteMsg('but;')
    message = myUART.readline()
    return int(DecodeMsg(message)[1])

def Detector():
    WriteMsg('det;')
    message = myUART.readline()
    return int(DecodeMsg(message)[1])


def DecodeMsg(message):
    new_str = message.decode('utf-8')
    new_str = new_str.strip()
    list_str = new_str.split()
    return list_str


def WriteMsg(msg):
    myUART.write(msg.encode('utf-8'))


def ID():
    WriteMsg('id;')
    message = myUART.readline()
    return DecodeMsg(message)[1]




