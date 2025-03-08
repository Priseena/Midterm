import unittest
import os
from history import HistoryManager

class TestHistoryManager(unittest.TestCase):
    
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_add_record(self):
        self.history_manager.add_record('add', 2, 2, 4)
        self.assertEqual(len(self.history_manager.history), 1)
        self.assertEqual(self.history_manager.history.iloc[0]['operation'], 'add')
        self.assertEqual(self.history_manager.history.iloc[0]['operand1'], 2)
        self.assertEqual(self.history_manager.history.iloc[0]['operand2'], 2)
        self.assertEqual(self.history_manager.history.iloc[0]['result'], 4)

    def test_save_load_history(self):
        self.history_manager.add_record('add', 2, 2, 4)
        self.history_manager.save_history('test_history.csv')

        new_history_manager = HistoryManager()
        new_history_manager.load_history('test_history.csv')
        self.assertEqual(len(new_history_manager.history), 1)
        self.assertEqual(new_history_manager.history.iloc[0]['operation'], 'add')
        self.assertEqual(new_history_manager.history.iloc[0]['operand1'], 2)
        self.assertEqual(new_history_manager.history.iloc[0]['operand2'], 2)
        self.assertEqual(new_history_manager.history.iloc[0]['result'], 4)

        # Clean up test file
        os.remove('test_history.csv')

    def test_clear_history(self):
        self.history_manager.add_record('add', 2, 2, 4)
        self.history_manager.clear_history()
        self.assertEqual(len(self.history_manager.history), 0)

    def test_delete_history(self):
        self.history_manager.save_history('test_history.csv')
        self.history_manager.delete_history('test_history.csv')
        self.assertFalse(os.path.exists('test_history.csv'))

if __name__ == '__main__':
    unittest.main()
