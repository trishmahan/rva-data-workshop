def hello_world():
    return "Hi!"


def test_hello_world():
    greeting = hello_world()
    assert greeting == 'Hi!'