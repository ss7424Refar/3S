# Selenium 入门教程



## 1. Selenium 简介

 - 什么是Selenium

   ```
   Selenium是一个用于Web应用程序自动化测试工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7,  8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。
   
   主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。
   测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成 .Net、Java、Python等不同语言的测试脚本。
   ```

   

 - Selenium套件介绍

   1. Selenium IDE              

      ```
      IDE是一个Firefox插件，可以录制用户的基本操作，生成测试用例。随后可以运行这些测试用例在浏览器里回放，可将测试用例转换为其他语言的自动化脚本。
      ```

   2. Selenium RC 

      ```
      RC为核心部分。它使用的编程语言，如Java，C＃，PHP，Python、Ruby和Perl强大功能来创建更复杂的测试。Selenium RC分  为Client Libraries(编写测试脚本) 和 Selenium Server（控制浏览器行为）。
      ```

   3. Selenium WebDriver 

      ```
      WebDriver前身是Selenium RC，可以看作是Selenium RC的替代品，直接发送命令给浏览器，并检索结果
      ```

   4. Selenium Grid  

      ```
      网格用于运行在不同的机器，不同的浏览器并行测试的工具，目的在于加快测试用例运行的速度，从而减少测试运行的总时间。利用Grid可以很方便地实现在多台机器上和异构环境中运行测试用例。
      ```

- Selenium特点

  ```
  开源，免费；
  多浏览器支持：Firefox、Chrome、IE、Opera、Edge;
  多平台支持：Linux、Windows、MAC;
  多语言支持：Java、Python、Ruby、C#、JavaScript、C++；
  简单（API简单）、灵活（用开发语言驱动>；
  ```



+ Selenium的应用场景

  1. 自动化不自动化？ 这是个问题！[摘自](https://www.seleniumhq.org/docs/cn/01_introducing_selenium.jsp)

     > 自动化是否总是有利的？什么时候人们决定自动化测试用例呢？

     ```
     自动化测试用例并不总是有利的。有些时候手动测试可能更为恰当。 例如，如果应用程序的用户界面在不久的将来会有相当大的改变，那么任何自动化将需要重写。此外，有时根本没有足够的时间来构建测试自动化。短期而言，手动测试可能会更为有效。 如果应用程序有一个十分紧迫的截止日期，目前还没有测试自动化，并且它的当务之急是在这个时限内完成的测试，那么手动测试是最好的解决办法。
     
     然而，对于提高软件团队测试过程的长期效率，自动化有独特的优势。 测试自动化支持：
     	1. 频繁的回归测试
     	2. 在开发过程中给开发人员快速反馈
     	3. 几乎无限的测试用例执行迭代
     	4. 纪律的测试用例文档
     ```

  2. 举个栗子

     > 保险金融业务

     ```
     假设有个保险系统，有块业务为投保业务。流程如下
     ```

      ```mermaid
      graph LR
      	建立保单 --> 保险人员投保鉴定
      	保险人员投保鉴定 --> 缴入第一笔保费
      	缴入第一笔保费 --> 按期缴费
      	按期缴费 --> 保全
         保全 --> 保险金理赔
         保险金理赔 --> 打印账票
      ```

     

     >  爬虫的应用

     ```
     1. 数据分析
        - 有些网站有时候理不清里面的JS代码，看不到所谓的后台接口，可能是以模板渲染的方式加载。
     2. 纯粹的http请求可能会被封IP
     ```

     

     >宅男必备给主播刷礼物的神器



## 2. Selenium环境安装

 - Python 安装 （包括pip）

   1. [[windows下面安装Python和pip终极教程](https://www.cnblogs.com/clover-siyecao/p/5693935.html)]

   2. ubuntu 下安装Python和pip

      [![Vp1ECt.png](https://t1.picb.cc/uploads/2019/03/23/Vp1ECt.png)](https://www.picb.cc/image/Vp1ECt)

      

      ```
      sudo apt-get install pip3
      pip3 install Selenium
      ```

- 安装浏览器驱动

  | 浏览器  | 驱动下载地址                                                 |
  | ------- | ------------------------------------------------------------ |
  | Chrome  | https://sites.google.com/a/chromium.org/chromedriver/downloads |
  | Edge    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
  | Firefox | https://github.com/mozilla/geckodriver/releases              |
  | Safari  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |

  > 以火狐浏览器的驱动为例，在github下载对应的系统位数。

  ```
  Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires [geckodriver](https://github.com/mozilla/geckodriver/releases), which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.
  
  Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.
  ```

  ![Vp1Ysr.png](https://t1.picb.cc/uploads/2019/03/23/Vp1Ysr.png)

  ```
  from selenium import webdriver
  
  driver = webdriver.Firefox()   # Firefox浏览器
  
  driver = webdriver.Chrome()    # Chrome浏览器
  
  driver = webdriver.Ie()        # Internet Explorer浏览器
  
  driver = webdriver.Edge()      # Edge浏览器
  
  driver = webdriver.Opera()     # Opera浏览器
  ```

  > [window驱动安装请参考](http://www.testclass.net/selenium_python/selenium3-browser-driver)



## 3. Selenium的元素定位

 + #### Selenium提供了8种定位方式:

   1. id
   2. name
   3. class name
   4. tag name
   5. link text
   6. partial link text
   7. xpath
   8. css selector

   

 + #### 定位元素的8种方式

   | 定位一个元素                      | 定位多个元素                       | 含义                  |
   | --------------------------------- | ---------------------------------- | --------------------- |
   | find_element_by_id                | find_elements_by_id                | 通过元素id定位        |
   | find_element_by_name              | find_elements_by_name              | 通过元素name定位      |
   | find_element_by_xpath             | find_elements_by_xpath             | 通过xpath表达式定位   |
   | find_element_by_link_text         | find_elements_by_link_tex          | 通过完整超链接定位    |
   | find_element_by_partial_link_text | find_elements_by_partial_link_text | 通过部分链接定位      |
   | find_element_by_tag_name          | find_elements_by_tag_name          | 通过标签定位          |
   | find_element_by_class_name        | find_elements_by_class_name        | 通过类名进行定位      |
   | find_elements_by_css_selector     | find_elements_by_css_selector      | 通过css选择器进行定位 |

   > xpath要对DOM结构有一定了解，所以比较难。可以参考[菜鸟教程xpath](http://www.runoob.com/xpath/xpath-tutorial.html)



## 4. Selenium的API

	> [摘自](https://blog.csdn.net/weixin_36279318/article/details/79475388)

 + 控制浏览器操作的一些方法

   | 方法                | 说明                   |
   | ------------------- | ---------------------- |
   | set_window_size()   | 设置浏览器的大小       |
   | back()              | 控制浏览器后退         |
   | forward()           | 控制浏览器前进         |
   | refresh()           | 刷新当前页面           |
   | clear()             | 清除文本               |
   | send_keys (value)   | 模拟按键输入           |
   | click()             | 单击元素               |
   | submit()            | 用于提交表单           |
   | get_attribute(name) | 获取元素属性值         |
   | is_displayed()      | 设置该元素是否用户可见 |
   | size                | 返回元素的尺寸         |
   | text                | 获取元素的文本         |

+ #### 鼠标事件

  | 方法                   | 说明                                                         |
  | ---------------------- | ------------------------------------------------------------ |
  | ActionChains(driver)   | 构造ActionChains对象                                         |
  | context_click()        | 执行鼠标悬停操作                                             |
  | move_to_element(above) | 右击                                                         |
  | double_click()         | 双击                                                         |
  | drag_and_drop()        | 拖动                                                         |
  | move_to_element(above) | 执行鼠标悬停操作                                             |
  | context_click()        | 用于模拟鼠标右键操作， 在调用时需要指定元素定位              |
  | perform()              | 执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作 |

+ #### 多表单切换

  | 方法                        | 说明                                               |
  | --------------------------- | -------------------------------------------------- |
  | switch_to.frame()           | 将当前定位的主体切换为frame/iframe表单的内嵌页面中 |
  | switch_to.default_content() | 跳回最外层的页面                                   |

+ #### 警告框处理

  | 方法                  | 说明                                               |
  | --------------------- | -------------------------------------------------- |
  | text                  | 返回 alert/confirm/prompt 中的文字信息             |
  | accept()              | 接受现有警告框                                     |
  | send_keys(keysToSend) | 发送文本至警告框。keysToSend：将文本发送至警告框。 |

+ #### 窗口截图

  | 方法                                   | 说明                                 |
  | -------------------------------------- | ------------------------------------ |
  | get_screenshot_as_file(self, filename) | 用于截取当前窗口，并把图片保存到本地 |

## 5. Selenium使用Demo

 +  元素定位

   > 准备html放入web容器中，如ngnix，tomcat

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8">
       <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
       <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
       <link rel="stylesheet" href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
   
   </head>
   <body>
       <div class="jumbotron">
           <h1>Selenium Api 练习</h1>
           <p>学的不仅是技术，更是梦想！！！</p>
       </div>
   
       <hr>
       <h2>元素选择, 点击事件练习</h2>
       <button type="button" class="btn btn-primary" onclick="alert('通过元素id定位')" id="main">通过元素id定位</button>
       <button type="button" class="btn btn-secondary" onclick="alert('通过元素name定位')" name="next">通过元素name定位</button>
       <button type="button" class="btn btn-success" onclick="alert('通过xpath表达式定位')">通过xpath表达式定位</button>
       <a type="button" class="btn btn-info" onclick="alert('通过完整超链接定位')">通过完整超链接定位</a>
       <a type="button" class="btn btn-warning" onclick="alert('通过部分链接定位')">通过部分链接定位</a>
       <span type="button" class="btn btn-danger" onclick="alert('通过span标签定位')">通过span标签定位</span>
       <button type="button" class="btn btn-dark" onclick="alert('通过类名进行定位')">通过类名进行定位</button>
       <a class="btn btn-light btn-lg" title="css" onclick="alert('通过css选择器进行定位')">通过css选择器进行定位</a>
   
   </body>
   </html>
   ```

   > 效果图如下

   ![VpqdPt.png](https://t1.picb.cc/uploads/2019/03/24/VpqdPt.png)

   > Python + selenium 代码如下

   ```python
   from selenium import webdriver
   
   import time
   
   
   # 处理弹出框函数
   def alert_process():
       # 获取弹出框
       dig_alert = browser.switch_to.alert
       time.sleep(1)
       # 打印警告对话框内容
       print(dig_alert.text)
       # alert对话框属于警告对话框，接受弹窗
       dig_alert.accept()
       time.sleep(1)
   
   
   if __name__ == '__main__':
       # 加载驱动
       browser = webdriver.Firefox()
       # 打开网页地址
       browser.get("http://localhost/ats_kimi/demo_api.html")
       time.sleep(1)
   
       try:
           # 通过元素id定位
           id2 = browser.find_element_by_id('main')
           id2.click()
           time.sleep(1)
           alert_process()
   
           # 通过元素name定位
           next = browser.find_element_by_name('next')
           next.click()
           time.sleep(1)
           alert_process()
   
           # 通过xpath表达式定位
           xpath = browser.find_element_by_xpath('/html/body/button[3]')
           xpath.click()
           time.sleep(1)
           alert_process()
   
           # 通过完整超链接定位
           link = browser.find_element_by_link_text('通过完整超链接定位')
           link.click()
           time.sleep(1)
           alert_process()
   
           # 通过部分链接定位
           link2 = browser.find_element_by_partial_link_text('部分链接')
           link2.click()
           time.sleep(1)
           alert_process()
   
           # 通过span标签定位
           span = browser.find_element_by_tag_name('span')
           span.click()
           time.sleep(1)
           alert_process()
   
           # 通过类名进行定位
           classType = browser.find_element_by_class_name('btn-dark')
           classType.click()
           time.sleep(1)
           alert_process()
   
           # 通过css选择器进行定位
           css = browser.find_element_by_css_selector('a[title=\"css\"]')
           css.click()
           time.sleep(1)
           alert_process()
   
           browser.quit()
       except:
           print('error, quit browser')
           browser.quit()
       else:
           print('done')
   ```



 + 爬取网页内容生成到excel中

   > 包含excel的html代码

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
       <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
       <link rel="stylesheet" href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
   </head>
   <body>
   <div class="container">
       <div class="jumbotron">
           <h1>Selenium demo </h1>
           <p>学的不仅是更是梦想，更是哲学！！！</p>
       </div>
       <table class="table table-hover" id="table">
   
           <tr>
               <td>hello1</td>
               <td>world1</td>
               <td>selenium1</td>
               <td>test1</td>
           </tr>
           <tr>
               <td>hello2</td>
               <td>world2</td>
               <td>selenium2</td>
               <td>test2</td>
           </tr>
           <tr>
               <td>hello3</td>
               <td>world3</td>
               <td>selenium3</td>
               <td>test3</td>
           </tr>
       </table>
   </div>
   </body>
   </html>
   ```

   > 效果图如下

   ![VpvJe1.png](https://t1.picb.cc/uploads/2019/03/24/VpvJe1.png)

   > python + selenium 代码如下

   ```python
   from selenium import webdriver
   from re import findall
   from openpyxl import Workbook
   
   import time
   
   # 加载驱动
   browser = webdriver.Firefox()
   # 打开网页地址
   browser.get("http://localhost/ats_kimi/demo_excel.html")
   
   try:
       time.sleep(1)
       # 获取table
       table = browser.find_element_by_id('table')
       # 获取table内容
       content = table.get_attribute('innerHTML')
   
       # 正则表达式匹配
       pattern = r'<tr>' + r'(.|\n)*?<td>(.*?)</td>' * 4 + r'(.|\n)*?</tr>'
       # 查找结果
       result = findall(pattern, content)
   
       print(result)
   except:
       print('error')
       browser.quit()
   else:
       print('done')
   
   # 创建空白的excel文件
   wb = Workbook()
   # 工作表1
   ws = wb.worksheets[0]
   
   # 把网页上爬到的数据写入excel文件
   for line in result:
       line = [line[1], line[3], line[5], line[7]]
       ws.append(line)
   
   # 保存到excel中
   wb.save('../output/demo_excel.xlsx')
   ```

   

 + 实现网页上的简单操作并截图（TPMS）

   > python + selenium代码

   ```ptyhon
   from selenium import webdriver
   
   import time
   
   browser = webdriver.Firefox()
   
   browser.get("http://localhost/tpms_dev/login.php")
   
   # 获取登录名和密码
   input_name = browser.find_element_by_name('tl_login')
   input_pass = browser.find_element_by_name('tl_password')
   
   # 清空登录名和密码
   input_name.clear()
   input_pass.clear()
   
   # 输入账号和密码
   input_name.send_keys('Zhao Tianer')
   input_pass.send_keys('password')
   
   # 点击登录按钮
   button_submit = browser.find_element_by_name('login_submit')
   button_submit.click()
   
   # browser.implicitly_wait(3)
   
   # browser.get_screenshot_as_file('./hello.png')
   
   # 选择title bar frame
   browser.switch_to.frame('titlebar')
   
   # 选中链接
   admin = browser.find_element_by_link_text('Administration')
   admin.click()
   
   time.sleep(10)
   
   # 跳出frame
   browser.switch_to.default_content()
   # 选择主界面的frame
   browser.switch_to.frame(browser.find_element_by_name('mainframe'))
   
   # 选中zhulin的链接
   link = browser.find_element_by_link_text('Zhu Lin')
   browser.execute_script("arguments[0].scrollIntoView();", link)
   
   link.click()
   
   # 在firstname输入stack
   firstName = browser.find_element_by_name('firstName')
   firstName.send_keys('Stack')
   
   # 在last name输入john snow
   lastName = browser.find_element_by_name('lastName')
   lastName.send_keys('John Snow')
   
   # 截图
   browser.get_screenshot_as_file('./done.png')
   
   time.sleep(5)
   
   # 点击更新按钮
   doUpdate = browser.find_element_by_name('do_update')
   doUpdate.click()
   
   browser.close()
   ```

   









