import pytest
import steam_id


def test_check_converted_id():
    converted_user_id = steam_id.convert_id("STEAM_0:1:35807358")
    assert converted_user_id == '71614717'
