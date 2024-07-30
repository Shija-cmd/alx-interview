#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Prototype: def canUnlockAll(boxes)
	boxes is a list of lists
	A key with the same number as a box opens that box
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for id_x in range(len(boxes)):
            boxes_checked = k in boxes[id_x] and k != id_x
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
