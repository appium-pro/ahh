# flake8: noqa

from pages.base_page import BasePage, Locator, ScrollDirection
from pages.zoom.meeting_page import MeetingPage, MeetingPageIOS
from pages.zoom.start_meeting_page import StartMeetingPage, StartMeetingPageIOS
from pages.notes.notes_page import NotesPage, NotesPageIOS
from pages.craigslist.search_results_page import SearchResultsPage
from pages.craigslist.search_page import SearchPage
from pages.craigslist.choose_loc_page import ChooseLocPage
from pages.craigslist.loc_perms_page import LocPermsPage
from pages.craigslist.get_started_page import GetStartedPage

# Twitter
from pages.twitter.profile_page import TwProfilePage
from pages.twitter.search_page import TwSearchPage
from pages.twitter.home_page import TwHomePage
from pages.twitter.login_page import TwLoginPage
from pages.twitter.splash_page import TwSplashPage

# YouMail
from pages.youmail.voicemail_page import YMVoicemailPage, YMVoicemailPageIOS
from pages.youmail.voicemails_page import YMVoicemailsPage, YMVoicemailsPageIOS

# YouTube
from pages.youtube.video_page import YTVideoPage
from pages.youtube.search_results import YTSearchResultsPage
from pages.youtube.home_page import YTHomePage

# IOS Weather
from pages.weather.weather_page import WeatherPage, WeatherPageIOS
from pages.weather.city_list_page import CityListPage, CityListPageIOS
