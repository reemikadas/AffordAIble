import pytest

from affordaible.models import BuyerProfile


def test_buyer_profile_accepts_valid_values() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=850,
        available_savings=90000,
    )

    assert profile.annual_gross_income == 120000
    assert profile.monthly_debt_payments == 850
    assert profile.available_savings == 90000


def test_buyer_profile_rejects_nonpositive_income() -> None:
    with pytest.raises(ValueError, match="Annual gross income"):
        BuyerProfile(
            annual_gross_income=-120000,
            monthly_debt_payments=850,
            available_savings=90000,
        )


def test_buyer_profile_rejects_negative_debt() -> None:
    with pytest.raises(ValueError, match="Monthly debt payments"):
        BuyerProfile(
            annual_gross_income=120000,
            monthly_debt_payments=-850,
            available_savings=90000,
        )


def test_buyer_profile_rejects_negative_savings() -> None:
    with pytest.raises(ValueError, match="Available savings"):
        BuyerProfile(
            annual_gross_income=120000,
            monthly_debt_payments=850,
            available_savings=-90000,
        )