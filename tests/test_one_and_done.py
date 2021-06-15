from tests.flow.flo import Flo
import pytest
# @pytest.mark.skip("todo")
def test_one_and_done():
    Flo.test("tests/flow/one_and_done.sim.txt")