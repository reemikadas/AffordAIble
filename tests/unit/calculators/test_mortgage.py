import pytest

from affordaible.calculators.mortgage import calculate_monthly_principal_and_interest
from affordaible.models import LoanScenario


def test_calculates_30_year_mortgage_payment() -> None:
    scenario = LoanScenario(
        purchase_price=950000,
        down_payment=190000,
        annual_interest_rate=0.065,
        loan_term_years=30,
    )

    result = calculate_monthly_principal_and_interest(scenario)

    assert result == pytest.approx(4803.72, abs=0.01)


def test_calculates_15_year_mortgage_payment() -> None:
    scenario = LoanScenario(
        purchase_price=950000,
        down_payment=190000,
        annual_interest_rate=0.065,
        loan_term_years=15,
    )

    result = calculate_monthly_principal_and_interest(scenario)

    assert result == pytest.approx(6620.42, abs=0.01)


def test_calculates_zero_interest_mortgage_payment() -> None:
    scenario = LoanScenario(
        purchase_price=950000,
        down_payment=190000,
        annual_interest_rate=0,
        loan_term_years=30,
    )

    result = calculate_monthly_principal_and_interest(scenario)

    assert result == pytest.approx(2111.11, abs=0.01)