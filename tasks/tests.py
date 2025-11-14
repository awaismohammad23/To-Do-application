from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskModelTest(TestCase):
    """Test cases for Task model"""
    
    def test_task_creation(self):
        """Test that a task can be created with all fields"""
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task description',
            is_completed=False
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task description')
        self.assertFalse(task.is_completed)
        self.assertIsNotNone(task.created_at)
    
    def test_task_creation_minimal(self):
        """Test that a task can be created with only required fields"""
        task = Task.objects.create(title='Minimal Task')
        self.assertEqual(task.title, 'Minimal Task')
        self.assertEqual(task.description, None)
        self.assertFalse(task.is_completed)
    
    def test_task_string_representation(self):
        """Test the string representation of Task model"""
        task = Task.objects.create(title='String Test Task')
        self.assertEqual(str(task), 'String Test Task')
    
    def test_task_completion_toggle(self):
        """Test that task completion status can be toggled"""
        task = Task.objects.create(title='Toggle Test', is_completed=False)
        self.assertFalse(task.is_completed)
        
        task.is_completed = True
        task.save()
        self.assertTrue(task.is_completed)


class TaskViewTest(TestCase):
    """Test cases for Task views"""
    
    def setUp(self):
        """Set up test client and sample data"""
        self.client = Client()
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            is_completed=False
        )
    
    def test_task_list_view(self):
        """Test that task list view returns 200 and displays tasks"""
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'tasks/task_list.html')
    
    def test_task_detail_view(self):
        """Test that task detail view returns 200 and displays task details"""
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertContains(response, 'Test Description')
        self.assertTemplateUsed(response, 'tasks/task_detail.html')
    
    def test_task_create_view_get(self):
        """Test that task create view returns form on GET request"""
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')
    
    def test_task_create_view_post(self):
        """Test that task can be created via POST request"""
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'is_completed': False
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())
    
    def test_task_update_view_get(self):
        """Test that task update view returns form with existing data"""
        response = self.client.get(reverse('task_update', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'tasks/task_form.html')
    
    def test_task_update_view_post(self):
        """Test that task can be updated via POST request"""
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'is_completed': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertTrue(self.task.is_completed)
    
    def test_task_delete_view_get(self):
        """Test that task delete view returns confirmation page"""
        response = self.client.get(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'tasks/task_confirm_delete.html')
    
    def test_task_delete_view_post(self):
        """Test that task can be deleted via POST request"""
        task_id = self.task.pk
        response = self.client.post(reverse('task_delete', args=[task_id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertFalse(Task.objects.filter(pk=task_id).exists())
    
    def test_task_toggle_view(self):
        """Test that task completion status can be toggled"""
        initial_status = self.task.is_completed
        response = self.client.get(reverse('task_toggle', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after toggle
        self.task.refresh_from_db()
        self.assertNotEqual(self.task.is_completed, initial_status)

