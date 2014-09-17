from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
# import unittest

class NewVisitorTest(LiveServerTestCase):
    """docstring for NewVisitorTest"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invitedto enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-Do item'
            )

        # She types " Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a todo-list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table Madafaka! -- its text was:\n%s" % (
        #         table.text,
        #         )
        #     )
        #self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # The is still a text box inviting her to add another item. She 
        # enters "Use peacock feathers to make a fly" (Edith is very 
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        #     )

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she see 
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test Madafaka!')

        # She visits that URL - her to-to list is still there.

        # Satisfied, she goes back to sleep
