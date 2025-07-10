# Test authorization
# Need a unit test for fail cases
from django.test import TestCase, RequestFactory, override_settings
from unittest.mock import patch, MagicMock
from auth_app.views import whoami
import json

# Need test fail auth
@override_settings(DB_JWT_SECRET="fake-secret")
class AuthUserTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
    
    #@patch("auth_app.views.supabase")
    @override_settings(DB_JWT_SECRET="fake-secret")
    def test_invalid_auth(self):
        request = self.factory.get(
            "/auth_user/", 
            **{"HTTP_AUTHORIZATION": "Bearer my.jwt.token"}
        )
        response = whoami(request)
        data = json.loads(response.content)

        print(data)
        self.assertEqual(response.status_code, 401)
       # self.assertIn("user_id", data)

    @patch("auth_app.utils.jwt.decode")
    def test_auth_user(self, mock_jwt_decode):
        # Pretend the decoded token returns a valid payload
        mock_jwt_decode.return_value = {
            "sub": "user123",
            "email": "test@example.com"
        }

        request = self.factory.get(
            "/auth_user/",
            **{"HTTP_AUTHORIZATION": "Bearer fake.jwt.token"}
        )

        response = whoami(request)
        data = json.loads(response.content)

        print(data)  # Will output {'user_id': 'user123', 'email': 'test@example.com'}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["user_id"], "user123")
        self.assertEqual(data["email"], "test@example.com")