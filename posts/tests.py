from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create user
        testuser1 = User.objects.create_user(username = 'usertest1', password = 'abcd1234')
        testuser1.save()
        test_post1 = Post.objects.create(author = testuser1, title = 'title test', body = 'body test ..... ')
        test_post1.save()
        
    def test_blog_content(self):
        post = Post.objects.get(id=1)  
        author = f'{post.author}' 
        title = f'{post.title}'
        body = f'{post.body}'
        
        self.assertEqual(author, 'usertest1')
        self.assertEqual(title, 'title test') 
        self.assertEqual(body, 'body test ..... ')
        
        
    