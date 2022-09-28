from doctest import testfile
import glob, os
import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--dataset', default='dataset', help='Dataset Folder Name')
parser.add_argument('--test', type=int, default=20, help='Test Percentage')
parser.add_argument('--valid', type=int, default=10, help='Test Percentage')

args = parser.parse_args()

percentage_test = args.test
folder_name = args.dataset
ext_list = ['.JPG','.jpg','.PNG','.png','.JPEG','.jpeg']

current_dir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.basename(os.getcwd())

counter = 0
#dataset_file = open('dataset.txt', 'w+')
train_file = open('train.txt', 'w+')
test_file = open('test.txt', 'w+')
valid_file = open('valid.txt', 'w+')

dataset_list = []

total = 0

test_index = 0
train_percent = 0
valid_index = 0

file_list = []
if os.path.isdir(folder_name):
        
    for subdir, dirs, files in os.walk(folder_name):

        for dir in dirs:
            
            dataset_path = os.path.join(folder_name,dir)

            for ext in ext_list:
                for pathAndFilename in glob.iglob(os.path.join(dataset_path, '*'+ext)):

                    title, exts = os.path.splitext(os.path.basename(pathAndFilename))
                    dataset_list.append(os.path.join(basedir, dataset_path,'') + title + exts)
                    counter += 1
else:
    print(args.dataset, 'folder does not exist')


random.shuffle(dataset_list)

train_percent = 100 - args.test - args.valid
test_percent = args.test
valid_percent = args.valid

train_index = int(len(dataset_list)*(train_percent)/100)
test_index = int(len(dataset_list)*(test_percent)/100)
valid_index = int(len(dataset_list)*(valid_percent)/100)
total = train_index + test_index + valid_index


train_data = dataset_list[:train_index]

test_data = dataset_list[train_index:train_index+test_index]

valid_data = dataset_list[-valid_index:]

#for data in dataset_list:
    #dataset_file.write(data + "\n")

for train in train_data:
    train_file.write(train + "\n")

for test in test_data:
    test_file.write(test + "\n")
    
for valid in valid_data:
    valid_file.write(valid + "\n")


print(train_index,test_index,valid_index)

print("Total Files: {0} \nTotal Train: {1} ({2}%)\nTotal Test: {3} ({4}% \nTotal Valid: {5} ({6}%)".
      format(total,train_index, train_percent, test_index, test_percent,valid_index,valid_percent))
