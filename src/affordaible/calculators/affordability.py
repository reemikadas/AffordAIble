from affordaible.models import BuyerProfile, DtiLimits, MonthlyHousingBudget


def calculate_monthly_housing_budget(
        profile: BuyerProfile,
        limits: DtiLimits,
) -> MonthlyHousingBudget:
    gross_monthly_income = profile.annual_gross_income / 12

    front_end_limit = (
        gross_monthly_income * limits.maximum_front_end_ratio
    )

    back_end_limit_after_debt = (
        gross_monthly_income * limits.maximum_back_end_ratio
        - profile.monthly_debt_payments
    )

    return MonthlyHousingBudget(
        front_end_limit=front_end_limit,
        back_end_limit_after_debt=back_end_limit_after_debt,
    )