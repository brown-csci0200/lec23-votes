import pytest

import hello_world as hw # pull in the things from hello_world.py

# all testing functions should start with test_
def test_max_val():
    assert hw.max_val([3, 4, 5]) == 5
    assert hw.max_val([-4, -1, -2, -5]) == -1
    # hw.max_val means call the max_val function in hello_world.py