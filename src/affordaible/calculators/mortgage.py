from affordaible.models import LoanScenario


def calculate_monthly_principal_and_interest(
        scenario: LoanScenario,
) -> float:
    monthly_interest_rate = scenario.annual_interest_rate / 12
    number_of_payments = scenario.loan_term_years * 12

    if monthly_interest_rate == 0:
        return scenario.loan_amount / number_of_payments
    
    growth_factor = (1 + monthly_interest_rate) ** number_of_payments

    return (
        scenario.loan_amount
        * monthly_interest_rate
        * growth_factor
        / (growth_factor - 1)
    )