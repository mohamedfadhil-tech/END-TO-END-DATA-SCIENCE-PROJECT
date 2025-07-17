# Manually created dataset (example-based)
samples = [
    [5.1, 3.5, 1.4, 0.2, 'setosa'],
    [7.0, 3.2, 4.7, 1.4, 'versicolor'],
    [6.3, 3.3, 6.0, 2.5, 'virginica'],
    [5.8, 2.7, 5.1, 1.9, 'virginica'],
    [6.1, 2.8, 5.6, 2.4, 'virginica'],
    [5.0, 3.6, 1.4, 0.2, 'setosa'],
    [5.7, 2.8, 4.5, 1.3, 'versicolor'],
]

# Simple rule-based prediction (mock classifier)
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    if petal_length < 2.0:
        return 'setosa'
    elif petal_length < 5.0:
        return 'versicolor'
    else:
        return 'virginica'

# Test the function
sample_input = (6.1, 2.8, 5.6, 2.4)
result = predict_species(*sample_input)
print("Predicted species:", result)
