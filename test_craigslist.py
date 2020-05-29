from pages import GetStartedPage
from conftest import MakeDriver


class TestCraigslist(object):

    def test_max_price_filter(self: 'TestCraigslist', make_driver: MakeDriver) -> None:
        driver = make_driver("craigslist")
        max_price = 2000
        get_started = GetStartedPage.instance(driver)
        loc_perms = get_started.get_started()
        choose_loc = loc_perms.share_location()
        search = choose_loc.choose_location('Vancouver, BC', typed_location='vancouver')
        results = search.browse_category('housing', 'apts/housing for rent')
        results.filter_max_price(max_price)
        prices = results.get_prices()
        for price in prices:
            assert price <= max_price
