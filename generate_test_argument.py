import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, help='The name of dataset')
parser.add_argument('--log_dir', type=str, help='The path of model log')

if __name__ == "__main__":
    args = parser.parse_args()

    path = '/home/jisukim/generative_inpainting/test_data/flist/'
    flist = path + args.dataset_name + '.flist'
    matching = path + 'mask_matching_' + args.dataset_name + '.flist'

    flist_items = []
    matching_items = []
    result = []

    f = open(flist, 'r')
    flist_items = f.read().splitlines()
    f.close()

    f = open(matching, 'r')
    matching_items = f.read().splitlines()
    f.close()

    index = 0

    for flist_item in flist_items:
        path = 'python test.py --image ' + flist_items[index] + ' --mask ' + matching_items[index] + ' --output ./output.png ' + '--checkpoint ' + args.log_dir
        result.append(path)

        index += 1
    
    output = './test_argument_list/test_list_' + args.dataset_name + '.txt'
    f = open(output, 'w')
    f.write('\n'.join(result))
    f.close()