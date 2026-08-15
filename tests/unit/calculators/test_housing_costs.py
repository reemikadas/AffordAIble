import pytest

from affordaible.calculators.housing_costs import calculate_monthly_housing_costs
from affordaible.models import HousingCostAssumptions, LoanScenario


def test_calculates_complete_monthly_housing_cost() -> None:
    scenario = LoanScenario(
        purchase_price=950000,
        down_payment=190000,
        annual_interest_rate=0.065,
        loan_term_years=30,
    )

    assumptions = HousingCostAssumptions(
        annual_property_tax_rate=0.012,
        annual_homeowners_insurance=1800,
        annual_mortgage_insurance_rate=0.005,
        monthly_hoa_dues=350,
    )

    result = calculate_monthly_housing_costs(
        scenario,
        assumptions,
    )

    assert result.principal_and_interest == pytest.approx(4803.72, abs=0.01,)
    assert result.property_tax == pytest.approx(950, abs=0.01)
    assert result.homeowners_insurance == pytest.approx(150, abs=0.01)
    assert result.mortgage_insurance == pytest.approx(316.67, abs=0.01)
    assert result.hoa_dues == 350
    assert result.total == pytest.approx(6570.38, abs=0.01)


def test_calculates_housing_cost_without_additional_expenses() -> None:
    scenario = LoanScenario(
        purchase_price=950000,
        down_payment=190000,
        annual_interest_rate=0.065,
        loan_term_years=30,
    )
    assumptions = HousingCostAssumptions(
        annual_property_tax_rate=0,
        annual_homeowners_insurance=0,
        annual_mortgage_insurance_rate=0,
        monthly_hoa_dues=0,
    )

    result = calculate_monthly_housing_costs(
        scenario,
        assumptions,
    )

    assert result.property_tax == 0
    assert result.homeowners_insurance == 0
    assert result.mortgage_insurance == 0
    assert result.hoa_dues == 0
    assert result.total == pytest.approx(result.principal_and_interest, abs=0.01,)