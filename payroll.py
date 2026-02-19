# Author: Ricky Kerr
# Date: 2/19/26
# File: payroll.py
# Description: writing functions to demonstrate polymorphism and serialize payroll and build payroll data
from payable import Payable
from invoice import Invoice
from person import Person
from manager import Manager
from executivemanager import ExecutiveManager
from secretary import Secretary
from salesperson import Salesperson

def serialize_payroll(payable: Payable) -> dict:
    # turn any payable object into a plain dictionary
    return payable.to_dict()


def build_payroll_data() -> dict:
    # One list that mixes invoices and employees together
    payables = []

    # Invoices
    payables.append(Invoice("Printer Cartridge", 75.5, 3))
    payables.append(Invoice("Monitor Stand", 42.99, 2))

    # People
    p1 = Person("Alice", "Wong", "F", "123-45-6789")
    p2 = Person("Thomas", "Cho", "M", "987-65-4321")
    p3 = Person("Elena", "Stone", "F", "222-33-444")
    p4 = Person("John", "Davis", "M", "111-22-333")

    # Employees
    payables.append(Secretary(p1, 101, 2, 25, 40))
    payables.append(Manager(p2, 102, 8, 8500, "IT"))
    payables.append(ExecutiveManager(p3, 103, 10, 14500.0, "Operations",2500))
    payables.append(Salesperson(p4, 104, 4, 15000.0, 0.08))

    # Serialize + totals
    payables_data = []
    total_invoices = 0
    total_employees = 0
    total_gross = 0.0

    for obj in payables:
        payables_data.append(serialize_payroll(obj))
        if isinstance(obj, Invoice):
            total_invoices += 1
        else:
            total_employees += 1

        total_gross += float(obj.calculate_payment())

    return {
        "payables": payables_data,
        "invoice_count": total_invoices,
        "employee_count": total_employees,
        "total_gross": round(total_gross, 2),
    }

print(build_payroll_data())
print(Invoice.get_invoice_count())
