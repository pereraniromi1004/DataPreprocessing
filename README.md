# DataPreprocessing
data preprocessing using python and R


The sklearn.preprocessing package provides several common utility functions and transformer classes to change raw feature vectors into a representation that is 
more suitable for the downstream estimators.

In general, learning algorithms benefit from standardization of the data set. If some outliers are present in the set, robust scalers or transformers are more appropriate.
The behaviors of the different scalers, transformers, and normalizers on a dataset containing marginal outliers
is highlighted in Compare the effect of different scalers on data with outliers.
Standardization of datasets is a common requirement for many machine learning estimators implemented in scikit-learn; 
they might behave badly if the individual features do not more or less look like standard normally distributed data: Gaussian with zero mean and unit variance.

In practice we often ignore the shape of the distribution and just transform the data to center it by removing the mean value of each feature,
then scale it by dividing non-constant features by their standard deviation.

For instance, many elements used in the objective function of a learning algorithm (such as the RBF kernel of
Support Vector Machines or the l1 and l2 regularizers of linear models) assume that all features are centered around zero and have variance in the same order.
If a feature has a variance that is orders of magnitude larger than others, it might dominate the objective function and make the estimator unable to learn from other
features correctly as expected.

The preprocessing module provides the StandardScaler utility class, which is a quick and easy way to perform the following operation on an array-like dataset:
It is possible to disable either centering or scaling by either passing with_mean=False or with_std=False to the constructor of StandardScaler.
