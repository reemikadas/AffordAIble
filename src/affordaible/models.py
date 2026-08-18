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


@dataclass(frozen=True)
class HousingCostAssumptions:
    annual_property_tax_rate: float
    annual_homeowners_insurance: float
    annual_mortgage_insurance_rate: float
    monthly_hoa_dues: float

    def __post_init__(self) -> None:
        if not 0 <= self.annual_property_tax_rate <= 1:
            raise ValueError("Annual property tax rate must be between zero and one.")
        
        if self.annual_homeowners_insurance < 0:
            raise ValueError("Annual homeowners insurance cannot be negative.")
        
        if not 0 <= self.annual_mortgage_insurance_rate <= 1:
            raise ValueError("Annual mortgage insurance rate must be between zero and one.")
        
        if self.monthly_hoa_dues < 0:
            raise ValueError("Monthly HOA dues cannot be negative.")


@dataclass(frozen=True)
class MonthlyHousingCostBreakdown:
    principal_and_interest: float
    property_tax: float
    homeowners_insurance: float
    mortgage_insurance: float
    hoa_dues: float

    @property
    def total(self) -> float:
        return (
            self.principal_and_interest
            + self.property_tax
            + self.homeowners_insurance
            + self.mortgage_insurance
            + self.hoa_dues
        )


@dataclass(frozen=True)
class DtiLimits:
    maximum_front_end_ratio: float
    maximum_back_end_ratio: float

    def __post_init__(self) -> None:
        if not 0 < self.maximum_front_end_ratio <= 1:
            raise ValueError(
                "Maximum front-end ratio must be greater than zero "
                "and no greater than one."
            )
        
        if not 0 < self.maximum_back_end_ratio <= 1:
            raise ValueError(
                "Maximum back-end ratio must be greater than zero "
                "and no greater than one."
            )
        
        if self.maximum_front_end_ratio > self.maximum_back_end_ratio:
            raise ValueError(
                "Maximum front-end ratio cannot exceed "
                "maximum back-end ratio."
            )


@dataclass(frozen=True)
class MonthlyHousingBudget:
    front_end_limit: float
    back_end_limit_after_debt: float

    @property
    def maximum_housing_cost(self) -> float:
        return max(
            0,
            min(
                self.front_end_limit,
                self.back_end_limit_after_debt,
            ),
        )
    
    @property
    def limiting_factor(self) -> str:
        if self.front_end_limit <= self.back_end_limit_after_debt:
            return "front_end"
        
        return "back_end"