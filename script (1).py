
points = [(2, 3), (5, 7),(8,9),(11,13),(6,4)]
def euclideanDistance(point1,point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
print(f"En kısa uzaklık: {round(min(distances),3)}")
