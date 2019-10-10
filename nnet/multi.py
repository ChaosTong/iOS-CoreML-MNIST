from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1, cache=True)
# print(mnist)
X, y = mnist['data'], mnist['target']
# print('x的大小为；', X.shape, '\n','x的大小为；', y)

# Common imports
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.externals import joblib

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "classification"

def save_fig(fig_id, tight_layout=True):
    path = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID, fig_id + ".png")
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)

def plot_digit(data):
    image = data.reshape(28, 28)
    plt.imshow(image, cmap = mpl.cm.binary,
               interpolation="nearest")
    plt.axis("off")

# EXTRA
def plot_digits(instances, images_per_row=10, **options):
    size = 28
    images_per_row = min(len(instances), images_per_row)
    images = [instance.reshape(size,size) for instance in instances]
    n_rows = (len(instances) - 1) // images_per_row + 1
    row_images = []
    n_empty = n_rows * images_per_row - len(instances)
    images.append(np.zeros((size, size * n_empty)))
    for row in range(n_rows):
        rimages = images[row * images_per_row : (row + 1) * images_per_row]
        row_images.append(np.concatenate(rimages, axis=1))
    image = np.concatenate(row_images, axis=0)
    plt.imshow(image, cmap = mpl.cm.binary, **options)
    plt.axis("off")

some_digit = X[36000]
# some_digit_image = some_digit.reshape(28, 28)
# plt.imshow(some_digit_image, cmap = mpl.cm.binary,
#            interpolation="nearest")
# plt.axis("off")

# save_fig("some_digit_plot")
# plt.show()

# plt.figure(figsize=(9,9))
# example_images = np.r_[X[:12000:600], X[13000:30600:600], X[30600:60000:590]]
# plot_digits(example_images, images_per_row=10)
# save_fig("more_digits_plot")
# plt.show()

# 创建测试集
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
# 打乱测试集
shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
print(y_train)
# y_train = y_train.astype(np.int8)
print(X_train)
print(y_train)
from sklearn.linear_model import SGDClassifier

sgd_clf = SGDClassifier(max_iter=5, tol=-np.infty, random_state=42)

sgd_clf.fit(X_train, y_train)
predict = sgd_clf.predict([some_digit])
print(predict)

some_digit_scores = sgd_clf.decision_function([some_digit])
print(some_digit_scores)

from sklearn.ensemble import RandomForestClassifier
forest_clf = RandomForestClassifier(n_estimators=10, random_state=42)
forest_clf.fit(X_train, y_train)
joblib.dump(forest_clf, 'forest_clf.pkl')
print(forest_clf.predict([some_digit]))

print(forest_clf.predict_proba([some_digit]))