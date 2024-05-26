from django.test import TestCase
from .models import Post

# Create your tests here.


class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(title="testing post", slug="testing", body="a post to test")
        Post.objects.create(
            title="testing post 2", slug="testing2", body="a post to test 2"
        )

    def test_post_properties(self):
        post = Post.objects.get(title="testing post")
        self.assertEqual(post.title, "testing post")
        self.assertEqual(post.slug, "testing")
        self.assertEqual(post.body, "a post to test")

    def test_post_default_retrieval_order(self):
        posts = Post.objects.all()
        self.assertEqual(posts[0].title, "testing post 2")
        self.assertEqual(posts[1].title, "testing post")
