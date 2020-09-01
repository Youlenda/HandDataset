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
