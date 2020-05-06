import unittest
from app.models import Pitch,User
class PostModelTest(unittest.TestCase):
    def setUp(self):
        self.user_john = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.pitch = Pitch(id=1,content='test pitch')
    def tearDown(self):
        Pitch.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.pitch, Pitch))
    def test_check_instance_variables(self):
        self.assertEquals(self.pitch.id,1)
        self.assertEquals(self.pitch.content,'test pitch')
        
