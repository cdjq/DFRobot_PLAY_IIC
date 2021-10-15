'''!
 @file DFRobot_PLAY_IIC.py
 @brief Define the basic structure of class DFRobot_PLAY_IIC, the implementation of the basic methods
 @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 @licence     The MIT License (MIT)
 @author [fengli](li.feng@dfrobot.com)
 @version  V1.1
 @date  2021-10-15
 @https://github.com/DFRobot/DFRobot_PLAY_IIC
'''
# -*- coding: utf-8 -*
import serial
import time
import smbus
                

class DFRobot_PLAY_IIC(object):


  
  ''' register configuration '''
  I2C_ADDR                = 0x50
  MUSIC = 1         ##Music Mode 
  UFDISK = 2        ##Slave mode 
 
  SINGLECYCLE = 1   ##Repeat one song 
  ALLCYCLE = 2      ##Repeat all 
  SINGLE = 3        ##Play one song only 
  RANDOM = 4        ##Random
  FOLDER = 5        ##Repeat all songs in folder 
  ERROR  = 6           
  curFunction = MUSIC
  ''' Conversion data '''
  #txbuf      = [0]
  _addr      =  0x50
  #_mode      =  0
  #idle =    0
  def __init__(self ,bus,address):
    self.i2cbus = smbus.SMBus(bus)
    self._addr = address
    self.idle =    0

  def begin(self ):
    '''!  
      @brief init function
      @return Boolean type, Indicates the initialization result
      @retval true The setting succeeded
      @retval false Setting failed
    '''
    string,length= self.pack()
    #self.i2cbus.write_byte(self._addr,0xaa)
    time.sleep(0.5)
    self.write_AT_command(string,length)
    if self.read_ack(4) == 'OK\r\n':
      return True
    else:
      return False
  def get_vol(self):
    '''!  
      @brief Get volume 
      @return vol：volume
    '''
    vol = "  "
    string,length = self.pack("VOL","?")
    self.write_AT_command(string,length)
    ack = self.read_ack(12)
    vol += ack[7]
    if ack[8] != 0x5d:
      vol += ack[8]
    return int(vol)
  def set_vol(self,vol):
   '''!  
     @brief Set volume 
     @param vol:0-30
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   string,length = self.pack("VOL",str(vol))
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def get_play_mode(self):
    '''!  
      @brief Get palyback mode 
      @return Play Mode
    '''
    mode = "  "
    string,length = self.pack("PLAYMODE","?")
    self.write_AT_command(string,length)
    ack = self.read_ack(13)
    mode = ack[10]
    if ack[11] == '\r' and ack[12] == '\n':
      return int(mode)
    else:
      return self.ERROR
      
  def switch_function(self,function):
   '''!  
     @brief Set working mode 
     @param eFunction_t:MUSIC,RECORD,UFDISK
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   string,length = self.pack("FUNCTION",str(function))
   self.write_AT_command(string,length)
   self.pauseFlag = 0
   if self.read_ack(4) == "OK\r\n":
    time.sleep(1.5)
    return True
   else:
    return False

  def set_play_mode(self,mode):
   '''!  
     @brief Set playback mode 
     @param ePlayMode_t:SINGLECYCLE,ALLCYCLE,SINGLE,RANDOM,FOLDER
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAYMODE",str(mode))
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def set_led(self,om):
   '''!  
     @brief Set indicator LED(Power-down save) 
     @param true or false
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   mode = "   "
   if on == True:
     mode = "ON"
   else:
     mode = "OFF"
   string,length = self.pack("LED",mode)
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
 
  def set_prompt(self,on):
   '''!  
     @brief Set the prompt tone(Power-down save) 
     @param true or false
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if on == True:
     mode = "ON"
   else:
     mode = "OFF"
   string,length = self.pack("PROMPT",mode)
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def next(self):
   '''!
     @brief Next 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAY","NEXT")
   self.write_AT_command(string,length)
   pauseFlag = 1
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def last(self):
   '''!  
     @brief Previous 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAY","LAST")
   self.write_AT_command(string,length)
   pauseFlag = 1
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def start(self):
   '''!  
     @fn start
     @brief Play 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   pauseFlag = 1
   string,length = self.pack("PLAY","PP")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def pause(self):
   '''!  
     @brief Pause 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   pauseFlag = 0
   string,length = self.pack("PLAY","PP")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def delCurFile(self):
   '''!  
     @brief Delete the currently-playing file 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("DEL")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def play_spec_file(self,name):
   '''!  
     @brief Play file of the specific path 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAYFILE",name)
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def play_file_num(self,num):
   '''!  
     @brief Play the file of specific number, the numbers are arranged according to the sequences the files copied into the U-disk 
     @param File number, can be obtained by getCurFileNumber()
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("PLAYFILE",str(num))
   self.write_AT_command(string,length)
   print(string)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def fast_forward(self,second):
   '''!  
     @brief Fast forward the currently-playing song
     @param second  FF time(Unit: S) 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   cmd = "+" + str(second)
   string,length = self.pack("TIME","cmd")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False

  def fast_reverse(self,second):
   '''!  
     @brief Fast Rewind the currently-playing song 
     @param second  FR time(Unit: S)
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   cmd = "-" + str(second)
   string,length = self.pack("TIME","cmd")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def set_play_time(self,second):
   '''!  
     @brief Let the currently-playing song start playing from a particular time point 
     @param second  Fixed time point
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("TIME",str(second))
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def get_int(self,string):
    '''!  
      @brief The string is converted to a number
      @param The string to be converted
      @return A natural number of type int
    '''
    num_len = 0
    num = 0
    
    for i in range(0,len(string)):
      if string[i] != '\r' and string[i+1] != '\n':
        num_len += 1
      else:
        break
    for i in range(0,num_len):
      num = num*10 + ord(string[i]) - ord('0')
    return num


  def get_cur_time(self):
   '''!
     @brief Get the time length the current song has played  
     @return Time node
   '''
   if self.curFunction != self.MUSIC:
     return False

   string,length = self.pack("QUERY","3")
   self.write_AT_command(string,length)
   cur_time = self.read_ack(6)
   return self.get_int(cur_time)
    
  def enable_AMP(self):
   '''!  
     @brief Enable Amplifier chip
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("AMP","ON")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def disable_AMP(self):
   '''!  
     @brief init function
     @return Boolean type, Indicates the initialization result
     @retval true The setting succeeded
     @retval false Setting failed
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("AMP","OFF")
   self.write_AT_command(string,length)
   if self.read_ack(4) == "OK\r\n":
    return True
   else:
    return False
    
  def get_total_time(self):
   '''!  
   * @brief Get the total length of the currently-playing song
   * @return The total number of time
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("QUERY","4")
   self.write_AT_command(string,length)
   total_time = self.read_ack(6)
   return self.get_int(total_time)
    
  def get_cur_file_number(self):
   '''!  
   * @brief Get file number 
   * @return  file number
   '''
   if self.curFunction != self.MUSIC:
     return False
   string,length = self.pack("QUERY","1")
   self.write_AT_command(string,length)
   cur_number = self.read_ack(6)
   return self.get_int(cur_number)

  def get_total_file(self):
   '''!  
     @brief Get the number of files available to play 
     @return Total number of files
   '''
   if self.curFunction != self.MUSIC:
     return False

   string,length = self.pack("QUERY","2")
   self.write_AT_command(string,length)
   total_file = self.read_ack(6)
   return self.get_int(total_file)

  def get_file_name(self):
   '''!
     @brief Get the name of the playing file 
     @return A string representing the filename
   '''
   if self.curFunction != self.MUSIC:
     return "get file name error"
   string,length = self.pack("QUERY","5")
   self.write_AT_command(string,length)
   name = self.read_ack(0)
   return name 
   
  def pack(self,cmd = " ",para = " "):
    '''!  
      @brief Package data
      @param cmd The command
      @param para parameter
      @return A packed bag
    '''
    atCmd = ""
    atCmd += "AT"
    if cmd != " ":
      atCmd += "+"
      atCmd += cmd
    
    if para != " ":
     atCmd += "="
     atCmd += para

    atCmd += "\r\n";
    at_str = atCmd;
    at_length = len(at_str)
    return at_str,at_length
    
  def write_AT_command(self, data,len1):
    '''!  
      @brief Sends the AT command
      @param data Data to be sent
      @param len1 The length of the data to send
    '''
    self.read(24)
    time.sleep(0.1)
    for i in range(0,len1):
      self.i2cbus.write_byte(self._addr ,ord(data[i]))
      #print(ord(data[i]))
    #self.i2cbus.write_i2c_block_data(self._addr,0,[0,0,0])
  
  def read_ack(self,len):
    '''!  
      @brief Reads reply data
      @param len Length of data to read
      @return returns the reply as string data
    '''
    offset = 0
    data = [0]*108
    ack = ""
    time.sleep(0.1)
    if len == 0:
      data = self.read(108)
      for i in range(0,108):
        ack += chr(data[i])
        offset += 1
        if(ack[offset - 1]) == '\n' and (ack[offset-2]) =='\r':
          break
    else:
      data = self.read(len)
      for i in range(0,len):
        ack += chr(data[i])
        #print(data[i])
        offset += 1
        if(ack[offset - 1]) == '\n' and (ack[offset-2]) =='\r':
          ack += chr(0)
          break
    #print(ack)
    return ack
  def read(self,len):
    '''!  
      @brief read data     
      @param len The length of the data
      @return data stored as an array
    '''
    #self.i2cbus.write_byte(self._addr,1)
    rslt = [0]*108 
    time.sleep(0.01)
    #rslt = self.i2cbus.read_i2c_block_data(self._addr,0xff,len)
    for i in range(0,len):
       time.sleep(0.01)
       rslt[i] = self.i2cbus.read_byte(self._addr)
    #print(rslt)
    return rslt