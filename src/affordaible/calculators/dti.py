from affordaible.models import BuyerProfile


def calculate_front_end_dti(
        profile: BuyerProfile,
        *,
        monthly_housing_cost: float,
) -> float:
    _validate_monthly_housing_cost(monthly_housing_cost)
    
    gross_monthly_income = profile.annual_gross_income / 12

    return monthly_housing_cost / gross_monthly_income


def calculate_back_end_dti(
        profile: BuyerProfile,
        *,
        monthly_housing_cost: float,
) -> float:
    _validate_monthly_housing_cost(monthly_housing_cost)
    
    gross_monthly_income = profile.annual_gross_income / 12
    total_monthly_debt = (
        monthly_housing_cost + profile.monthly_debt_payments
    )

    return total_monthly_debt / gross_monthly_income


def _validate_monthly_housing_cost(monthly_housing_cost: float) -> None:
    if monthly_housing_cost < 0:
        raise ValueError("Monthly housing cost cannot be negative.")