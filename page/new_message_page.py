from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class NewMessagePage(BaseAction):

    # 接收者
    phone_edit_text = By.XPATH, "//*[@text='接收者']"
    # 键入信息
    message_edit_text = By.XPATH, "//*[@text='键入信息']"
    # 发送
    send_button = By.XPATH, "//*[@content-desc='发送']"

    @allure.step(title='新建短信 - 输入 手机号')
    def input_phone(self, content):
        allure.attach('输入手机号', content)
        self.input(self.phone_edit_text, content)

        # allure.attach("输入手机号", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

        # 截图保存在 image文件夹 中
        self.screen_shot("xx.png")
        # 将 image文件夹中 的 图片 添加到报告上
        self.allure_pic_with_local("截图：", "xx.png")

    @allure.step(title='新建短信 - 输入 信息')
    def input_message(self, content):
        allure.attach('输入信息', content)
        self.input(self.message_edit_text, content)

    @allure.step(title='新建短信 - 点击 发送')
    def click_send(self):
        self.click(self.send_button)
