# Q1) Given a list of 2-D coordinates, write a function that returns True
#     if the points lie on a straight line and False otherwise.
#
#     Use only the Python standard libraries.
#
# collinear([[1,1], [2,2], [4,4], [-10, -10]]) = True
# collinear([[1,0], [2,0], [3,1]]) = False


def collinear(points):
    if len(points) < 2:
        return True

    p1, p2 = points[:2]
    # Explanation:
    # (p[0] - p1[0]) * (p2[1] - p1[1]) != (p[1] - p1[1]) * (p2[0] - p1[0])
    # This is the formula for the slope of the line between two points.
    # If the slope is the same for all points, then they are on a straight line.
    for p in points[2:]:
        if (p[0] - p1[0]) * (p2[1] - p1[1]) != (p[1] - p1[1]) * (p2[0] - p1[0]):
            return False
    return True


# Write test cases to test the function
print(collinear([[1, 1], [2, 2], [4, 4], [-10, -10]]))
print(collinear([[1, 0], [2, 0], [3, 1]]))
