import numpy as np

# This function counts the occurrences of each unique value in the input array y and prints them.
# Parameters:
# y: np.ndarray, Input array of target values
# Returns: None

def count_occurances(y):
    arr = np.unique(y, return_counts=True)
    for i in range(len(arr[0])):
        print("class ", arr[0][i], " has ", arr[1][i], " items")

# This function prints the shapes of the input arrays X and y.
# Parameters:
# X: np.ndarray, Input array of features
# y: np.ndarray, Input array of target values
# Returns: None

def print_shape(X, y):
    print("X shape is ", X.shape)
    print("y shape is ", y.shape)

# This function generates a blob dataset with a specified number of samples, features, centers, radii, balance, noise, and random state
# n_samples: the number of samples in the dataset
# n_features: the number of features in the dataset
# n_centers: the number of clusters or centers in the dataset
# low_radius: the lower bound of the radii of the clusters
# high_radius: the upper bound of the radii of the clusters
# balanced: a boolean value indicating whether the clusters have equal probabilities or not
# noise: the standard deviation of the noise added to the features
# random_state: the seed for the random number generator

def make_blobs(n_samples=100, n_features=20, n_centers=2, low_radius = 0.01, high_radius = 0.035, balanced = True, noise = 0.0, random_state=None):
    np.random.seed(random_state)

    # Create balanaced or unbalanced samples
    size = n_samples // n_centers
    rest = n_samples % n_centers
    prob = np.random.uniform(size=(n_centers))
    prob = np.where(balanced == True, [1/n_centers] * n_centers, prob / sum(prob))
    # Generate target values
    y = np.random.choice(n_centers, n_samples, replace=True, p=prob)
    y = np.sort(y)
    blob_centers = np.random.uniform(size=(n_centers, n_features))
    blob_radius = np.random.uniform(low=low_radius, high=high_radius, size=n_centers)
    class_sizes = np.bincount(y)

    features = [center + radius * np.random.randn(samples, n_features)
         for center, radius, samples in zip(blob_centers, blob_radius, class_sizes)]
    
    X = np.concatenate(features)
    X += np.random.normal(scale=noise, size=(n_samples, n_features))
    return X, y