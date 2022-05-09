from django.db import models

from django.utils import timezone

# Create your models here.
class Author(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    author_firstname = models.CharField(max_length=150)
    author_lastname = models.CharField(max_length=150)
    author_avatar = models.CharField(max_length=150)
    author_bio = models.CharField(max_length=1000, null=True)
    author_profile_picture = models.ImageField(upload_to='authors', default="authors/default.gif", null=True)
    
    def __str__(self):
        return self.author_avatar

class Post_Category(models.Model):
    class Meta:
        verbose_name_plural = "post_categories"
    category_id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=150)
    post_date = models.DateTimeField()
    post_categories = models.ManyToManyField(Post_Category)

    def __str__(self):
        return self.post_title

class Post_Section(models.Model):
    SECTION_NUMBERS = [
        (1, "Part 1"),
        (2, "Part 2"),
        (3, "Part 3"),
        (4, "Part 4"),
        (5, "Part 5"),
        (6, "Part 6"),
        (7, "Part 7"),
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    section_number = models.IntegerField(choices=SECTION_NUMBERS)
    heading = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="blog", blank=True)

# class Comment(models.Model):
#     comment_id = models.BigAutoField(primary_key=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=500)
#     comment_authorname = models.CharField(max_length=150)
#     comment_email = models.EmailField()
#     comment_date = models.DateField()
    

# class Comment_Reply(models.Model):
#     reply_id = models.BigAutoField(primary_key=True)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     reply = models.CharField(max_length=500)
#     reply_author = models.CharField(max_length=200)
#     reply_email = models.EmailField()
#     reply_date = models.DateField()

# class Post_Image(models.Model):
#     post_image_id = models.BigAutoField(primary_key=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     post_image_title = models.CharField(max_length=150)
#     post_image = models.ImageField()
