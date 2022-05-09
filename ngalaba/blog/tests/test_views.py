
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from blog.models import Post, Author, Post_Section
# Create your tests here.
def create_post(post_title):
    def create_author():
        fname = "Mebi"

        return Author.objects.create(author_firstname=fname, author_lastname=fname, author_avatar=fname)
    body="kwechiri boy!"

    return Post.objects.create(author = create_author(), post_title=post_title, post_date=timezone.now())

class PostIndexViewTests(TestCase):
    def test_no_post(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"No blog posts are available.")
        self.assertEqual(list(response.context['latest_post_list']), [])

    def test_post_blog(self):
        post = create_post(post_title="Hosanna")
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(
            list(response.context['latest_post_list']), 
            [post],
        )

    def test_two_post_blog(self):
        post1 = create_post(post_title="Alleluia")
        post2 = create_post(post_title="Hosanna")
        response = self.client.get(reverse('blog:index'))
        self.assertListEqual(
            list(response.context['latest_post_list']), 
            [post1, post2],
        )
class AuthorDetailViewTests(TestCase):
    def test_no_author(self):
        """
        confirm response for an author that does
        not exist
        """
        id = 20
        url = reverse('blog:author-detail', args=[id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_author(self):
        """
        check the response for an existing author

        """
        fname = "Mebi"
        author = Author.objects.create(author_firstname=fname, author_lastname=fname, author_avatar=fname)
        print("primary key = {}".format(author.author_id))
        url = reverse('blog:author-detail', args=[author.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.content)
class PostDetailViewTests(TestCase):
    def test_post_detail(self):
        post1 = create_post("Agidigba")
        post_part1 = Post_Section.objects.create(post=post1, body="This is perfecto my friend! I can't believe it's this cool. We gotta do this more often!")
        url = reverse('blog:post-detail', args=(post1.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.content)