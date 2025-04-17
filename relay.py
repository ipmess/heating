#!/usr/bin/env python3

from smbus2 import SMBus

channel = 1
address = 0x11
CMD_CHANNEL_CTRL = 0x10
ctrlByteAllON = 0b00001111
ctrlByteAllOFF = 0b00000000

CHANNEL1_BIT = 0b00000001
CHANNEL2_BIT = 0b00000010
CHANNEL3_BIT = 0b00000100
CHANNEL4_BIT = 0b00001000

# Initialize all off:
ctrlByte = ctrlByteAllOFF

def turn_on_channel(ch):
    global ctrlByte
    # create the new state of relays:
    ctrlByte = ctrlByte | channelByte(ch)
    # send the new control Byte out the I2C:
    sendCtrlByteOut(ctrlByte)

def turn_off_channel(ch):
    global ctrlByte
    # create the new state of relays:
    ctrlByte = ctrlByte ^ channelByte(ch)
    # send the new control Byte out the I2C:
    sendCtrlByteOut(ctrlByte)
    
def turn_off_all_channels():
    global ctrlByte
    # create the new state of relays:
    ctrlByte = ctrlByteAllOFF
    # send the new control Byte out the I2C:
    sendCtrlByteOut(ctrlByte)

def channelByte(ch):
    match ch:
        case 1:
            return CHANNEL1_BIT
        case 2:
            return CHANNEL2_BIT
        case 3:
            return CHANNEL3_BIT
        case 4:
            return CHANNEL4_BIT
        case _:
            return ctrlByteAllOFF
            
def sendCtrlByteOut(ctrlByte):
    with SMBus(channel) as bus:
        bus.write_byte_data(address, CMD_CHANNEL_CTRL, ctrlByte)


if (__name__ == '__main__'):
    import time
    print("Resting/debugging")
    with SMBus(channel) as bus:
        print("it looks like we connected to SMBus")
        time.sleep(0.5)
        bus.write_byte_data(address, CMD_CHANNEL_CTRL, ctrlByteAllON)
        time.sleep(0.5)
        turn_off_all_channels()
        time.sleep(5)
        turn_on_channel(1)
        time.sleep(5)
        turn_on_channel(2)
        time.sleep(5)
        turn_on_channel(3)
        time.sleep(5)
        turn_on_channel(4)
        time.sleep(5)
        turn_off_channel(1)
        time.sleep(5)
        turn_off_channel(2)
        time.sleep(5)
        turn_off_channel(3)
        time.sleep(5)
        turn_off_channel(4)

