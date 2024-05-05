#!/usr/bin/python3
"""
Module for lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each sublist represents a box
                      and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    # Set to keep track of visited boxes
    visited = set()
    visited.add(0)  # Start with the first box open

    # Queue for BFS traversal
    queue = [0]

    # BFS traversal
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
