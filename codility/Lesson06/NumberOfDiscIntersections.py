''' Module implements the solution to Codility, Lesson06 - Sorting, NumberOfDiscIntersections problem.

    Author: Miloš Pivaš, student
'''

class DiameterLine:
    ''' Represents a diameter line of a circle with given center and radius.

        The center is on the numbered axis, and both the center and radius are ints.

        Attributes
        ----------
        left : int
            Left endpoint of the diameter line.
        right : int
            Right endpoint of the diameter line.
    '''

    def __init__(self, center, radius):
        self.left = center - radius
        self.right = center + radius


def find_first_line_outside_right_border_idx(lines, left, border):
    ''' Finds the index of the first left point of a line in lines,
        that is outside the given right border.

        Uses binary search on attribute left of elements in lines.

        Parameters
        ----------
        lines : list
            List of DiameterLine.
            Elements need to be sorted by attribute [left]!

        border : int
            Right border.

        Returns
        -------
        out : int
            The index of the first left point outside the border.
    '''

    idx_left = left
    idx_right = len(lines)-1

    while idx_left <= idx_right:
        idx_mid = (idx_left+idx_right)//2
        point = lines[idx_mid].left

        if idx_left == idx_right:
            if point <= border:
                return idx_mid+1
            else:
                return idx_mid

        if point <= border:
            idx_left = idx_mid + 1
        elif point > border:
            idx_right = idx_mid - 1

    return idx_left


def count_intersections_in_sorted_lines(lines):
    ''' Counts the number of intersections inside the sorted list of lines.

        Parameters
        ----------
        lines : list
            List of DiameterLine.
            Elements need to be sorted by attribute [left]!

        Returns
        -------
        out : int
            The number of intersections.
    '''

    sol = 0
    for idx, l in enumerate(lines):
        idx_right = find_first_line_outside_right_border_idx(lines, idx, l.right)
        curr_intersections = idx_right - idx - 1
        sol += curr_intersections
    return sol


def solution(A):
    ''' Find the number of intersections of circles given by A.

        Circles' centers are on a numbered axis.
        Both centers and radii are ints,
        so touching at a single point also counts as an intersection.

        Parameters
        ----------
        A : list
            List of int. A[i] represents a circle with center on i, and radius = A[i]

        Returns
        -------
        out : int
            The number of intersections.
            -1 if the number exceeds 10,000,000.
    '''

    if len(A) <= 1:
        return 0

    lines = [DiameterLine(center, radius) for center, radius in enumerate(A)]

    lines.sort(key = lambda x : x.left)

    sol = count_intersections_in_sorted_lines(lines)

    if sol > 10000000:
        sol = -1

    return sol

