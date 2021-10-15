from abc import ABC, abstractmethod


# interface
class CompanyWorker(ABC):
    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    def add(self, employee):
        pass

    def remove(self, employee):
        pass

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent


# basic component
class Employee(CompanyWorker):
    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary

    def do_work(self):
        print(f'{self.name} is working')

    def get_salary(self):
        print(f'{self.name} salary is {self.salary}')


# main composite class
class CompanyComposite(CompanyWorker):
    def __init__(self):
        self._workers = []

    def add(self, employee):
        self._workers.append(employee)
        employee.parent = self

    def remove(self, employee):
        self._workers.remove(employee)
        employee.parent = None

    def do_work(self):
        results = []
        for worker in self._workers:
            results.append(worker.do_work())
        return results

    def get_salary(self):
        results = []
        for worker in self._workers:
            results.append(worker.get_salary())
        return results


# composite class 1
class OfficeComposite(CompanyComposite):
    def __init__(self):
        super().__init__()


# composite class 2
class AccountingComposite(OfficeComposite):
    def __init__(self):
        super().__init__()


# client code for single component
def client_code_component(component):
    component.do_work()
    component.get_salary()
    print('')


# client code for composite
def client_code_composite(composite):
    composite.do_work()
    print('')
    composite.get_salary()


def main():
    component = Employee('Boss', '10000$')
    client_code_component(component)

    # create and add accounting workers to composite
    accounting_composite = AccountingComposite()

    head_accountant = Employee('Head Accountant', '5000$')
    assistant_accountant = Employee('Assistant Accountant', '2500$')

    accounting_composite.add(head_accountant)
    accounting_composite.add(assistant_accountant)

    # composite contains all office workers
    office_composite = OfficeComposite()

    receptionist = Employee('Receptionist', '1500$')

    office_composite.add(accounting_composite)
    office_composite.add(receptionist)

    # global composite
    company_composite = CompanyComposite()

    company_composite.add(office_composite)

    client_code_composite(company_composite)


if __name__ == '__main__':
    main()
