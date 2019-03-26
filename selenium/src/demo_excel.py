from selenium import webdriver
from re import findall
from openpyxl import Workbook

import time

# 加载驱动
browser = webdriver.Firefox()
# 打开网页地址
browser.get("http://localhost/demo_excel.html")
# 设置窗口最大化
browser.maximize_window()
time.sleep(1)

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
    browser.quit()

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