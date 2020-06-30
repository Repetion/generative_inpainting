import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, help='The name of dataset')
parser.add_argument('--data_type', default='train', type=str, help='The type of data (train or validation or test)')
parser.add_argument('--image_path', type=str, help='The path of image folder')
parser.add_argument('--flist_path', default='/home/jisukim/generative_inpainting/flist' ,type=str, help='The path of flist')

if __name__ == "__main__":
    args = parser.parse_args()
    
    image_names = []
        
    for dirname, dirnames, filenames in os.walk(args.image_path):
        for filename in filenames:
            image_names.append(os.path.join(dirname, filename))

    assert args.data_type == 'train' or 'validation' or 'test'

    if args.data_type == 'train':
        result = args.flist_path + '/train_' + args.dataset_name + '.flist'
    elif args.data_type == 'validation':
        result = args.flist_path + '/validation_' + args.dataset_name + '.flist'
    else:
        result = args.flist_path + '/test_' + args.dataset_name + '.flist'

    f = open(result, 'w')
    f.write('\n'.join(image_names))
    f.close()