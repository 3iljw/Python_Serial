import serial

def open_port(COM_PORT, BAUD_RATES) :
    '''
    COM_PORT : 
      in windows : 
        f'COM{com.port.number}'
      in linux : 
        f'/dev/ttyS{com.port.number}'

    BAUD_RETES :
      default value is 57600
    '''
    if serial.Serial().is_open :
        pass
    else :
        global ser 
        ser = serial.Serial(
            port = COM_PORT, 
            baudrate = BAUD_RATES, 
            parity = 'N', 
            stopbits = 1, 
            bytesize = 8,
            timeout = 1
        )
    # ser = serial.Serial(COM_PORT, BAUD_RATES, bytesize=8, parity='N', stopbits=1, timeout=1)

def read_data() :
    # while ser.in_waiting :
    try :
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        return mcu_feedback
    except Exception as e: 
        return str(e)

def write_data(data) :
    data = (str(data)).encode()
    ser.write(data)

def close_port() :
    if ser.is_open :
        ser.close()
    else :
        pass
