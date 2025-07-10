# Test fetching announcements
# Digest

#from unittest import TestCase, RequestFactory
from django.test import TestCase, RequestFactory
from unittest.mock import patch, MagicMock
from announcements_sync.models import Announcement
from announcements_sync.views import get_announcements
import json

'''

Not sure if this works or is necessary

class AnnouncementModelTest(TestCase):
    @patch("announcements_sync.models.Announcement.objects")
    def test_get_recent_announcements(self, mock_objects):
        # Arrange: fake queryset
        mock_announcement = Announcement(
            id=1, title="Test", body="Body", created_at="2025-07-09"
        )
        mock_objects.order_by.return_value = [mock_announcement]

        # Act
        result = Announcement.objects.order_by("-created_at")

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Test")
'''

# This is an integration test it doesn't use patch so it hits the real Supabase DB
# Slower due to the nature of integration tests
class FetchAnnouncementsViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def testViews(self):
        request = self.factory.get("/get_announcements/")
        response = get_announcements(request)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertIn("announcements", data)
        self.assertEqual(len(data["announcements"]), 2) # right now theres only 2 announcements change as needed
        print(data)


'''

Sample untested unit test with mock objects with fail case (not implemented yet)

class GetAnnouncementsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("announcements_sync.views.supabase")
    def test_get_announcements_success(self, mock_supabase):
        # Arrange: fake supabase response
        mock_data = MagicMock()
        mock_data.data = [
            {"id": 1, "title": "Test", "body": "Hello", "created_at": "2025-07-09T12:00:00Z"}
        ]
        mock_supabase.table.return_value.select.return_value.order.return_value.execute.return_value = mock_data

        # Act
        request = self.factory.get("/get_announcements/")
        response = get_announcements(request)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("announcements", response.json())
        self.assertEqual(len(response.json()["announcements"]), 1)

    @patch("announcements_sync.views.supabase")
    def test_get_announcements_failure(self, mock_supabase):
        # Arrange: simulate exception
        mock_supabase.table.side_effect = Exception("Database error")

        # Act
        request = self.factory.get("/get_announcements/")
        response = get_announcements(request)

        # Assert
        self.assertEqual(response.status_code, 500)
        self.assertIn("error", response.json())
'''