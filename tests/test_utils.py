import pytest
from pathlib import Path
from utils import (
    _get_tree_theme,
    _is_path_in_exclude,
    _generate_tree,
    get_formatted_tree_output,
    get_write_positions_in_file,
    write_to_file
)

def test_get_tree_theme():
    assert _get_tree_theme('cmd') == (' ', '│ ', '├──', '└──')
    assert _get_tree_theme('slash') == (' ', '│ ', '│── ', '\── ')
    assert _get_tree_theme('elli') == (' ', '︙ ', '︙··· ', ' ···· ')
    assert _get_tree_theme('null') == (' ', ' ', ' ', ' ')
    assert _get_tree_theme('sh') == (' ', '│ ', '├── ', '└──')
    with pytest.raises(NotImplementedError):
        _get_tree_theme('invalid_theme')

@pytest.mark.parametrize(
    "path, expected",
    [
        (Path('.git'), True),
        (Path('__pycache__'), True),
        (Path('src/utils.py'), False),
        (Path('src/__pycache__/utils.cpython-312.pyc'), True),
    ]
)
def test_is_path_in_exclude(path, expected):
    exclude_list = ['.git', '__pycache__']
    if expected:
        assert _is_path_in_exclude(path, exclude_list)
    else:
        assert not _is_path_in_exclude(path, exclude_list)

def test_generate_tree(tmp_path):
    # Create a temporary directory structure
    (tmp_path / 'dir1').mkdir()
    (tmp_path / 'dir1' / 'file1.txt').touch()
    (tmp_path / 'dir1' / 'dir2').mkdir()
    (tmp_path / 'dir1' / 'dir2' / 'file2.txt').touch()
    (tmp_path / 'file3.txt').touch()
    
    exclude_list = ['.git', '__pycache__']
    tree = list(_generate_tree(tmp_path, exclude_list, ' ', '│ ', '├── ', '└── '))
    expected = [
        '├── dir1',
        '│ ├── dir2',
        '│ │ └── file2.txt',
        '│ └── file1.txt',
        '└── file3.txt'
    ]
    assert tree == expected

def test_get_formatted_tree_output(tmp_path):
    # Similar setup as above
    (tmp_path / 'dir1').mkdir()
    (tmp_path / 'dir1' / 'file1.txt').touch()
    (tmp_path / 'file3.txt').touch()
    
    exclude_list = ['.git', '__pycache__']
    tree_output = get_formatted_tree_output(tmp_path, exclude_list, 'sh', 'sh')
    assert isinstance(tree_output, list)
    assert len(tree_output) > 0
    assert tree_output[0].startswith('```')
    assert tree_output[-1].startswith('```')

def test_get_write_positions_in_file(tmp_path):
    test_file = tmp_path / 'test.md'
    test_file.write_text('''
    Some content
    <!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
    <!-- DIRTREE-README-ACTION-INSERT-HERE-END -->
    More content
    ''')
    start, end = get_write_positions_in_file(
        test_file,
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->',
        '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
    )
    assert start == 2
    assert end == 3

def test_write_to_file(tmp_path):
    test_file = tmp_path / 'test.md'
    test_file.write_text('''
    Some content
    <!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
    <!-- DIRTREE-README-ACTION-INSERT-HERE-END -->
    More content
    ''')
    dirtree = ['``````']
    write_to_file(test_file, dirtree, 2, 3)
    with open(test_file, 'r') as f:
        content = f.read()
    assert '```'
    assert '├── dir1' in content
    assert '│ └── file1.txt' in content
    assert '└── file3.txt' in content
    assert '```' in content
