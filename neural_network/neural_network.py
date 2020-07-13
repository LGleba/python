# 2020
# Neural Network
# Designed and powered by LGleba

from numpy import exp, array, random, dot


def sigmoid(x):
    """
    Sigmoid function
    :param x: x coordinate
    :return: value of function
    """
    return 1 / (1 + exp(-x))


def sigmoid_derivative(x):
    """
    Derivative sigmoid
    :param x: x coordinate
    :return: value of function
    """
    return x * (1 - x)


def find_result(array):
    result = sigmoid(dot(test, weights))
    print(f"Result: {result}")


weights = 2 * random.random((4, 1)) - 1                             # [n][1]
print(f"Weights before:\n{weights}\n")

train_input = array([[0, 0, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0],
                     [0, 0, 1, 1],
                     [0, 1, 0, 0],
                     [0, 1, 0, 1]])
train_output = array([[0, 0, 1, 1, 0, 0]]).T                        # [n][1]

for i in range(1000):
    result = sigmoid(dot(train_input, weights))                     # [n][1]
    error = train_output - result                                   # [n][1]
    diff = dot(train_input.T, error * sigmoid_derivative(result))   # [n][1]
    weights += diff                                                 # [n][1]

print(f"Weights after:\n{weights}\n")

test = array([0, 1, 0, 1])
find_result(test)
