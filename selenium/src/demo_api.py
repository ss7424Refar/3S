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

