from affordaible.calculators.mortgage import calculate_monthly_principal_and_interest
from affordaible.models import HousingCostAssumptions, LoanScenario, MonthlyHousingCostBreakdown


def calculate_monthly_housing_costs(
        scenario: LoanScenario,
        assumptions: HousingCostAssumptions,
) -> MonthlyHousingCostBreakdown:
    principal_and_interest = calculate_monthly_principal_and_interest(scenario)

    monthly_property_tax = (
        scenario.purchase_price
        * assumptions.annual_property_tax_rate
        / 12
    )

    monthly_homeowners_insurance = (
        assumptions.annual_homeowners_insurance / 12
    )

    monthly_mortgage_insurance = (
        scenario.loan_amount
        * assumptions.annual_mortgage_insurance_rate
        / 12
    )

    return MonthlyHousingCostBreakdown(
        principal_and_interest=principal_and_interest,
        property_tax=monthly_property_tax,
        homeowners_insurance=monthly_homeowners_insurance,
        mortgage_insurance=monthly_mortgage_insurance,
        hoa_dues=assumptions.monthly_hoa_dues,
    )