from tests.flow.flo import Flo
import pytest
# @pytest.mark.skip("todo")
def test_bank_one_and_done():
    Flo.test("tests/flow/bank_one_roll_then_quit.sim.txt")