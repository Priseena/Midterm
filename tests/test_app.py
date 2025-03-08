import pytest
from app import App

def test_app_get_environment_variable():
    """Test retrieval of environment variables."""
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test handling of an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit):
        app.start()
    
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
