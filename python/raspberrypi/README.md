# DFRobot_PLAY_IIC
- [中文版](./README_CN.md)

Here comes the DFPlayer Pro-a mini simple but powerful MP3 Player! This MP3 player module supports four controlling modes: Arduino, AT command, on-board buttons, and ADKEY. You can directly press the on-board button to play or switch music without using a controller. By using a USB cable, you can easily copy your favorite songs into this module to play them any where you want, or use it as a sound card for your PC or Raspberry Pi after connecting them together.

![Product Image](../../resources/images/SEN0245svg1.png)


## Product Link (Link to DFRobot store)

    SKU: XXXX

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary
1. Playing Music

## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.
```python
python play.py
```



## Methods

```python
  def begin(self ):
    '''!  
      @brief init function
      @return Boolean type, Indicates the initialization result
      @retval true The setting succeeded
      @retval false Setting failed
    '''
	
  def get_vol(self):
    '''!  
      @brief Get volume 
      @return vol：volume
    '''
	
  def set_vol(self,vol):
   '''!  
     @brief Set volume 
     @param vol:0-30
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def get_play_mode(self):
    '''!  
      @brief Get palyback mode 
      @return Play Mode
    '''
      
  def switch_function(self,function):
   '''!  
     @brief Set working mode 
     @param eFunction_t:MUSIC,RECORD,UFDISK
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def set_play_mode(self,mode):
   '''!  
     @brief Set playback mode 
     @param ePlayMode_t:SINGLECYCLE,ALLCYCLE,SINGLE,RANDOM,FOLDER
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def set_led(self,om):
   '''!  
     @brief Set indicator LED(Power-down save) 
     @param true or false
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''
 
  def set_prompt(self,on):
   '''!  
     @brief Set the prompt tone(Power-down save) 
     @param true or false
     @return Boolean type, the result of seted
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def next(self):
   '''!
     @brief Next 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def last(self):
   '''!  
     @brief Previous 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
    
  def start(self):
   '''!  
     @fn start
     @brief Play 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def pause(self):
   '''!  
     @brief Pause 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def delCurFile(self):
   '''!  
     @brief Delete the currently-playing file 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
    
  def play_spec_file(self,name):
   '''!  
     @brief Play file of the specific path 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def play_file_num(self,num):
   '''!  
     @brief Play the file of specific number, the numbers are arranged according to the sequences the files copied into the U-disk 
     @param File number, can be obtained by getCurFileNumber()
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
    
  def fast_forward(self,second):
   '''!  
     @brief Fast forward the currently-playing song
     @param second  FF time(Unit: S) 
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def fast_reverse(self,second):
   '''!  
     @brief Fast Rewind the currently-playing song 
     @param second  FR time(Unit: S)
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
    
  def set_play_time(self,second):
   '''!  
     @brief Let the currently-playing song start playing from a particular time point 
     @param second  Fixed time point
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''

  def get_cur_time(self):
   '''!
     @brief Get the time length the current song has played  
     @return Time node
   '''
    
  def enable_AMP(self):
   '''!  
     @brief Enable Amplifier chip
     @return Boolean type, the result of operation
     @retval true The setting succeeded
     @retval false Setting failed
   '''
    
  def disable_AMP(self):
   '''!  
     @brief init function
     @return Boolean type, Indicates the initialization result
     @retval true The setting succeeded
     @retval false Setting failed
   '''
    
  def get_total_time(self):
   '''!  
   * @brief Get the total length of the currently-playing song
   * @return The total number of time
   '''
    
  def get_cur_file_number(self):
   '''!  
   * @brief Get file number 
   * @return  file number
   '''

  def get_total_file(self):
   '''!  
     @brief Get the number of files available to play 
     @return Total number of files
   '''

  def get_file_name(self):
   '''!
     @brief Get the name of the playing file 
     @return A string representing the filename
   '''
```

## Compatibility


* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |           |            |    √     |         |
| RaspberryPi4 |     √     |            |          |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |

## History

- 2021/06/04 - 1.0.0 版本
- 2021/10/15 - 1.0.1 版本

## Credits

Written by fengli(li.feng@dfrobot.com), 2020.7.31 (Welcome to our [website](https://www.dfrobot.com/))
