from collections.abc import Iterator, Iterable


# concrete iterator
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        boys_students = []
        girls_students = []

        try:
            for _ in self._collection:
                student = self._collection[self._index]
                self._index += 1

                for k, v in student.items():
                    if v == 'Boy':
                        boys_students.append(student)
                    else:
                        girls_students.append(student)
        except IndexError:
            raise StopIteration()

        return boys_students, girls_students


# concrete iterable
class ConcreteIterable(Iterable):
    def __init__(self, collection,):
        self._collection = collection

    def __iter__(self):
        return ConcreteIterator(self._collection)

    def get_students(self):
        return self.__iter__().__next__()


def client_code():
    collection = [{'John': 'Boy'}, {'Ann': 'Girl'}, {'Kate': 'Girl'}, {'Tom': 'Boy'}]

    iterable = ConcreteIterable(collection)
    iteration = iterable.get_students()

    print('Iteration result: boys students')
    print(iteration[0], end='\n\n')

    print('Iteration result: girls students')
    print(iteration[1])


def main():
    client_code()


if __name__ == '__main__':
    main()
