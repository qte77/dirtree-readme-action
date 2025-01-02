import pytest
import src.app

@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv('CMD_HIGHLIGHT', 'sh')
    monkeypatch.setenv('EXCLUDE', '.git|__pycache__')
    monkeypatch.setenv(
        'INSERT_HERE_START_STRING',
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->'
    )
    monkeypatch.setenv(
        'INSERT_HERE_END_STRING',
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
    )
    monkeypatch.setenv('OUT_FILE', 'README.md')
    monkeypatch.setenv('TREE_THEME', 'sh')

def test_main_execution(mock_env, tmp_path):
    # Setup by writing a dummy file
    (tmp_path / 'README.md').write_text('''
        # README
        <!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
        <!-- DIRTREE-README-ACTION-INSERT-HERE-END -->
    ''')
    (tmp_path / 'src').mkdir()
    (tmp_path / 'src' / 'utils.py').touch()
    (tmp_path / 'src' / 'app.py').touch()
    
    # Run the main function
    try:
        main()
    except SystemExit as e:
        pytest.fail(f"SystemExit was raised with code {e.code}")

    # Check if the README was updated with some code block
    with open(tmp_path / 'README.md', 'r') as f:
        content = f.read()

    assert '```sh' in content
    assert '├── src' in content
    assert '│ ├── utils.py' in content
    assert '│ └── app.py' in content
    assert '```' in content
