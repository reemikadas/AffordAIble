import pytest

from affordaible.models import BuyerProfile, LoanScenario


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


def test_loan_scenario_calculates_loan_amount() -> None:
    scenario = LoanScenario(
        purchase_price=950000,
        down_payment=190000,
        annual_interest_rate=0.065,
        loan_term_years=30
    )

    assert scenario.loan_amount == 760000


def test_loan_scenario_rejects_nonpositive_purchase_price() -> None:
    with pytest.raises(ValueError, match="Purchase price"):
        LoanScenario(
            purchase_price=0,
            down_payment=0,
            annual_interest_rate=0.065,
            loan_term_years=30,
        )


def test_loan_scenario_rejects_negative_down_payment() -> None:
    with pytest.raises(ValueError, match="Down payment cannot be negative"):
        LoanScenario(
            purchase_price=950000,
            down_payment=-10000,
            annual_interest_rate=0.065,
            loan_term_years=30,
        )


def test_loan_scenario_rejects_down_payment_equal_to_price() -> None:
    with pytest.raises(ValueError, match="less than purchase price"):
        LoanScenario(
            purchase_price=950000,
            down_payment=950000,
            annual_interest_rate=0.065,
            loan_term_years=30,
        )


@pytest.mark.parametrize("invalid_rate", [-0.01, 6.5])
def test_loan_scenario_rejects_invalid_interest_rate(
    invalid_rate: float,
) -> None:
    with pytest.raises(ValueError, match="Annual interest rate"):
        LoanScenario(
            purchase_price=950000,
            down_payment=190000,
            annual_interest_rate=invalid_rate,
            loan_term_years=30,
        )


def test_loan_scenario_rejects_unsupported_loan_term() -> None:
    with pytest.raises(ValueError, match="Loan term"):
        LoanScenario(
            purchase_price=950000,
            down_payment=190000,
            annual_interest_rate=0.065,
            loan_term_years=20,
        )