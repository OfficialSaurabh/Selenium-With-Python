import pytest

# @pytest.fixture()
@pytest.mark.run(order=2)
def test_run_order_methodA(OneTimesetUp, setUp):
    print("Runnig confest Method A")
@pytest.mark.run(order=1)
def test_run_order_methodB(OneTimesetUp, setUp ):
    print("Runnig confest Method B")
@pytest.mark.run(order=3)
def test_run_order_methodc(OneTimesetUp, setUp ):
    print("Runnig confest Method c")


@pytest.mark.run(order=4)
def test_run_order_methodd(OneTimesetUp, setUp ):
    print("Runnig confest Method d")