class StorageContainer(object):
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def _getTotalArea(self):
        area = 0
        area = self._length * self._width
        return area
    def _getCubicArea(self):
        cArea = 0
        cArea = self._length * self._width * self._height
        return cArea


    def __str__(self):
        return f'Length: {self._length:.2f} m\nHeight: {self._height:.2f} m\nWidth: {self._width:.2f} m\nArea: {self._getTotalArea():.2f} square metres\nStorage Capacity: {self._getCubicArea():.2f} cubic metres'
