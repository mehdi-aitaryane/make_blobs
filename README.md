# Make_Blobs
This project generates and visualizes blob datasets with two modules: datasets.py and plots.py. The datasets.py module creates feature and target arrays with a random cluster model, radii, and noise. The plots.py module shows the scatter plot of the dataset with 2D or 3D plots. The project also has an example notebook that uses the modules.

## Mathematics Behind the Algorithm
The algorithm is based on the concept of clustering. The goal is to create a dataset that has a number of groups or clusters of data points. The algorithm initializes cluster centers and radii randomly, generates random features and adds noise, assigns target values based on the nearest cluster center, and adjusts the features to satisfy the cluster model.

## Pseudocode of the Algorithm
The pseudocode describes the steps of the make_blobs function, which takes the number of samples, features, centers, radii, balance, noise, and random state as input, and returns the feature and target arrays as output.

```
Procedure make_blobs:

Input: n_samples, n_features, n_centers, low_radius, high_radius, balanced, noise, random_state:

set the random seed to random_state

create cluster centers and radii using uniform random distribution

create probabilities for each cluster using uniform or balanced distribution

create targets using multinomial random distribution with probabilities

sort targets in ascending order

create features using normal random distribution with cluster centers and radii

add noise to features using normal random distribution

return features and targets
```

## Modules
The project contains two modules: datasets.py and plots.py. The datasets.py module has functions to generate and print the blob dataset. The plots.py module has functions to create 2D or 3D plots of the dataset.

## Notebook
The project has an example notebook that demonstrates how to use the modules to generate and visualize a blob dataset. The notebook imports the modules, generates a dataset using the make_blobs function, and visualizes the dataset using the scatter2D or scatter3D functions.

## Usage
To use the project, you need to import the modules, generate a dataset using the make_blobs function, and visualize the dataset using the scatter2D or scatter3D functions.

## Contributing
The project welcomes contributions from other users. They can open an issue or submit a pull request with their ideas or changes.

## License
The project is licensed under the terms of the MIT license.

