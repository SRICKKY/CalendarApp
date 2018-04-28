from django.test import TestCase
from .models import Entry
from django.contrib.auth.models import User
from django.utils import timezone

class TestEntry(TestCase):

	def setUp(self):
		self.entry = Entry(name='name',
				author=User.objects.create(),
				date=timezone.now(),
				description="This should be a long description"
			)

	def test_short_description(self): 
		self.assertEqual(self.entry.short_description, 'This')
