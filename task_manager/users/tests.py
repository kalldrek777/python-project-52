from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import CustomUser
from task_manager.read_json import get_json_data


# Create your tests here.
class TestUsersCrud(TestCase):
    filename = 'users.json'

    def setUp(self):
        self.user_data = get_json_data(self.filename)
        CustomUser.objects.create(
            first_name=self.user_data['user1']['first_name'],
            last_name=self.user_data['user1']['last_name'],
            username=self.user_data['user1']['username'],
            password=self.user_data['user1']['password1'],
            # self.user_data['user1']
        )

    def test_singUp(self):
        responce = self.client.get(reverse('users:create_page'))
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='users/register.html')

        responce = self.client.post(reverse('users:create_page'),
                                    self.user_data['user2']
                                    )

        self.assertEqual(responce.status_code, 302)
        self.assertRedirects(responce, reverse('login_page'))

        user = CustomUser.objects.first()
        self.assertEqual(user.first_name, "Denis")
        self.assertEqual(user.last_name, "Ivanov")
        self.assertEqual(user.username, "dench")

        user = CustomUser.objects.last()
        self.assertEqual(user.first_name, "Ivan")
        self.assertEqual(user.last_name, "Leshev")
        self.assertEqual(user.username, "ivlesh")

        responce = self.client.get(reverse('users:index_page'))
        self.assertTrue(len(responce.context['users']) == 2)
