import pytest

from affordaible.calculators.affordability import calculate_monthly_housing_budget
from affordaible.models import BuyerProfile, DtiLimits


def test_back_end_ratio_limits_monthly_housing_budget() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=850,
        available_savings=90000,
    )
    limits = DtiLimits(
        maximum_front_end_ratio=0.28,
        maximum_back_end_ratio=0.36,
    )

    result = calculate_monthly_housing_budget(profile, limits)

    assert result.front_end_limit == pytest.approx(2800)
    assert result.back_end_limit_after_debt == pytest.approx(2750)
    assert result.maximum_housing_cost == pytest.approx(2750)
    assert result.limiting_factor == "back_end"


def test_front_end_ratio_limits_monthly_housing_budget() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=0,
        available_savings=90000,
    )
    limits = DtiLimits(
        maximum_front_end_ratio=0.28,
        maximum_back_end_ratio=0.36,
    )

    result = calculate_monthly_housing_budget(profile, limits)

    assert result.front_end_limit == pytest.approx(2800)
    assert result.back_end_limit_after_debt == pytest.approx(3600)
    assert result.maximum_housing_cost == pytest.approx(2800)
    assert result.limiting_factor == "front_end"


def test_housing_budget_is_zero_when_debt_exceeds_allowance() -> None:
    profile = BuyerProfile(
        annual_gross_income=120000,
        monthly_debt_payments=4000,
        available_savings=90000,
    )
    limits = DtiLimits(
        maximum_front_end_ratio=0.28,
        maximum_back_end_ratio=0.36,
    )

    result = calculate_monthly_housing_budget(profile, limits)

    assert result.front_end_limit == pytest.approx(2800)
    assert result.back_end_limit_after_debt == pytest.approx(-400)
    assert result.maximum_housing_cost == 0
    assert result.limiting_factor == "back_end"