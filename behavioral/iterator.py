from collections.abc import Iterator, Iterable
from abc import ABC, abstractmethod


# iterators abstract class
class StudentIterator(ABC, Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    @abstractmethod
    def __next__(self):
        pass


# collections abstract class
class StudentCollection(ABC, Iterable):
    def __init__(self, collection,):
        self._collection = collection

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get_students(self):
        pass


# concrete iterator for boys
class BoyIterator(StudentIterator):
    def __init__(self, collection: StudentCollection):
        super().__init__(collection)

    def __next__(self):
        boys_students = []

        try:
            for _ in self._collection:
                student = self._collection[self._position]
                self._position += 1

                for k, v in student.items():
                    if v == 'Boy':
                        boys_students.append(student)
                    else:
                        continue

        except IndexError:
            raise StopIteration()

        return boys_students


# concrete iterator for girls
class GirlIterator(StudentIterator):
    def __init__(self, collection: StudentCollection):
        super().__init__(collection)

    def __next__(self):
        girls_students = []

        try:
            for _ in self._collection:
                student = self._collection[self._position]
                self._position += 1

                for k, v in student.items():
                    if v == 'Girl':
                        girls_students.append(student)
                        continue
                    else:
                        continue

        except IndexError:
            raise StopIteration()

        return girls_students


# concrete collection to get boys
class BoyStudent(StudentCollection):
    def __init__(self, collection):
        super().__init__(collection)

    def __iter__(self):
        return BoyIterator(self._collection)

    def get_students(self):
        return self.__iter__().__next__()


# concrete collection to get girls
class GirlStudent(StudentCollection):
    def __init__(self, collection):
        super().__init__(collection)

    def __iter__(self):
        return GirlIterator(self._collection)

    def get_students(self):
        return self.__iter__().__next__()


def client_code():
    collection = [{'John': 'Boy'}, {'Ann': 'Girl'}, {'Kate': 'Girl'}, {'Tom': 'Boy'}]

    # concrete collections
    boys = BoyStudent(collection)
    girls = GirlStudent(collection)

    # iterations
    print('Iteration result: boys students')
    iteration1 = boys.get_students()
    print(iteration1)
    print('')

    print('Iteration result: girls students')
    iteration2 = girls.get_students()
    print(iteration2)


def main():
    client_code()


if __name__ == '__main__':
    main()
