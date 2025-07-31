import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize("input_string, expected_result", [("skypro", "Skypro"),
                                                           ("Skypro", "Skypro"),
                                                           ("hello world", "Hello world"),
                                                           ("123abc", "123abc"),
                                                           ("",""),
                                                           ("йцукен", "Йцукен"),
                                                           (" door", "door"),
                                                           ("&hello world", "&hello world")])
def test_capitilize(input_string, expected_result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == expected_result

@pytest.mark.parametrize("input_string, expected_result", [(" Skypro", "Skypro"),
                                                           ("   Skypro","Skypro"),
                                                           ("Skypro","Skypro"),
                                                           (" hello world","hello world")])
def test_trim(input_string, expected_result):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == expected_result

@pytest.mark.parametrize("input_string, delimeter, expected_result", [("book,door,phone", ",", ["book", "door", "phone"]), 
                                                                      ("book:door:phone", ":", ["book", "door", "phone"]), 
                                                                      ("book/door/phone", "/", ["book", "door", "phone"]),
                                                                      ("book|door|phone", "|", ["book", "door", "phone"]),
                                                                      ("", ",", []),
                                                                      ("single", ",", ["single"])])
def test_to_list(input_string, delimeter, expected_result):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string, delimeter)
    assert res == expected_result

@pytest.mark.parametrize("input_string, symbol, expected_result", [("SkyPro", "S", True),
                                                                   ("SkyPro", "s", False ),
                                                                   ("", "s", False),
                                                                   ("12345", "4", True)])
def test_contains(input_string, symbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, symbol)
    assert res == expected_result

@pytest.mark.parametrize("input_string, simbol, expected_result", [("SkyPro", "Sky", "Pro"),
                                                                   ("SkyPro", "pro", "SkyPro"),
                                                                   (" ", "pro", " "),
                                                                   ("Hello//", "//", "Hello"),
                                                                   ("Hello", "Hello", ""),
                                                                   ("1234", "12", "34")])
def test_delete_symbol(input_string, simbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, simbol)
    assert res == expected_result

@pytest.mark.parametrize("input_string, simbol, expected_result", [("SkyPro", "S", True),
                                                                   ("skyPro", "s", True),
                                                                   (" SkyPro", "S", False),
                                                                   ("SkyPro", "Sky", True),
                                                                   (" ", "S", False),
                                                                   ("1234", "1", True)])
def test_starts_with(input_string, simbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, simbol)
    assert res == expected_result

@pytest.mark.parametrize("input_string, simbol, expected_result", [("SkyPro", "o", True),
                                                                   ("SkyPrO", "O", True),
                                                                   ("SkyPro ", "o", False),
                                                                   (" ", "o", False),
                                                                   ("1234", "34", True),])
def test_end_with(input_string, simbol, expected_result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, simbol)
    assert res == expected_result

@pytest.mark.parametrize("input_string, expected_result", [(" ", True),
                                                           ("Sky", False),
                                                           ("123", False),
                                                           (".;/;", False),
                                                           ("", True)])
def test_is_empty(input_string, expected_result):
    string_utils = StringUtils()
    res = string_utils.is_empty(input_string)
    assert res == expected_result


@pytest.mark.parametrize("input_list, joiner, expected_result", [(["book", "door", "table"], ", ", "book, door, table"),
                                                                   (["book", "door", "table"], "/", "book/door/table"),
                                                                   (["book", "door", "table"], "-", "book-door-table")])
def test_list_to_string(input_list, joiner, expected_result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_list, joiner)
    assert res == expected_result


