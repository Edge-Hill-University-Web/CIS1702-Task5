from app.oxygen_monitor import check_oxygen

def test_check_oxygen_low():
    assert check_oxygen(15) == "Warning: Low Oxygen"
    assert check_oxygen(19.9) == "Warning: Low Oxygen"

def test_check_oxygen_optimal():
    assert check_oxygen(21) == "Oxygen Levels Optimal"
    assert check_oxygen(100) == "Oxygen Levels Optimal"
