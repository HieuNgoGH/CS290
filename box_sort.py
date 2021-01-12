# Hieu Ngo
# Project 4b
# 10/19/2020

class Box:
    """A class that takes length, width, and height as parameters."""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """Returns the volume of a box."""
        return self._length * self._width * self._height

    def get_length(self):
        """Returns the length of a box."""
        return self._length

    def get_width(self):
        """Returns the width of a box."""
        return self._width

    def get_height(self):
        """Returns the height of a box."""
        return self._height

def box_sort(list_here):
    """Sorts a list in descending order."""

    unraveled_boxes = []
    for box in list_here:
        box_volume = Box.volume(box)
        unraveled_boxes.append(box_volume)

    for index in range(1, len(unraveled_boxes)):
        value = unraveled_boxes[index]
        position = index - 1
        while position >= 0 and unraveled_boxes[position].volume() < value.volume():
            unraveled_boxes[position + 1] = unraveled_boxes[position]
            position -= 1
        unraveled_boxes[position + 1] = value
    return unraveled_boxes

b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
b4 = Box(2, 3, 4)
b5 = Box(10, 10, 10)
box_list = [b2, b3, b4, b5]
print(box_sort(box_list))