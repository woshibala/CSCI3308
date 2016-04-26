from django.test import TestCase
from article.models import User,Article
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='user1', email='user1@example.com',password='123')
        User.objects.create(username='user2', email='user2@example.com',password='123')

    def test_User(self):
        user1 = User.objects.get(email='user1@example.com')
        user2 = User.objects.get(email='user2@example.com')
        self.assertEqual(user1.username, 'user1')
        self.assertEqual(user2.password, '123')

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="title1",category="category1",content="content1")
        Article.objects.create(title="title2",category="category2",content="content2")
        

    def test_Article(self):
        article1 = Article.objects.get(title='title1')
        article2 = Article.objects.get(title='title2')
        self.assertEqual(article1.title, 'title1')
        self.assertEqual(article2.content, 'content2')
