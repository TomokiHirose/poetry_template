from template.sample import Foo, Hoge


def test_foo_say():
    """
    :Proceure:
    :Confirmation:
    :Tester:
    :Date:
    """
    assert Foo().say() == "foo"


def test_foo_say2():
    """
    :Proceure:
    :Confirmation:
    :Tester:
    :Date:
    """
    assert Foo().say2() == "foo"


def test_hoge_say():
    """
    :Proceure:
    :Confirmation:
    :Tester:
    :Date:
    """
    assert Hoge().say() == "hoge"


def test_hoge_say2():
    """
    :Proceure:
    :Confirmation:
    :Tester:
    :Date:
    """
    assert Hoge().say2() == "hoge2"
