import unittest
from django.test import TestCase
from hu.models import Task
from django.contrib.auth.models import User

class test_get_task(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="priyanka",password="123",email = "asd@gmail.com")
        Task.objects.create(task_name="Task test", user_name = self.user,task_visibility="0")

    def test_check_if_saved(self):
        tasks = Task.objects.filter(user_name = self.user)
        self.assertEqual(len(tasks), 1, 'the task was not saved')
