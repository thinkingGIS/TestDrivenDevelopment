from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
# class SmokeTest(TestCase):
#     """docstring for SmokeTest
#     Stupid Test to fail
#     """

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):
    """docstring for HomePageTest
    We test 2 things:
    - Can we resolve the URL for the root of the site("/") to a particular
        view function we´ve made?
    - Can we make this function return some HTML which will get the functional test to pass?
    """

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html', 
            {'new_item_text': 'A new list item'}
            )
        self.assertEqual(response.content.decode(), expected_html)
        pass