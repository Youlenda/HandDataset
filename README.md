# Hand Dataset (6720 Images)


This repository makes available the public dataset for the hand which has 6720 images. These images were captured by fifteen persons, nine women and six men, in eighteen different spaces with simple backgrounds. Other variation of data such as light condition, differnt capturing devise (mobile and laptop) and also diffrent resoulation were considered. The presented dataset consists of 4 classes which are:
- Fist
- Palm
- Left
- Right

Some of training samples for each class:

<p align="center">
  <img width="400" height="400" src="https://github.com/YaldaForootan/HandDataset-6720Images-/blob/master/trainingset%20samples.jpg">
</p>

## Download dataset.
Following links let you download training and validation set.

[Training Set (79 MB)]()

[Validation Set (9 MB)]()


**Please notice that training set and validation set have different distribution.**

Each sample in training set is a 100 × 100 x 3 image associated with a label from 4 classes. Validation data were captured by [SSD Hand Detection](https://github.com/victordibia/handtracking); Therefore, sample in validation set have different size but 3 dimensions.


## Train your model.
In my case, the dataset was classified with [EfficientNet-B0](https://arxiv.org/abs/1905.11946) and some fully connected layers in order to control pointer of mouse with hand detection and classification. After downloading dataset, you can use [load dataset.py](https://github.com/Youlenda/6720HandImages/blob/master/load%20dataset.py) to unzip 6720 hand images and make your training data and its labels. 

