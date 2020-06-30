import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, help='The name of dataset')
parser.add_argument('--test_path', type=str, help='The path of test dataset')
parser.add_argument('--log_dir', type=str, help='The path of model log')

if __name__ == "__main__":
    args = parser.parse_args()

    image_items = []
    matching_items = []
    output_items = []
    result = []

    for dirname, dirnames, filenames in os.walk(args.test_path):
        for filename in filenames:
            image_items.append(os.path.join(dirname, filename))
            output_items.append(filename)

    matching_path = '/home/jisukim/generative_inpainting/flist/' + 'mask_matching_' + args.dataset_name + '.flist'

    f = open(matching_path, 'r')
    matching_items = f.read().splitlines()
    f.close()

    index = 0

    for image_item in image_items:
        path = 'python test.py --image ' + image_items[index] + ' --mask ' + matching_items[index] + ' --output ./output_' + output_items[index] + ' ' + '--checkpoint ' + args.log_dir
        result.append(path)

        index += 1
    
    output = './flist/test_argument_list/test_list_' + args.dataset_name + '.flist'
    f = open(output, 'w')
    f.write('\n'.join(result))
    f.close()