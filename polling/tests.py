from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from polling.models import Poll

class PollTestCase(TestCase):

    def setUp(self):
        self.poll = Poll.objects.create(
                title = "a simple poll",
                text = "mushrooms are weird",
                score = 0)
    
    def test_string_representation(self):
        poll = Poll(title="a simple poll")
        self.assertEqual(str(poll), poll.title)

    def test_poll_content(self):
        self.assertEqual(f'{self.poll.title}', "a simple poll")
        self.assertEqual(f'{self.poll.text}', 'mushrooms are weird')
        self.assertEqual(f'{self.poll.score}', '0')

    def test_poll_list_view(self):
        response = self.client.get(reverse('poll_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polling/list.html')

    def test_poll_detail_view(self):
        response = self.client.get('/polling/polls/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mushrooms are weird')
        self.assertTemplateUsed(response, 'polling/detail.html')

