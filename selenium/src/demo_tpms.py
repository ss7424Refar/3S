from selenium import webdriver

import time

browser = webdriver.Firefox()

browser.get("http://localhost/tpms_dev/login.php")
# 设置窗口最大化
browser.maximize_window()
time.sleep(1)

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
browser.get_screenshot_as_file('../output/done.png')

time.sleep(5)

# 点击更新按钮
doUpdate = browser.find_element_by_name('do_update')
doUpdate.click()

browser.close()
