# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from .models import Profile
#
# class ProfileViewsTest(TestCase):
#     def setUp(self):
#         # Create test users and profiles
#         self.user1 = User.objects.create_user(username='user1', password='pass1')
#         self.user2 = User.objects.create_user(username='user2', password='pass2')
#         self.profile1 = Profile.objects.create(user=self.user1, bio='Bio of user1')
#         self.profile2 = Profile.objects.create(user=self.user2, bio='Bio of user2')
#
#     def test_index_view(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profiles/index.html')
#         self.assertContains(response, 'Bio of user1')
#         self.assertContains(response, 'Bio of user2')
#
#     def test_profile_view(self):
#         response = self.client.get(reverse('profile', args=['user1']))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profiles/profile.html')
#         self.assertContains(response, 'Bio of user1')
#
#         response = self.client.get(reverse('profile', args=['user2']))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profiles/profile.html')
#         self.assertContains(response, 'Bio of user2')
#
#     def test_profile_view_non_existent_user(self):
#         response = self.client.get(reverse('profile', args=['nonexistent']))
#         self.assertEqual(response.status_code, 404)
#
# if __name__ == "__main__":
#     TestCase.main()
