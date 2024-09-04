import unittest
from unittest.mock import patch
from task_manager import add_task, delete_task

@patch('task_manager.TASKS_FILE', 'test_tasks.txt')
class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Fixtures      
        self.tasks = ["Task 1", "Task 2", "Task 3"]
        
    def test_add_task(self):
        # Test adding a new task
        new_task = "Task 4"
        add_task(self.tasks, new_task)
        self.assertIn(new_task, self.tasks)
        self.assertEqual(len(self.tasks), 4)  # Ensure the task was added

    def test_delete_task_valid(self):
        # Test deleting a valid task
        task_num = 2
        result = delete_task(self.tasks, task_num)
        self.assertTrue(result)
        self.assertNotIn("Task 2", self.tasks)
        self.assertEqual(len(self.tasks), 2)        

    def test_delete_task_invalid(self):
        # Test deleting a task with an invalid index
        task_num = 10
        result = delete_task(self.tasks, task_num)
        self.assertFalse(result)
        self.assertEqual(len(self.tasks), 3)  # No task should be removed

    def test_delete_task_value_error(self):
        # Test deleting a task with a non-integer input
        result = delete_task(self.tasks, "invalid")
        self.assertFalse(result) 

if __name__ == '__main__':
    unittest.main()
