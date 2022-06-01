from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username": "test", "password": "test"}
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


UserModel = get_user_model()


class TestProductListCreateAPIView(APITestCase):
    def authenticate(self):
        data = {"username": "test", "password": "test"}
        UserModel.objects.create_superuser(
            username="test",
            password="test"
        )
        auth_token = self.client.post('/api/auth/', data).data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {auth_token}')

    def test_should_not_create_product_with_no_auth(self):
        sample_product = {
            "name": "test",
            "price": 0.00
        }

        response = self.client.post('/api/products/', sample_product)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_create_product(self):
        self.authenticate()

        sample_product = {
            "name": "test",
            "price": 0.00
        }

        response = self.client.post('/api/products/', sample_product)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_delete_product(self):
        self.authenticate()

        sample_product = {
            "name": "test",
            "price": 0.00
        }

        response = self.client.post('/api/products/', sample_product)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        product_id = response.data['id']
        delete_response = self.client.delete(
            f'/api/products/{product_id}/delete/', sample_product)

        self.assertEqual(delete_response.status_code,
                         status.HTTP_204_NO_CONTENT)

    def test_should_rate_product(self):
        self.authenticate()

        sample_product = {
            "name": "test",
            "price": 0.00
        }

        response = self.client.post('/api/products/', sample_product)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product_id = response.data['id']
        data = {
            "product_id": product_id,
            "rating": 5
        }

        rating_response = self.client.post('/api/products/rating/', data)

        self.assertEqual(rating_response.status_code,
                         status.HTTP_201_CREATED)

        product_rating = self.client.get(
            f'/api/products/{product_id}/').data['rating']

        self.assertEqual(product_rating, '5.00')
