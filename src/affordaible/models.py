from dataclasses import dataclass


@dataclass(frozen=True)
class BuyerProfile:
    annual_gross_income: float
    monthly_debt_payments: float
    available_savings: float

    def __post_init__(self) -> None:
        if self.annual_gross_income <= 0:
            raise ValueError("Annual gross income must be greater than zero.")
        
        if self.monthly_debt_payments < 0:
            raise ValueError("Monthly debt payments cannot be negative.")
        
        if self.available_savings < 0:
            raise ValueError("Available savings cannot be negative.")