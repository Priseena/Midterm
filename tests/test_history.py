import unittest
import os
from calculator.history_manager import HistoryManager

class TestHistoryManager(unittest.TestCase):
    
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_add_record(self):
        """Test adding a record to history"""
        self.history_manager.add_record('add', 2, 2, 4)
        self.assertEqual(len(self.history_manager.history), 1)

    def test_save_load_history(self):
        """Test saving and loading history from a file"""
        self.history_manager.add_record('add', 2, 2, 4)
        self.history_manager.save_history('test_history.csv')

        new_history_manager = HistoryManager()
        new_history_manager.load_history('test_history.csv')
        self.assertEqual(len(new_history_manager.history), 1)

        os.remove('test_history.csv')  # Cleanup

    def test_clear_history(self):
        """Test clearing history"""
        self.history_manager.add_record('add', 2, 2, 4)
        self.history_manager.clear_history()
        self.assertEqual(len(self.history_manager.history), 0)

    def test_delete_history(self):
        """Test deleting history file"""
        self.history_manager.save_history('test_history.csv')
        self.history_manager.delete_history('test_history.csv')
        self.assertFalse(os.path.exists('test_history.csv'))

if __name__ == '__main__':
    unittest.main()
