# DFRobot_PLAY_IIC
您是否在寻找一款简单又强大的MP3播放模块？看这里！这款MP3播放模块支持<br>
arduino、AT指令、板载按键和AD按键四种控制方式。 <br>
通过板载按键即使在没有微控制器的情况下也能进行音乐播放和切换。模块搭载<br>
了128MB的存储空间，通过USB线您可以很容易的将您喜欢的音乐拷贝到模块中。<br>
该模块可作为电脑或Raspberry Pi声卡，用USB数据线将模块和电脑连接，电脑<br>
播放音乐即可通过该 模块输出。<br>

![Product Image](../../resources/images/SEN0245svg1.png)


## 产品链接（链接到中文商城）

    SKU：产品名称

## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性y)
* [历史](#历史)
* [创作者](#创作者)

## 概述
1. Playing Music

## 库安装

要使用这个库，首先将库下载到Raspberry Pi，然后打开例程文件夹。要执行一个例程demox.py，请在命令行中输入python demox.py。例如，要执行play.py例程，你需要输入:

```python
python play.py
```



## 方法

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

## 兼容性


| 主板         | 通过 | 未通过 | 未测试 | 备注 |
| ------------ | :--: | :----: | :----: | :--: |
| RaspberryPi2 |      |        |   √    |      |
| RaspberryPi3 |      |        |   √    |      |
| RaspberryPi4 |  √   |        |        |      |

* Python 版本

| Python  | 通过 | 未通过 | 未测试 | 备注 |
| ------- | :--: | :----: | :----: | ---- |
| Python2 |  √   |        |        |      |
| Python3 |  √   |        |        |      |

## 历史

- 2021/06/04 - 1.0.0 版本
- 2021/10/15 - 1.0.1 版本

## 创作者

Written by fengli(li.feng@dfrobot.com), 2020.7.31 (Welcome to our [website](https://www.dfrobot.com/))
