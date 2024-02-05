from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import CustomUser
from task_manager.utils import get_json_data


class TestUsersCrud(TestCase):
    filename = 'users.json'

    def setUp(self):
        self.user_data = get_json_data(self.filename)
        CustomUser.objects.create(
            first_name=self.user_data['user1']['first_name'],
            last_name=self.user_data['user1']['last_name'],
            username=self.user_data['user1']['username'],
            password=self.user_data['user1']['password1'],
        )
        CustomUser.objects.create(
            first_name=self.user_data['user3']['first_name'],
            last_name=self.user_data['user3']['last_name'],
            username=self.user_data['user3']['username'],
            password=self.user_data['user3']['password1'],
        )
        self.assertEqual(CustomUser.objects.count(), 2)

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
        self.assertTrue(len(responce.context['users']) == 3)

    def test_list_users(self):
        responce = self.client.get(reverse('users:index_page'))
        self.assertTrue(len(responce.context['users']) == 2)

    def test_update_user(self):
        user = CustomUser.objects.get(id=1)

        responce = self.client.get(reverse('users:update_page',
                                           kwargs={'pk': user.id}))
        self.assertEqual(responce.status_code, 302)
        self.assertRedirects(responce, reverse('login_page'))

        self.client.force_login(user)
        responce = self.client.get(reverse('users:update_page',
                                           kwargs={'pk': user.id}))
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='users/update.html')
        responce = self.client.post(reverse(
            'users:update_page', kwargs={'pk': user.id}),
            {
                'first_name': 'Petya',
                'last_name': 'Piter',
                'username': 'Petr1',
                'password1': 'lovePiter',
                'password2': 'lovePiter',
            }
        )
        self.assertEqual(responce.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Petya')

    def test_delete_user(self):
        user = CustomUser.objects.get(id=1)

        responce = self.client.get(reverse('users:delete_page',
                                           kwargs={'pk': user.id}))
        self.assertEqual(responce.status_code, 302)
        self.assertRedirects(responce, reverse('login_page'))

        self.client.force_login(user)
        responce = self.client.get(reverse('users:delete_page',
                                           kwargs={'pk': user.id}))
        self.assertEqual(responce.status_code, 200)

        resp = self.client.post(
            reverse('users:delete_page', kwargs={'pk': user.id})
        )
        self.assertRedirects(resp, reverse('users:index_page'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(CustomUser.objects.count(), 1)
