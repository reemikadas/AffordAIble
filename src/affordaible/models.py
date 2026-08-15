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


@dataclass(frozen=True)
class LoanScenario:
    purchase_price: float
    down_payment: float
    annual_interest_rate: float
    loan_term_years: int

    def __post_init__(self) -> None:
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be greater than zero.")
        
        if self.down_payment < 0:
            raise ValueError("Down payment cannot be negative.")
        
        if self.down_payment >= self.purchase_price:
            raise ValueError("Down payment must be less than purchase price.")
        
        if not 0 <= self.annual_interest_rate <= 1:
            raise ValueError("Annual interest rate must be a decimal between zero and one.")
        
        if self.loan_term_years not in {15, 30}:
            raise ValueError("Loan term must be either 15 or 30 years.")
    
    @property
    def loan_amount(self) -> float:
        return self.purchase_price - self.down_payment