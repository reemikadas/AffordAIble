import pytest

from affordaible.calculators.dti import calculate_back_end_dti, calculate_front_end_dti
from affordaible.models import BuyerProfile


def test_calculate_front_end_dti() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=850,
        available_savings=90000,
    )

    result = calculate_front_end_dti(
        profile,
        monthly_housing_cost=2800,
    )

    assert result == pytest.approx(0.28)


def test_front_end_dti_allows_zero_housing_cost() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=850,
        available_savings=90000,
    )

    result = calculate_front_end_dti(
        profile,
        monthly_housing_cost=0,
    )

    assert result == 0

def test_front_end_dti_rejects_negative_housing_cost() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=850,
        available_savings=90000,
    )

    with pytest.raises(ValueError, match="Monthly housing cost"):
        calculate_front_end_dti(
            profile,
            monthly_housing_cost=-2800
        )


def test_calculate_back_end_dti() -> None:
    profile = BuyerProfile(
        annual_gross_income = 120000,
        monthly_debt_payments = 850,
        available_savings = 90000,
    )

    result = calculate_back_end_dti(
        profile,
        monthly_housing_cost=2800,
    )

    assert result == pytest.approx(0.365)


def test_back_end_dti_includes_debt_with_zero_housing_cost() -> None:
    profile = BuyerProfile(
        annual_gross_income = 120000,
        monthly_debt_payments = 850,
        available_savings = 90000,
    )

    result = calculate_back_end_dti(
        profile,
        monthly_housing_cost=0,
    )

    assert result == pytest.approx(0.085)


def test_back_end_dti_rejects_negative_housing_cost() -> None:
    profile = BuyerProfile(
        annual_gross_income = 120000,
        monthly_debt_payments = 850,
        available_savings = 90000,
    )

    with pytest.raises(ValueError, match="Monthly housing cost"):
        calculate_back_end_dti(
            profile,
            monthly_housing_cost=-2800
        )