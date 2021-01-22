from appium import webdriver
from conftest import MakeDriver
from pages import YTHomePage


class TestYoutube(object):

    def test_find_video_happypath(self: 'TestYoutube', make_driver: MakeDriver) -> None:
        driver: webdriver.Remote = make_driver('youtube')
        home = YTHomePage.instance(driver)
        search = home.search('making your appium tests fast & reliable')
        video = search.play_video('Making Your Appium Tests Reliable')
        cur_num_likes = video.get_num_likes()
        video.like()
        assert video.get_num_likes() > cur_num_likes
        video.pause()
        video.play()
        video.minimize()
        video.close()
        video.navigate_to_home()
