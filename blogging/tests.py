""" blogging tests script """

# imports
import datetime
from django.utils.timezone import utc

from django.test import TestCase
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.urls import reverse

from blogging.models import Post, Category
# -----------------------------------------


class SimpleTest(TestCase):
    """ tests if the page actually exists """
    def test_list_view_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
# -----------------------------------------


class PostTestCase(TestCase):
    """ PostTest """
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        """ setup """
        self.user = User.objects.get(pk=1)
        self.post = Post(
            title="test title",
            text="nice text content",
            author=self.user,)
        
    def test_string_representation(self):
        """ test string for post """
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
    
    def test_post_content(self):
        """ test content for post """
        self.assertEqual(f"{self.post.title}", "test title")
        self.assertEqual(f"{self.post.text}", "nice text content")
        self.assertEqual(f"{self.post.author}", "admin")

    def test_no_post_detail_view(self):
        """ test post detail view"""
        no_response = self.client.get("/posts/100000/")
        self.assertEqual(no_response.status_code, 404)
        
# -----------------------------------------

    
class CategoryTestCase(TestCase):
    """ CategoryTest """
    def test_string_representation(self):
        """ test string for category """
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)
# -----------------------------------------


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogging/fixtures/blogging_test_fixture.json', ]

    def setUp(self):
        """ set up """
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        """ test list published """
        resp = self.client.get('/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        
        #self.assertTrue("Recent Posts" in resp_text)
        self.assertFalse("Recent Posts" in resp_text)
        
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=2) #count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        """ test details published """
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
