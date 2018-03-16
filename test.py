import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GithubSearchTest(unittest.TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://167.99.49.144:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_github_repo_search(self):
        browser = self.browser
        browser.get('https://github.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)  # simulate long running test
        self.assertIn('Search more than', browser.page_source)

    def test_github_repo_search_for_selenium(self):
        browser = self.browser
        browser.get('https://github.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)  # simulate long running test
        self.assertIn('repository results', browser.page_source)

    def test_github_repo_search_for_testdriven(self):
        browser = self.browser
        browser.get('https://github.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)  # simulate long running test
        self.assertIn('testdriven', browser.page_source)

    def test_github_repo_search_with_no_results(self):
        browser = self.browser
        browser.get('https://github.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('?*#^^%')
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)  # simulate long running test
        self.assertIn(
            'We couldn’t find any repositories matching',
            browser.page_source
        )

    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()
