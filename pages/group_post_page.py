import os
# from pages.base_page import BasePage
# from utils import locators
# from utils import testcase_data
# from utils.openpyxlfunction import *
from time import sleep
from datetime import datetime
from pathlib import Path
from pages.signin_page import *



class GroupPost(BasePage):
    def __init__(self, driver):
        self.locator = locators.PostingLocators
        self.count = 0
        self.sign_in_locator = locators.SignInPageLocator
        self.sign_in_count = 0
        super(GroupPost, self).__init__(driver)

    def accept_alert_message(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            print("No alert found")

    def group_posting(self, message):
        # all the variable which you have to change according to your need
        # sheetpath = Path(__file__).parent.parent / "utils/hr_grouplist.xlsx"
        sheetpath = Path(__file__).parent.parent / "utils/hr_grouplist.xlsx"
        print("*" * 80)
        print(sheetpath)
        # imagepath = os.getcwd() + "\image\hire.png"
        imagepath = os.getcwd() + "\image\newHire.png"
        datacounterpath = Path(__file__).parent.parent / "utils/datacounter.txt"
        allsheetname = allsheetName(sheetpath)
        images_list = [imagepath]
        datacounter = readWrite(datacounterpath)
        sheetcount = len(allsheetname)
        for i in range(3, sheetcount):
            sheetname = allsheetname[i]
            print(i)
            # sheetname = "ihealthcare"
            groups_links_list = readallsheetdataurl(sheetpath, sheetname, 2, 3)
            print("this is a group list {0}".format(groups_links_list))
            # Post on each group
            for group in groups_links_list:
                print("this is group link{0}".format(group))
                i = readWrite(datacounterpath) + 1
                self.driver.get(group)
                sleep(2)
                self.accept_alert_message()
                try:
                    for photo in images_list:
                        photo_element = self.driver.find_element(*self.locator.imageInput)
                        photo_element.send_keys(photo)

                    sleep(2)
                    try:
                        post_box = self.driver.find_element(*self.locator.postbox)
                        post_box.click()
                        sleep(2)
                        message.encode('utf-8')
                        message2 = message + "\n" + "Post Id:" + str(i) + "\n"

                        post_box.send_keys(message2)
                        sleep(2)
                        post_button = self.driver.find_element(*self.locator.postbutton)
                        post_button.click()
                        sleep(20)
                        errorData = [i, f"Posted->Done grouplink: {group}", str(datetime.now()), "No issues"]
                        writecol(sheetpath, testcase_data.log, i, errorData)
                    except:
                        # clicking Post button
                        errorData = [i, f"grouplink: {group} couldn't post ", str(datetime.now()), "Post Blocking off"]
                        writecol(sheetpath, testcase_data.log, i, errorData)
                except:
                    print("No input field found.")
                    errorData = [str(i), f"grouplink: {group}not posted due to blocked issue", str(datetime.now()),
                                 "not posted"]
                    writecol(sheetpath, testcase_data.log, i, errorData)
                self.count = self.count + 1
                print(self.count)
                if self.count == 50:
                    self.count = 0
                    # self.sign_in.switch_account(self, self.sign_in_count)
                    self.switch_account(self.sign_in_count)
                    print("*" * 80)
                    print(self.sign_in_count)
                    self.sign_in_count = self.sign_in_count + 1

    def signIn(self, email, password):
        self.find_element2(*self.sign_in_locator.email).send_keys(email)
        self.find_element2(*self.sign_in_locator.password).send_keys(password)
        self.find_element2(*self.sign_in_locator.signInBtn).click()

    def click_account_button(self):
        self.click(*self.sign_in_locator.account_button)

    def click_log_out_button(self):
        self.click(*self.sign_in_locator.log_out_button)

    def switch_account(self, i):
        self.click_account_button()
        print("click on account")
        self.click_log_out_button()
        print("click on click_log_out_button")
        self.accept_alert_message()
        sleep(10)
        self.signIn(testcase_data.account[i], testcase_data.password[i])

    def post(self):
        self.group_posting(testcase_data.group_post_message)
