from appium import webdriver
from conftest import MakeDriver


class TestTwitter(object):

    def test_like_something(self: 'TestTwitter', make_driver: MakeDriver) -> None:
        d: webdriver.Remote = make_driver("twitter")
        print(d.page_source)
