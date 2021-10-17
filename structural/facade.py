from abc import ABC, abstractmethod


class Facade:
    def __init__(self, photo):
        self._importer = PhotoImporter(photo)
        self._editor = BlackWhiteEditor(photo)
        self._exporter = PhotoExporter(photo)

    def edit_photo(self):
        import_ = self._importer.import_photo()
        edit = self._editor.edit_photo()
        export = self._exporter.export_photo()

        print(import_)
        print(edit)
        print(export)


class PhotoImporter:
    def __init__(self, photo):
        self._photo = photo

    def import_photo(self):
        return f'{self._photo} is imported'


class PhotoEditor(ABC):
    def __init__(self, photo):
        self._photo = photo

    @abstractmethod
    def edit_photo(self):
        pass


class BlackWhiteEditor(PhotoEditor):
    def edit_photo(self):
        return f'{self._photo} is edited. It\'s black and white now'


class PictureEditor(PhotoEditor):
    def edit_photo(self):
        return f'{self._photo} is edited. It\'s picture styled now'


class PhotoExporter:
    def __init__(self, photo):
        self._photo = photo

    def export_photo(self):
        return f'{self._photo} is exported'


def client_code(facade: Facade):
    facade.edit_photo()


def main():
    facade = Facade('my_portrait.jpeg')
    client_code(facade)


if __name__ == '__main__':
    main()
