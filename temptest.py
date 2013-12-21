#!/usr/bin/python

MIN_TEMP = -100
temp1 = "/sys/bus/w1/devices/28-00000379fea9/w1_slave"
temp2 = "/sys/bus/w1/devices/28-00000447416d/w1_slave"

def read_temp1():
  # open/read/close the file with the temperature
  temp1file = open(temp1)
  text = temp1file.read()
  temp1file.close()

  # split the two lines
  lines = text.split("\n")

  # make sure the crc is valid
  if lines[0].find("YES") > 0:
    #get the 9th (10th) chunk of text and lose the t= bit
    temp = float((lines[1].split(" ")[9])[2:])
    # add a decimal point
    temp /= 1000
    temp = round(temp,2)
    return temp
  return MIN_TEMP-1

def read_temp2():
  # open/read/close the file with the temperature
  temp2file = open(temp2)
  text = temp2file.read()
  temp2file.close()

  # split the two lines
  lines = text.split("\n")

  # make sure the crc is valid
  if lines[0].find("YES") > 0:
    #get the 9th (10th) chunk of text and lose the t= bit
    temp = float((lines[1].split(" ")[9])[2:])
    # add a decimal point
    temp /= 1000
    temp = round(temp,2)
    return temp
  return MIN_TEMP-1

print(read_temp1())
print(read_temp2())


