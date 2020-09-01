# Hand Dataset (6720 Images)


This repository makes available the public dataset for the hand which has 6720 images. These images were captured by fifteen persons, nine women and six men, in eighteen different spaces with simple backgrounds. Other variation of data such as light condition, differnt capturing devise (mobile and laptop) and also diffrent resoulation were considered. The presented dataset consists of 4 classes which are:
- Fist
- Palm
- Left
- Right

There are training set sample for each class in below:

<p align="center">
  <img width="400" height="400" src="https://github.com/YaldaForootan/HandDataset-6720Images-/blob/master/trainingset%20samples.jpg">
</p>

## Download dataset.
Following links let you download training and validation set.

[Training Set (79 MB)](https://drive.google.com/file/d/1eo7kkq8zzrlWgcCcQh1Stkei_eZhIAbl/view?usp=sharing)

[Validation Set (9 MB)](https://drive.google.com/file/d/1sghCxu83xV_DIZ1qWA4eLg_-hAQh-Pxs/view?usp=sharing)


**Please notes that training set and validation set have different dixtributions.**

Each sample in training set is a 100×100x3 image associated with a label from 4 classes. Validation data were captured by [SSD Hand Detection](https://github.com/victordibia/handtracking); So sample in validation set have different size but 3 dimensions.


## Train your model.
In my case the dataset was classified with [EfficientNet-B0](https://arxiv.org/abs/1905.11946) and some fully connected layers in order to control pointer of mouse with hand detection and classification. You can use the following code to unzip 6720 hand dataset and make your training data and its labels. 


```
!unzip training set

#Please change your training set path.
training_path = '/content/train'

x_train = []
y_train = []
count = 0
datacount = 0
lookup = dict()
reverselookup = dict()


for j in os.listdir(training_path):
    if not j.startswith('.'):
        lookup[j] = count
        reverselookup[count] = j
        count = count + 1

for i in range(0, 4):
    for j in os.listdir(training_path + '/' + str(i) + '/'):
        if not j.startswith('.'):
            count = 0
            img = Image.open(training_path + '/' + str(i) + '/' + j).convert("RGB")
            img = img.resize((100, 100))
            arr = np.array(img)
            x_train.append(arr) 
            count = count + 1
            y_values_t = np.full((count, 1), lookup[str(i)])
            y_train.append(y_values_t)
            datacount = datacount + count
x_train = np.array(x_train, dtype='float32')
y_train = np.array(y_train)
y_train = y_train.reshape(datacount)
```
