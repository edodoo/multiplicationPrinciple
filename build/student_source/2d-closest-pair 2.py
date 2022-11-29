def closest(points):
    #Let m be the median x-coordinate of the pts in points.
    m = median(points, lambda p: p[0])
    #Let left be the subset of points with x-coordinates less than m.
    left = [p for p in points if p[0] < m]
    #Let right be the subset of points with x-coordinates greater than m.
    right = [p for p in points if p[0] > m]
    #If |left| is empty, then the closest pair of points in right is the closest pair in points.
    if not left:
        return closest(right)
    #Otherwise, if |right| is empty, then the closest pair of points in left is the closest pair in points.
    elif not right:
        return closest(left)
    #Otherwise, the closest pair of points in left and right is the closest pair in points.
    else:
        return closest(left) + closest(right)

def median(points, f):
    #Let pts be the list of points in points.
    pts = points[:]
    #Let pts be sorted by f.
    pts.sort(key=f)
    #Let n be the number of points in pts.
    n = len(pts)
    #If n is odd, then the median is the point at index ((n-1)/2) in pts.
    if n % 2 == 1:
        return pts[(n-1)//2]
    #Otherwise, the median is the average of the points at indices ((n-1)/2) and ((n-1)/2)+1 in pts.
    else:
        return (pts[(n-1)//2] + pts[(n-1)//2 + 1]) / 2
    
# Test the above code
points = [(0,0), (1,1), (2,3)]
print(closest(points))
points = [(0,0), (1,1), (2,3), (3,2), (4,4)]
print(closest(points))


