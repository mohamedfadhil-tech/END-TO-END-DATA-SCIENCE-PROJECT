iris_data = [
    ([5.1, 3.5, 1.4, 0.2], 'setosa'),
    ([4.9, 3.0, 1.4, 0.2], 'setosa'),
    ([6.2, 3.4, 5.4, 2.3], 'virginica'),
    ([5.9, 3.0, 5.1, 1.8], 'virginica'),
    ([5.6, 2.9, 3.6, 1.3], 'versicolor'),
    ([6.7, 3.1, 4.7, 1.5], 'versicolor'),
]

def euclidean_distance(point1, point2):
    return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5


def knn_classify(data, query, k=3):
    # Calculate distances from query to all points
    distances = []
    for features, label in data:
        dist = euclidean_distance(features, query)
        distances.append((dist, label))
    
    distances.sort(key=lambda x: x[0])  
    
    nearest_labels = [label for _, label in distances[:k]]

    votes = {}
    for label in nearest_labels:
        votes[label] = votes.get(label, 0) + 1
    
    return max(votes, key=votes.get)

test_points = [
    [5.0, 3.4, 1.5, 0.2],  # Expected: setosa
    [6.0, 2.9, 4.5, 1.5],  # Expected: versicolor
    [6.5, 3.0, 5.5, 2.0],  # Expected: virginica
]

for i, point in enumerate(test_points, 1):
    prediction = knn_classify(iris_data, point, k=3)
    print(f"Test Point {i}: {point} => Predicted Species: {prediction}")
