from bot import get_user_first_name

class MockUser:
    def __init__(self, first_name=None):
        self.first_name = first_name

class MockMessage:
    def __init__(self, first_name=None):
        self.from_user = MockUser(first_name=first_name)

def test_get_user_first_name_with_name():
    message = MockMessage(first_name="Liza")
    assert get_user_first_name(message) == "Liza"

def test_get_user_first_name_without_name():
    message = MockMessage(first_name=None)
    assert get_user_first_name(message) == "друг"

if __name__ == "__main__":
    test_get_user_first_name_with_name()
    test_get_user_first_name_without_name()
    print("All tests passed.")
