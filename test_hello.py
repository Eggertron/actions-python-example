import pytest
from hello import Hello

def test_hello():
  a = Hello()
  assert a.say_hello() == "hello world."
