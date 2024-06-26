import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature      # Feature index
        self.threshold = threshold  # Threshold value for numerical features
        self.left = left            # Left subtree (less than or equal to threshold)
        self.right = right          # Right subtree (greater than threshold)
        self.value = value          # Value if node is a leaf (class label)

class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        # Check termination criteria
        if depth == self.max_depth or len(set(y)) == 1:
            return Node(value=max(set(y), key=y.count))

        n_samples, n_features = X.shape
        best_feature, best_threshold = self._find_best_split(X, y)

        if best_feature is None:
            return Node(value=max(set(y), key=y.count))

        left_indices = X[:, best_feature] <= best_threshold
        right_indices = X[:, best_feature] > best_threshold

        left_subtree = self._build_tree(X[left_indices], y[left_indices], depth + 1)
        right_subtree = self._build_tree(X[right_indices], y[right_indices], depth + 1)

        return Node(feature=best_feature, threshold=best_threshold, left=left_subtree, right=right_subtree)

    def _find_best_split(self, X, y):
        n_samples, n_features = X.shape
        best_gini = float('inf')
        best_feature = None
        best_threshold = None

        for feature_idx in range(n_features):
            unique_values = np.unique(X[:, feature_idx])
            for threshold in unique_values:
                left_indices = X[:, feature_idx] <= threshold
                right_indices = X[:, feature_idx] > threshold

                gini = self._gini_index(y[left_indices], y[right_indices])
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature_idx
                    best_threshold = threshold

        return best_feature, best_threshold

    def _gini_index(self, left_y, right_y):
        n_left = len(left_y)
        n_right = len(right_y)
        n_total = n_left + n_right

        if n_left == 0 or n_right == 0:
            return 0

        left_gini = 1 - sum((np.sum(left_y == c) / n_left) ** 2 for c in set(left_y))
        right_gini = 1 - sum((np.sum(right_y == c) / n_right) ** 2 for c in set(right_y))

        weighted_gini = (n_left / n_total) * left_gini + (n_right / n_total) * right_gini

        return weighted_gini

    def predict(self, X):
        return np.array([self._predict_tree(x, self.tree) for x in X])

    def _predict_tree(self, x, node):
        if node.value is not None:
            return node.value

        if x[node.feature] <= node.threshold:
            return self._predict_tree(x, node.left)
        else:
            return self._predict_tree(x, node.right)

# Example usage:
if __name__ == "__main__":
    # Sample data (binary classification)
    X = np.array([[2.771244718,1.784783929],
                  [1.728571309,1.169761413],
                  [3.678319846,2.81281357],
                  [3.961043357,2.61995032],
                  [2.999208922,2.209014212],
                  [7.497545867,3.162953546],
                  [9.00220326,3.339047188],
                  [7.444542326,0.476683375],
                  [10.12493903,3.234550982],
                  [6.642287351,3.319983761]])
    y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    # Initialize and train the decision tree
    tree = DecisionTreeClassifier(max_depth=3)
    tree.fit(X, y)

    # Predictions
    test_data = np.array([[3, 2], [5, 5]])
    predictions = tree.predict(test_data)
    for i, pred in enumerate(predictions):
        print(f"Data {test_data[i]} predicted class: {pred}")
