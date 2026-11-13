from app.fuel_converter import gallons_to_liters

def test_gallons_to_liters_whole():
    assert gallons_to_liters(10) == 37.85

def test_gallons_to_liters_decimal():
    assert gallons_to_liters(5.5) == 20.82
