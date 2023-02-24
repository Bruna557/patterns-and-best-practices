from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Contract(ABC):
    @abstractmethod
    def get_payment(self) -> float:
        pass


class Commission(ABC):
    @abstractmethod
    def get_payment(self) -> float:
        pass


@dataclass
class ContractCommission(Commission):
    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        return self.commission * self.contracts_landed


@dataclass
class Employee(ABC):
    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout

@dataclass
class HourlyContract(Contract):
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


def main() -> None:
    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract = henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=47832, contract = sarah_contract, commission = sarah_commission
    )
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()