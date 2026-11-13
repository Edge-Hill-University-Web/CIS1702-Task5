from app.warp_calculator import calculate_travel_time

def test_calculate_travel_time_standard():
    assert calculate_travel_time(100, 10) == 10.0

def test_calculate_travel_time_decimal():
    assert calculate_travel_time(50.5, 2) == 25.25
