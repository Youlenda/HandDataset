# Hand Dataset (6720 Images)


This repository makes available the public dataset for the hand which has 6720 images. These images were captured by fifteen persons, nine women and six men, in eighteen different spaces with simple backgrounds. Other variation of data such as light condition, differnt capturing devise (mobile and laptop) and also diffrent resoulation were considered. The presented dataset consists of 4 classes which are Fist, Palm, Left and Right. Below links let you download training and validation set.

[Training Set (79 MB)](https://drive.google.com/file/d/1eo7kkq8zzrlWgcCcQh1Stkei_eZhIAbl/view?usp=sharing)

[Validation Set (9 MB)](https://drive.google.com/file/d/1sghCxu83xV_DIZ1qWA4eLg_-hAQh-Pxs/view?usp=sharing)


**Please notes that training set and validation set have different dixtributions.**

Each sample in training set is a 100×100x3 image associated with a label from 4 classes. Validation data were captured by [SSD Hand Detection] (https://github.com/victordibia/handtracking); So sample in validation set have different size but 3 dimensions.



In my case the dataset was classified with [EfficientNet-B0](https://arxiv.org/abs/1905.11946) and some fully connected layers in order to control pointer of mouse with hand detection and classification. 
