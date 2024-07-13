from django.test import TestCase
from ..models import Project

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='This is a test project.',
            technology='Django',
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.description, 'This is a test project.')
        self.assertEqual(self.project.technology, 'Django')

    def test_project_str(self):
        self.assertEqual(str(self.project), self.project.title)
