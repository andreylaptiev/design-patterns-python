class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def create_new_instance(self):
        return Singleton()


if __name__ == '__main__':
    s = Singleton()
    s1 = s.create_new_instance()
    print(s == s1)
    print(s is s1)
