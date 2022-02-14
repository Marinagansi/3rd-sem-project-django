from django.test import SimpleTestCase, TestCase,Client
from django.urls import resolve, reverse
from registration.views import firstpage,home,explore,about_us,admin_page,hotel,faq,find_guide,hotelreview
from django.contrib.auth.models import User

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_firstpage(self):
        url=reverse('firstpage')
        self.assertEquals(resolve(url).func,firstpage)

    def test_case_home(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_case_admin_page(self):
        url=reverse('admin_page')
        self.assertEquals(resolve(url).func,admin_page)

    def test_case_hotel(self):
        url=reverse('hotel')
        self.assertEquals(resolve(url).func,hotel)


    def test_case_faq(self):
        url=reverse('faq')
        self.assertEquals(resolve(url).func,faq)


    def test_case_find_guide(self):
        url=reverse('find_guide')
        self.assertEquals(resolve(url).func,find_guide)

    def test_case_hotelreview(self):
        url=reverse('hotelreview')
        self.assertEquals(resolve(url).func,hotelreview)

    def test_case_explore(self):
        url=reverse('explore')
        self.assertEquals(resolve(url).func,explore)

    def test_case_about_us(self):
        url=reverse('about_us')
        self.assertEquals(resolve(url).func,about_us)

class TestViews(TestCase):
    def test_case_homepage_views(self):
        user=User.objects.create(username="testcase")
        user.set_password('123456')
        user.save()
 
        client=Client()
 
        logged_in=client.login(username='testcase',password="123456")
 
        url=reverse('home')
 
        response=client.get(url)
     
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"home.html")
