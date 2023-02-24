"""
Issues with this code:
- Duplication (HourlyEmployeeWithCommission and SalariedEmployeeWithCommission
are very similar)
- Class explosion: if we have more types of employees, we need NewEmployee and
NewEmployeeWithComission
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Employee(ABC):
    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        pass

@dataclass
class HourlyEmployee(Employee):
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


def main() -> None:
    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()