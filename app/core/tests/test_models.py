from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch


def sample_user(email='test@live.se', password='Test1234Pass'):
    """Creates a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Tests creating a new user with an email is successful"""
        email = 'test@live.se'
        password = 'Test1234Pass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests the email for a new user is normalized"""
        email = 'test@LIVE.SE'
        user = get_user_model().objects.create_user(email, 'Test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Tests creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234')

    def test_create_new_superuser(self):
        """Tests creating a new superuser"""
        email = 'test@live.se'
        password = 'Test1234Pass'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Tests the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name='Vegan')
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Tests the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Tests the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and Mushroom Sauce',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Tests that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'my-image.jpg')
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
