import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, help='The name of dataset')
parser.add_argument('--image_path', type=str, help='The train path')
parser.add_argument('--flist_path', default='/home/jisukim/generative_inpainting/train_flist' ,type=str, )

if __name__ == "__main__":
    args = parser.parse_args()

    image_items = os.listdir(args.image_path)
    train_names = []
    validation_names = []

    train_num = int(len(image_items) * 0.7)

    count = 0

    for count in range(train_num):
        train_item = args.image_path + '/' + str(image_items[count])
        train_names.append(train_item)

        count += 1
    
    for count in range(train_num, len(image_items)):
        validation_item = args.image_path + '/' + str(image_items[count])
        validation_names.append(validation_item)

        count += 1

    train = args.flist_path + '/train_' + args.dataset_name + '.flist'
    f = open(train, 'w')
    f.write('\n'.join(train_names))
    f.close()

    validation = args.flist_path + '/validation_' + args.dataset_name + '.flist'
    f = open(validation, 'w')
    f.write('\n'.join(validation_names))
    f.close()