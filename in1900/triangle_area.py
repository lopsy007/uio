def triangle_area(vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    return 1/2 * abs( x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x1*y1 )

def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0,0];  v2 = [1,0];  v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg

test_triangle_area()
