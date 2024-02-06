from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.utils import get_json_data
from django.urls import reverse


class TestStatusesCrud(TestCase):
    filename = 'users.json'

    def setUp(self):
        self.user_data = get_json_data(self.filename)
        CustomUser.objects.create(
            first_name=self.user_data['user1']['first_name'],
            last_name=self.user_data['user1']['last_name'],
            username=self.user_data['user1']['username'],
            password=self.user_data['user1']['password1'],
        )
        self.user = CustomUser.objects.get(first_name=self.user_data['user1']['first_name'])

        Status.objects.create(name='status1')
        Status.objects.create(name='status2')
        Status.objects.create(name='status3')

    def test_access(self):
        """Незалогинение пользователи получают редирект"""
        resp1 = self.client.get(reverse('statuses:create_page'))
        self.assertEqual(resp1.status_code, 302)
        resp2 = self.client.get(reverse('statuses:index_page'))
        self.assertEqual(resp2.status_code, 302)
        resp3 = self.client.get(reverse('statuses:update_page',
                                        kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)
        resp4 = self.client.get(reverse('statuses:delete_page',
                                        kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)
        """Залогинимся"""
        self.client.force_login(self.user)
        resp1 = self.client.get(reverse('statuses:create_page'))
        self.assertEqual(resp1.status_code, 200)
        resp2 = self.client.get(reverse('statuses:index_page'))
        self.assertEqual(resp2.status_code, 200)
        resp3 = self.client.get(reverse('statuses:update_page',
                                        kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 200)
        resp4 = self.client.get(reverse('statuses:delete_page',
                                        kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 200)

    def test_create_status(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('statuses:create_page'),
                                {'name': 'status4'}
                                )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(reverse(resp, 'status:index_page'))

        resp = self.client.get(reverse('statuses:index_page'))
        self.assertTrue(len(resp.context['statuses']) == 4)

    def test_update_status(self):
        s1 = Status.objects.all()[0]
        self.client.force_login(self.user)
        resp = self.client.post(reverse('statuses:update_page',
                                        kwargs={'pk': 1}),
                                {'name': 'updated_status'}
                                )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(reverse(resp, 'status:index_page'))
        s1.refresh_from_db()
        self.assertEqual(s1.name, 'updated_status')

    def test_delete_status(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse('statuses:delete_page',
                                        kwargs={'pk': 1})),
        self.assertRedirects(resp, reverse('statuses:index_page'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
