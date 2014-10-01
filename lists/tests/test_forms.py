from django.test import TestCase

from lists.forms import EMPTY_LIST_ERROR, ItemForm

class ItemFormTest(TestCase):
    """docstring for ItemFormTest"""

    def test_form_reders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blanck_items(self):
        form =ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_LIST_ERROR]
        )
