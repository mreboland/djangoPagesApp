# We use SimpleTestCase here since we aren't using a database. If we were using a db, we'd instead use TestCase.
from django.test import SimpleTestCase

# Here we are performing a check if the status code for each page is 200, which is the standard response code for a successful HTTP request.
# We run the test by typing 'python manage.py test' in the cmd line
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        # client.get returns a promise for a client (executable context) matching a given id. The id is the webpage in this case which we save to a variable.
        response = self.client.get("/")
        # The promise has a key of status_code and we are checking if it's value is equal (assetEqual) to 200 which we provided as the second argument.
        self.assertEqual(response.status_code, 200)
        
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)