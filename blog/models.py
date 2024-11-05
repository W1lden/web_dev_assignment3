from django.db import models
from django.contrib.auth.models import User
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_date__isnull=False)

    def by_author(self, author):
        return self.get_queryset().filter(author=author)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    objects = models.Manager()
    published = PublishedPostManager()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"