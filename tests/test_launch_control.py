from app.launch_control import authorize_launch

def test_authorize_launch_success():
    assert authorize_launch(True, True) == "Launch Authorised"

def test_authorize_launch_engines_fail():
    assert authorize_launch(False, True) == "Launch Aborted"

def test_authorize_launch_doors_fail():
    assert authorize_launch(True, False) == "Launch Aborted"

def test_authorize_launch_both_fail():
    assert authorize_launch(False, False) == "Launch Aborted"
