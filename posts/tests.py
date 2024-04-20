from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # def test_url_available_by_name(self):
    #     response = self.client.get(reverse("posts"))
    #     self.assertEqual(response.status_code, 200)

    # def test_correct_template_used(self):
    #     response = self.client.get(reverse("posts"))
    #     self.assertTemplateUsed(response, "home.html")

    # def test_correct_content_present(self):
    #     response = self.client.get(reverse("posts"))
    #     self.assertContains(response, "This is a test!")

    def test_homepage(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")
