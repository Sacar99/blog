import email
from multiprocessing import context
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.user.password, "secret")
        self.assertEqual(self.user.email, "test@email.com")
        self.assertEqual(self.post.get_absolute_url(), "/topic/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/topic/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("blog:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "base.html", "index.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("blog:post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/topic/188888/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")

        

