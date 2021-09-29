from pages.signin_page import SignInPage
from functionality.base_test import BaseTest
from pages.group_post_page import GroupPost
from pages.PeopleList import PeopleList
from pages.friend_request_send import SendingFriendRequest

class TestVerifysignin(BaseTest):

    def test_signin(self):
        page_signin = SignInPage(self.driver)
        page_signin.signin()
        page3 = PeopleList(self.driver)
        page3.collect()


# python3 -m unittest functionality.test1
# python3 -m pytest -s functionality/test_functionality_Facebook.py --alluredir=ReportAllure &&  allure serve ReportAllure/
