#!/usr/bin/env python3

# used only for testing purposes in the absence of the real hardware

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
    sendctrlByteOut(ctrlByte)

def turn_off_channel(ch):
    global ctrlByte
    # create the new state of relays:
    ctrlByte = ctrlByte ^ channelByte(ch)
    # send the new control Byte out the I2C:
    sendctrlByteOut(ctrlByte)
    
def turn_off_all_channels():
    global ctrlByte
    # create the new state of relays:
    ctrlByte = ctrlByteAllOFF
    # send the new control Byte out the I2C:
    sendctrlByteOut(ctrlByte)

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
            
def sendctrlByteOut(ctrlByte):
    print(f"Printing to address {address:x}, Ctrl command: {CMD_CHANNEL_CTRL:x}, the control byte: {ctrlByte:b}")


if (__name__ == '__main__'):
    import time
    print("Demo")
    
    
    print("it looks like we connected to SMBus")
    time.sleep(0.5)
    print(f"Printing to address {address:x}, Ctrl command: {CMD_CHANNEL_CTRL:x}, the control byte: {ctrlByteAllON:b}")
    time.sleep(0.5)
    turn_off_all_channels()
    time.sleep(0.5)
    print(f"Printing to address {address:x}, Ctrl command: {CMD_CHANNEL_CTRL:x}, the control byte: {ctrlByteAllON:b}")
    time.sleep(0.5)
    turn_off_all_channels()
    time.sleep(0.5)

