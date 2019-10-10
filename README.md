> 几次尝试写一个简单的分类器, 试图转到iOS都失败了, 终于走通了一次

# iOS-CoreML-MNIST
使用 scikit-learn RandomForestClassifier 输出Model, 使用 CoreMLTools 转换成iOS可食用的Model, 简单将流程走通
数据使用MNist, 识别手写数字0-9

## Requirements

- Xcode 11.0
- iOS 13.1
- For training: Python 3.7.4 (scikit-learn 0.20.3, CoreMLTools 3.0)

## Usage

[原项目使用Keras](https://github.com/r4ghu/iOS-CoreML-MNIST), 看机器学习实战书, 尝试使用Scikit-Learn实现

## Training

[教程](https://github.com/ageron/handson-ml) 03_classification 分类

## Results

These are the results of the app when tested on iPhone XR. 

<img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0266.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0267.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0268.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0269.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0270.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0271.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0272.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0273.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0275.PNG" alt="Result 1" width="280"> <img src="https://github.com/ChaosTong/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0276.PNG" alt="Result 1" width="280">

## Author

ChaosTong / [@ChaosTong](https://weibo.com/2048284377/profile)
