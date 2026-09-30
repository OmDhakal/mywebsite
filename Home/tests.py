from django.test import TestCase

from .models import ContactMessage


class ContactFormTests(TestCase):
    def test_contact_form_saves_message(self):
        response = self.client.post(
            '/contact/',
            {
                'name': 'Jane Doe',
                'email': 'jane@example.com',
                'subject': 'Hello',
                'message': 'I would like to get in touch.',
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'OK')
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.get().subject, 'Hello')

    def test_contact_form_rejects_invalid_data(self):
        response = self.client.post(
            '/contact/',
            {
                'name': 'Jane Doe',
                'email': 'not-an-email',
                'subject': 'Hello',
                'message': 'I would like to get in touch.',
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_contact_endpoint_rejects_get(self):
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 405)
