import smbus
import time

bus= smbus.SMBus(3)
bWrite=0x00
#mask=0xFF
adr_2=0x24
adr_1=0x20
i=0
bus.write_byte(adr_2, 0xFF)
while (True):
	if(bus.read_binary(adr_1)):
		while (i<10):
			bWrite=0xF9 
			bus.write_byte(adr_2, bWrite)
			time.sleep(1)
			bWrite=0xFA
			bus.write_byte(adr_2, bWrite)
			time.sleep(1)
			#continue
			bWrite=0xFC
			bus.write_byte(adr_2, bWrite)
			time.sleep(1)
			#continue
			bWrite=0xF8
			bus.write_byte(adr_2, bWrite)
			time.sleep(1)
			#continue
			i=i+1

