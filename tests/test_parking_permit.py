import pytest
from src.parking_permit import is_permit_valid

@pytest.mark.parametrize(
    ("permit_active", "parked_minutes", "expected_output"),
    [
        (True, 60, True), # Within range of parked minutes
        (True, 0, True), # Minimum limit of parked minutes
        (True, 120, True), # Maximum limit of parked minutes
        (False, 30, False), # Permit expired
        (True, 150, False), # Exceeded limit of parked minutes
    ],
)

def test_validate_parking_permit__valid_assert(permit_active, parked_minutes, expected_output):
    output_result = is_permit_valid(permit_active, parked_minutes)
    assert output_result is expected_output

@pytest.mark.parametrize(
    ("permit_active", "parked_minutes", "expected_error"),
    [
        ("True", 60, TypeError), # Text error of permit active
        (True, 7.5, TypeError), # Decimal error of parked minutes
        (True, "60", TypeError), # Text error of parked minutes
        (True, -60, ValueError), # Negative error of parked minutes
    ],
)

def test_validate_parking_permit__error_assert(permit_active, parked_minutes, expected_error):
    with pytest.raises(expected_error):
        is_permit_valid(permit_active, parked_minutes)