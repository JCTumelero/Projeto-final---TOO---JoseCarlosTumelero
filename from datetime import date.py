from datetime import date


class SecaoQuarta:
    def __init__(self, data: date):
        self._data = data

    @property
    def data(self) -> date:
        return self._data

    @data.setter
    def data(self, value: date):
        self._data = value












