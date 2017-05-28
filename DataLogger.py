import serial
import time
import datetime

##############################     Setup Serial Port     #######################################
LogSerial = serial.Serial(
    port='COM2',  # '/dev/ttyAMA0'
    baudrate=9600, parity='N',
    stopbits=1, bytesize=8, timeout=0.2
)
LogSerial.flush()
LogSerial.isOpen()  # for PC

#####################       Setup Log Time and Private variables      ##########################
repeatTime = 0.5  # One data per second
timer = time.time()  # Timer to see when we started
value = ['']
check_log = True
checksum = 0

###########################         Array Definition           ################################

on_off = [
    'OFF',
    'ON'
]
selected_Program = [
    'Jeans',  # 0
    'Daily',  # 1
    'Synthetics iron  dry',  # 2
    'Synthetics Cupboard dry',  # 3
    'Cotton iron dry',  # 4
    'Cotton cupboard dry',  # 5
    'Cotton Extra dry',  # 6
    'Refresh',  # 7
    'Time prg',  # 8
    'Delicate',  # 9
    'Shirts _30',  # 10
    'Sportswear',  # 11
    'Mix',  # 12
    'Wool refresh / Basket',  # 13
    'BEDDING',  # 14
    'Shirts',  # 15
    'Stop'  # 16
]
Error_code = [

]
state = [

]
motor_direction = [
    'CW',
    'CCW'
]
public_array_name = [
    "Log_Time",  # 0
    "Data1",  # 1
    "Data2",  # 2
    "Data3",  # 3
    "Data4",  # 4
    "Data5",  # 5
    "Data6",  # 6
    "Data7",  # 7
    "Data8",  # 8
    "Data9",  # 9
    "Data10",  # 10
    "Data11",  # 11
    "Data12",  # 12
    "Data13",  # 13
    "Data14",  # 14
    "Data15",  # 15
    "Data16",  # 16
    "Data17",  # 17
    "Data18",  # 18
    "Data19",  # 19
    "Data20",  # 20
    "Data21",  # 21
    "Data22",  # 22
    "Data23",  # 23
    "Data24",  # 24
    "Data25",  # 25
    "Data26",  # 26
    "Data27",  # 27
    "Data28",  # 28
    "Data29",  # 29
    "Data30",  # 30
    "Data31",  # 31
    "Data32",  # 32
    "Data33",  # 33
    "Data34",  # 34
    "Data35",  # 35
    "Data36",  # 36
    "Data37",  # 37
    "Data38",  # 38
    "Data39",  # 39
    "Data40",  # 40
    "Data41",  # 41
    "Data42",  # 42
    "Data43",  # 43
    "Data44",  # 44
    "Data45",  # 45
    "Data46",  # 46
    "Data47",  # 47
    "Data48",  # 48
    "Data49",  # 49
    "Data50",  # 50
    "Data51",  # 51
    "Data52",  # 52
    "Data53",  # 53
    "Data54",  # 54
    "Data55",  # 55
    "Data56",  # 56
    "Data57",  # 57
    "Data58",  # 58
    "Data59",  # 59
    "Data60",  # 60
    "Data61",  # 61
    "Data62",  # 62
    "Data63",  # 63
    "Data64",  # 64
    "Data65",  # 65
    "Data66",  # 66
    "Data67",  # 67
    "Data68",  # 68
    "Data69",  # 69
    "Data70",  # 70
    "Data71",  # 71
    "Data72",  # 72
    "Data73",  # 73
    "Data74",  # 74
    "Data75",  # 75
    "Data76",  # 76
    "Data77",  # 77
    "Data78",  # 78
    "Data79",  # 79
    "Data80",  # 80
    "Data81",  # 81
    "Data82",  # 82
    "Data83",  # 83
    "Data84",  # 84
    "Data85",  # 85
    "Data86",  # 86
    "Data87",  # 87
    "Data88",  # 88
    "Data89",  # 89
    "Data90",  # 90
    "Data91",  # 91
    "Data92",  # 92
    "Data93",  # 93
    "Data94",  # 94
    "Data95",  # 95
    "Data96",  # 96
    "Data97",  # 97
    "Data98",  # 98
    "Data99",  # 99
    "Data100",  # 100
    "Data101",  # 101
    "Data102",  # 102
    "Data103",  # 103
    "Data104",  # 104
    "Data105",  # 105
    "Data106",  # 106
    "Data107",  # 107
    "Data108",  # 108
    "Data109",  # 109
    "Data110",  # 110
    "Data111",  # 111
    "Data112",  # 112
    "Data113",  # 113
    "Data114",  # 114
    "Data115",  # 115
    "Data116",  # 116
    "Data117",  # 117
    "Data118",  # 118
    "Data119",  # 119
    "Data120",  # 120
    "Data121",  # 121
    "Data122",  # 122
    "Data123",  # 123
    "Data124",  # 124
    "Data125",  # 125
    "Data126",  # 126
    "Data127",  # 127
    "Data128",  # 128
    "Data129",  # 129
    "Data130",  # 130
    "Data131",  # 131
    "Data132",  # 132
    "Data133",  # 133
    "Data134",  # 134
    "Data135",  # 135
    "CheckSum",  # 136
]
public_array =bytearray([])
log_array = []

def log_Schedule(public_array):

    del log_array[:]  # clear buffer array
    log_array.append(str(public_array[0]))  # 0
    log_array.append(str(public_array[1]))  # 1
    log_array.append(on_off[tobits(public_array[2], 1)])  # 2	pompa ON/OFF
    log_array.append(str(public_array[3]& 0x0F ))  # 3 low byte
    log_array.append(str(public_array[3]>> 4))  # 4 high byte
    log_array.append(str(public_array[6]))  # 5
    log_array.append(str(public_array[6]& 0x1C))  # 6
    log_array.append(selected_Program[public_array[7]& 0x0F])  # 7
    log_array.append(str(public_array[8]))  # 8
    log_array.append(str(public_array[9]))  # 9
    log_array.append(str(public_array[10]))  # 10
    log_array.append(str(public_array[11]))  # 11
    log_array.append(str(public_array[12]))  # 12
    log_array.append(str(public_array[13]))  # 13
    log_array.append(str(public_array[14]))  # 14
    log_array.append(str(public_array[15]))  # 15
    log_array.append(str(public_array[16]))  # 16
    log_array.append(str(public_array[17]))  # 17
    log_array.append(str(public_array[18]))  # 18
    log_array.append(str(public_array[19]))  # 19
    log_array.append(str(public_array[20]))  # 20
    log_array.append(str(public_array[21]))  # 21
    log_array.append(str(public_array[22]))  # 22
    log_array.append(str(public_array[23]))  # 23
    log_array.append(str(public_array[24]))  # 24
    log_array.append(str(public_array[25]))  # 25
    log_array.append(str(public_array[26]))  # 26
    log_array.append(str(public_array[27]))  # 27
    log_array.append(str(public_array[28]))  # 28
    log_array.append(str(public_array[29]))  # 29
    log_array.append(str(public_array[30]))  # 30
    log_array.append(str(public_array[31]))  # 31
    log_array.append(str(public_array[32]))  # 32
    log_array.append(str(public_array[33]))  # 33
    log_array.append(str(public_array[34]))  # 34
    log_array.append(str(public_array[35]))  # 35
    log_array.append(str(public_array[36]))  # 36
    log_array.append(str(public_array[37]))  # 37
    log_array.append(str(public_array[38]))  # 38
    log_array.append(str(public_array[39]))  # 39
    log_array.append(str(public_array[40]))  # 40
    log_array.append(str(public_array[41]))  # 41
    log_array.append(str(public_array[42]))  # 42
    log_array.append(str(public_array[43]))  # 43
    log_array.append(str(public_array[44]))  # 44
    log_array.append(str(public_array[45]))  # 45
    log_array.append(str(public_array[46]))  # 46
    log_array.append(str(public_array[47]))  # 47
    log_array.append(str(public_array[48]))  # 48
    log_array.append(str(public_array[49]))  # 49
    log_array.append(str(public_array[50]))  # 50
    log_array.append(str(public_array[51]))  # 51
    log_array.append(str(public_array[52]))  # 52
    log_array.append(str(public_array[53]))  # 53
    log_array.append(str(public_array[54]))  # 54
    log_array.append(str(public_array[55]))  # 55
    log_array.append(str(public_array[56]))  # 56
    log_array.append(str(public_array[57]))  # 57
    log_array.append(str(public_array[58]))  # 58
    log_array.append(str(public_array[59]))  # 59
    log_array.append(str(public_array[60]))  # 60
    log_array.append(str(public_array[61]))  # 61
    log_array.append(str(public_array[62]))  # 62
    log_array.append(str(public_array[63]))  # 63
    log_array.append(str(public_array[64]))  # 64
    log_array.append(str(public_array[65]))  # 65
    log_array.append(str(public_array[66]))  # 66
    log_array.append(str(public_array[67]))  # 67
    log_array.append(str(public_array[68]))  # 68
    log_array.append(str(public_array[69]))  # 69
    log_array.append(str(public_array[70]))  # 70
    log_array.append(str(public_array[71]))  # 71
    log_array.append(str(public_array[72]))  # 72
    log_array.append(str(public_array[73]))  # 73
    log_array.append(str(public_array[74]))  # 74
    log_array.append(str(public_array[75]))  # 75
    log_array.append(str(public_array[76]))  # 76
    log_array.append(str(public_array[77]))  # 77
    log_array.append(str(public_array[78]))  # 78
    log_array.append(str(public_array[79]))  # 79
    log_array.append(str(public_array[80]))  # 80
    log_array.append(str(public_array[81]))  # 81
    log_array.append(str(public_array[82]))  # 82
    log_array.append(str(public_array[83]))  # 83
    log_array.append(str(public_array[84]))  # 84
    log_array.append(str(public_array[85]))  # 85
    log_array.append(str(public_array[86]))  # 86
    log_array.append(str(public_array[87]))  # 87
    log_array.append(str(public_array[88]))  # 88
    log_array.append(str(public_array[89]))  # 89
    log_array.append(str(public_array[90]))  # 90
    log_array.append(str(public_array[91]))  # 91
    log_array.append(str(public_array[92]))  # 92
    log_array.append(str(public_array[93]))  # 93
    log_array.append(str(public_array[94]))  # 94
    log_array.append(str(public_array[95]))  # 95
    log_array.append(str(public_array[96]))  # 96
    log_array.append(str(public_array[97]))  # 97
    log_array.append(str(public_array[98]))  # 98
    log_array.append(str(public_array[99]))  # 99
    log_array.append(str(public_array[100]))  # 100
    log_array.append(str(public_array[101]))  # 101
    log_array.append(str(public_array[102]))  # 102
    log_array.append(str(public_array[103]))  # 103
    log_array.append(str(public_array[104]))  # 104
    log_array.append(str(public_array[105]))  # 105
    log_array.append(str(public_array[106]))  # 106
    log_array.append(str(public_array[107]))  # 107
    log_array.append(str(public_array[108]))  # 108
    log_array.append(str(public_array[109]))  # 109
    log_array.append(str(public_array[110]))  # 110
    log_array.append(str(public_array[111]))  # 111
    log_array.append(str(public_array[112]))  # 112
    log_array.append(str(public_array[113]))  # 113
    log_array.append(str(public_array[114]))  # 114
    log_array.append(str(public_array[115]))  # 115
    log_array.append(str(public_array[116]))  # 116
    log_array.append(str(public_array[117]))  # 117
    log_array.append(str(public_array[118]))  # 118
    log_array.append(str(public_array[119]))  # 119
    log_array.append(str(public_array[120]))  # 120
    log_array.append(str(public_array[121]))  # 121
    log_array.append(str(public_array[122]))  # 122
    log_array.append(str(public_array[123]))  # 123
    log_array.append(str(public_array[124]))  # 124
    log_array.append(str(public_array[125]))  # 125
    log_array.append(str(public_array[126]))  # 126
    log_array.append(str(public_array[127]))  # 127
    log_array.append(str(public_array[128]))  # 128
    log_array.append(str(public_array[129]))  # 129
    log_array.append(str(public_array[130]))  # 130
    log_array.append(str(public_array[131]))  # 131
    log_array.append(str(public_array[132]))  # 132
    log_array.append(str(public_array[133]))  # 133
    log_array.append(str(public_array[134]))  # 134
    log_array.append(str(public_array[135]))  # 135

    return log_array

#############################      Function Write Data      #####################################
def write_data(value):

    today = datetime.date.today()
    log_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    with open(str(today) + '.csv', 'ab') as f:
        f.write('\n' + log_time)
        for i in range(0, public_array_name.__len__()-1):
            f.write("," + value[i])

#############################      Function Create File      ###################################
def create_file(name):

    '''      '''
    with open(str(name) + '.csv', 'ab') as f:
        f.write('\n' + public_array_name[0])
        for i in range(1, public_array_name.__len__()):
            f.write("," + public_array_name[i])
        f.close()
    print "Create File OK"

##############################    integer to binary      #######################################
def tobits(integer, bit):
    data = (bin(integer)[2:10])
    data = '00000000'[len(data):] + data
    # print data
    data = int(data[(7-bit):(8-bit)])
    # print data
    return data

###############################################################################################3
def get_data():

    time.sleep(0.2)
    check_log = True
    checksum = 0
    del public_array[:]
    for i in range(0, public_array_name.__len__()-1):
        try:
            data = (int((LogSerial.readline(1).encode('hex')), 16))
            checksum = checksum + data
            public_array.append(data)
        except:  # ValueError or Other Errors
            check_log = False
            break

    if(check_log == True ):
        if(checkSum(checksum-data) == data):

            #print type(public_array)
            #log_array.append(public_array[0])  # 0
            #  print(bin(int(value[36]))[2:])  #bitwise process
            #log_Schedule(public_array)
            #write_data(str(log_Schedule(public_array)))
            write_data(log_Schedule(public_array))
            print("OK")
        else:
            print(checkSum(checksum-data))
    else:
        print("ERROR")

###############################################################################################
def request_log():

    array_data = bytearray([4, 0, 0, 0, 251])
    LogSerial.write(array_data)
    print "request log..."

###############################################################################################
def checkSum( command, byte=0, value=0):
    cS = 255-(command+byte+value)%255
    return cS

###############################################################################################
log_day = datetime.date.today()
create_file(log_day)

while True:
    #  one log file everyday
    if(datetime.date.today() != log_day ):
        log_day = datetime.date.today()
        create_file(log_day)

    if time.time() - timer > repeatTime:
        request_log()
        get_data()
        timer = time.time()

LogSerial.close()
