import cmd
from calculator import Calculator
from history import HistoryManager

class CalculatorREPL(cmd.Cmd):
    intro = 'Welcome to the calculator REPL. Type help or ? to list commands.\n'
    prompt = '(calc) '
    
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
    
    def do_add(self, args):
        x, y = map(int, args.split())
        result = self.calculator.add(x, y)
        self.history_manager.add_record('add', x, y, result)
        print(f'Result: {result}')
    
    def do_subtract(self, args):
        x, y = map(int, args.split())
        result = self.calculator.subtract(x, y)
        self.history_manager.add_record('subtract', x, y, result)
        print(f'Result: {result}')

    def do_multiply(self, args):
        x, y = map(int, args.split())
        result = self.calculator.multiply(x, y)
        self.history_manager.add_record('multiply', x, y, result)
        print(f'Result: {result}')
    
    def do_divide(self, args):
        x, y = map(int, args.split())
        try:
            result = self.calculator.divide(x, y)
            self.history_manager.add_record('divide', x, y, result)
            print(f'Result: {result}')
        except ValueError as e:
            print(e)
    
    def do_history(self, args):
        if self.history_manager.history.empty:
            print("No history available.")
        else:
            print(self.history_manager.history)
    
    def do_save_history(self, args):
        self.history_manager.save_history()
        print("History saved")
    
    def do_load_history(self, args):
        self.history_manager.load_history()
        print("History loaded")
    
    def do_clear_history(self, args):
        self.history_manager.clear_history()
        print("History cleared")
    
    def do_delete_history(self, args):
        self.history_manager.delete_history()
        print("History deleted")
    
    def do_exit(self, args):
        print('Goodbye!')
        return True

if __name__ == '__main__':
    CalculatorREPL().cmdloop()
