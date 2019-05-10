import math

class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense

def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0, labels[0]))
    data.append(item(0, 0, 0, 1, labels[1]))
    data.append(item(0, 0, 1, 0, labels[2]))
    data.append(item(0, 0, 1, 1, labels[3]))
    data.append(item(0, 1, 0, 0, labels[4]))
    data.append(item(0, 1, 0, 1, labels[5]))
    data.append(item(0, 1, 1, 0, labels[6]))
    data.append(item(0, 1, 1, 1, labels[7]))
    data.append(item(1, 0, 0, 0, labels[8]))
    data.append(item(1, 0, 0, 1, labels[9]))
    data.append(item(1, 0, 1, 0, labels[10]))
    data.append(item(1, 0, 1, 1, labels[11]))
    data.append(item(1, 1, 0, 0, labels[12]))
    data.append(item(1, 1, 0, 1, labels[13]))
    data.append(item(1, 1, 1, 0, labels[14]))
    data.append(item(1, 1, 1, 1, labels[15]))
    data.append(item(1, 0, 0, 0, labels[16]))
    data.append(item(1, 0, 0, 1, labels[17]))
    data.append(item(1, 0, 1, 0, labels[18]))
    data.append(item(1, 0, 1, 1, labels[19]))
    data.append(item(1, 1, 0, 0, labels[20]))
    return data

class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1
        self.left = -1 #zero
        self.right = -1 #one
        self.decision_left = -1
        self.decision_right = -1
        self.new_index = -1

def data_def():
    data = getDataset()
    attributes = [[], [], [], [], []]  # mesh 3arfa akhleeh genereic 3shan item sabet aslan
    for row in data:
        attributes[0].append(row.age)
        attributes[1].append(row.prescription)
        attributes[2].append(row.astigmatic)
        attributes[3].append(row.tearRate)
        attributes[4].append(row.needLense)
    return attributes


class ID3:
    def __init__(self, features):
        self.features = features
        self.data_set = []
        self.labels = []
        self.dataset_entropy = -1
        self.classifier = []

    def divide_column(self, column, index):
        true = []
        false = []
        for i in range(len(column)):
            if self.data_set[index][column[i]] == 1:
                true.append(column[i])
            else:
                false.append(column[i])
        return true, false

    def classify(self, input):
        # takes an array for the features ex. [0, 0, 1, 1]
        # should return 0 or 1 based on the classification
        classifier_index = 0
        tree = self.classifier
        while True and classifier_index < len(self.classifier):
            start_index = self.classifier[classifier_index].new_index
            if input[start_index] == 0:
                if input[start_index] == self.classifier[classifier_index].left:
                    return self.classifier[classifier_index].decision_left
            else:
                if input[start_index] == self.classifier[classifier_index].right:
                    return self.classifier[classifier_index].decision_right
            classifier_index += 1

    def entropy(self, column):
        yes = column.count(1)
        no = column.count(0)
        entropy_value = 0

        if len(column) > 0:
            yes = yes / len(column)
        if len(column) > 0:
            no = no / len(column)

        if yes > 0:
            entropy_value = yes * math.log2(yes)
        if no > 0:
            entropy_value += no * math.log2(no)

        entropy_value *= -1
        return entropy_value

    def information_gain(self, column, indexes):
        class1 = []  # labels of class 1 of the attribute
        class2 = []  # labels of class 2 of the attribute

        column_labels = []
        for i in range(len(indexes)):
            column_labels.append(self.labels[indexes[i]])

        total_entropy = self.entropy(column_labels)

        i = 0

        for value in column:
            if value == 0:
                class1.append(self.labels[indexes[i]])
            else:
                class2.append(self.labels[indexes[i]])
            i += 1

        entropy1 = self.entropy(class1)
        entropy2 = self.entropy(class2)

        information_gain = total_entropy - (entropy1 * len(class1)/len(column) + entropy2 * len(class2)/len(column))
        return information_gain

    def init_model(self):

        self.data_set = data_def()  # get dataset
        self.labels = self.data_set[4]  # labels of each item

        self.dataset_entropy = self.entropy(self.labels)

        max_info_gain = -100000
        index = -1

        index_list = []
        for i in range(len(self.data_set[0])):
            index_list.append(i)

        for i in range(4):
            info_gain = self.information_gain(self.data_set[i], index_list)
            if info_gain > max_info_gain:
                max_info_gain = info_gain
                index = i

        self.features[index].visited = 1
        self.features[index].new_index = index
        self.classifier.append(features[index])

        self.train_model(index, index_list)

    def train_model(self, node_index, index_list):

        self.features[node_index].visited = 1
        max_info_gain = -100000000
        index = -1

        true_index, false_index = self.divide_column(index_list, node_index)

        true = []
        false = []

        for i in range(len(true_index)):
            true.append(self.labels[true_index[i]])

        for i in range(len(false_index)):
            false.append(self.labels[false_index[i]])

        entropy1 = self.entropy(true)
        entropy2 = self.entropy(false)

        if entropy2 != 0:

            for i in range(4):
                if self.features[i].visited == 1:
                    continue

                column = []

                for j in range(len(false_index)):
                    column.append(self.data_set[i][false_index[j]])

                info_gain = self.information_gain(column, false_index)
                if info_gain > max_info_gain:
                    max_info_gain = info_gain
                    index = i

            if index == -1:
                return
            self.features[index].new_index = index
            self.features[index].visited = 1
            self.classifier.append(self.features[index])
            self.train_model(index, false_index)
        else:
            self.classifier[len(self.classifier) - 1].left = 0
            self.classifier[len(self.classifier) - 1].decision_left = self.labels[false_index[0]]

        if entropy1 != 0:
            max_info_gain = -100000000
            index = -1

            for i in range(4):
                if self.features[i].visited == 1:
                    continue
                column = []

                for j in range(len(true_index)):
                    column.append(self.data_set[i][true_index[j]])

                info_gain = self.information_gain(column, true_index)

                if info_gain > max_info_gain:
                    max_info_gain = info_gain
                    index = i
            if index == -1:
                return
            self.features[index].new_index = index
            self.features[index].visited = 1
            self.classifier.append(self.features[index])
            self.train_model(index, true_index)
        else:
            if len(true_index) > 0:
                self.classifier[len(self.classifier) -1].right = 1
                self.classifier[len(self.classifier) -1].decision_right = self.labels[true_index[0]]


features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]

id3 = ID3(features)
id3.init_model()

cls = id3.classify([0, 0, 1, 1])  # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0])  # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0])  # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1])  # should print 1
print('testcase 4: ', cls)