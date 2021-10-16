from abc import ABC, abstractmethod


# abstract class
class CompanyComponent(ABC):
    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    def get_composite(self):
        return None

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent


# primitive component
class Employee(CompanyComponent):
    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary

    def do_work(self):
        print(f'{self.name} is working')

    def get_salary(self):
        print(f'{self.name} salary is {self.salary}')

    def add(self, component: CompanyComponent):
        raise Exception('This is not a composite')

    def remove(self, component: CompanyComponent):
        raise Exception('This is not a composite')


# base composite component
class CompanyComposite(CompanyComponent):
    def __init__(self):
        self._workers = []

    def get_composite(self):
        return self

    def add(self, component: CompanyComponent):
        self._workers.append(component)
        component.parent = self

    def remove(self, component: CompanyComponent):
        self._workers.remove(component)
        component.parent = None

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


# composite component for all office workers
class OfficeComposite(CompanyComposite):
    def __init__(self):
        super().__init__()


# composite component for accounting workers
class AccountingComposite(OfficeComposite):
    def __init__(self):
        super().__init__()


# client code to work with primitive components
def client_code_primitive(component: CompanyComponent):
    component.do_work()
    component.get_salary()
    print('')


# client code to work with composite components
def client_code_composite(component: CompanyComponent):
    component.do_work()
    print('')
    component.get_salary()


def main():
    primitive_component = Employee('Boss', '10000$')
    client_code_primitive(primitive_component)

    # create and add primitive components (accounting workers) to composite component
    head_accountant = Employee('Head Accountant', '5000$')
    assistant_accountant = Employee('Assistant Accountant', '2500$')

    accounting_composite = AccountingComposite()

    if accounting_composite.get_composite():
        accounting_composite.add(head_accountant)
        accounting_composite.add(assistant_accountant)

    # office composite component contains all primitive and composite components (all office workers)
    receptionist = Employee('Receptionist', '1500$')

    office_composite = OfficeComposite()

    if office_composite.get_composite():
        office_composite.add(accounting_composite)
        office_composite.add(receptionist)

    # base composite component contains all components of the company
    composite_component = CompanyComposite()

    composite_component.add(office_composite)

    client_code_composite(composite_component)


if __name__ == '__main__':
    main()
