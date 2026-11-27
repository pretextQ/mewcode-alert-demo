from app import configured_timeout


def test_timeout_is_five_seconds():
    assert configured_timeout() == 5


def test_return_type():
    assert isinstance(configured_timeout(), int)


if __name__ == "__main__":
    test_timeout_is_five_seconds()
    test_return_type()
