from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='testuser@example.com',
            role='STDNT',
            password='testpass123'
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.role, 'STDNT')
        self.assertTrue(user.check_password('testpass123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            email='superuser@example.com',
            role='ADMIN',
            password='superpass123'
        )
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertEqual(superuser.role, 'ADMIN')
        self.assertTrue(superuser.check_password('superpass123'))
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
