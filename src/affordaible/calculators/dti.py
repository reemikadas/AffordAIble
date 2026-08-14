from affordaible.models import BuyerProfile


def calculate_front_end_dti(
        profile: BuyerProfile,
        *,
        monthly_housing_cost: float,
) -> float:
    if monthly_housing_cost < 0:
        raise ValueError("Monthly housing cost cannot be negative.")
    
    gross_monthly_income = profile.annual_gross_income / 12

    return monthly_housing_cost / gross_monthly_income