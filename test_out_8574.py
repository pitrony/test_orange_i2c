import smbus
import time

bus= smbus.SMBus(1)
bWrite=0xFF
mask=0xF7
bus.write_byte(0x20, 0xF7)
while (True):
	res=bus.read_byte(0x20)
	res&=0xC0
	print('P6-P7 bit state: 0x%X' %res)
	if ((res==0x0 or (res==0xC0)):
		time.sleep(2)
		continue
	if(res==0x80):
		bWrite=0x8 | mask
		bus.write_byte(0x20, bWrite)
	if(res==0x40):
		bWrite &= mask
		bus.write_byte(0x20, bWrite)
	time.sleep(2)	
