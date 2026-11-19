import pytest
from src.parking_fee import calculate_parking_fee

@pytest.mark.parametrize(
    ("minutes", "expected_output"),
    [
        (0, 0), # 0.0 hour
        (30, 200), # 0.5 hours
        (60, 200), # 1.0 hour
        (90, 400), # 1.5 hours
    ],
)

def test_calculate_parking_fee__valid_assert(minutes, expected_output):
    output_result = calculate_parking_fee(minutes)
    assert output_result is expected_output

@pytest.mark.parametrize(
    ("minutes", "expected_error"),
    [
        (0.5, TypeError), # Decimal error
        ("30", TypeError), # Text error
        (-30, ValueError), # Negative error
    ],
)

def test_calculate_parking_fee__error_assert(minutes, expected_error):
    with pytest.raises(expected_error):
        calculate_parking_fee(minutes)