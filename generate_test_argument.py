import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, help='The name of dataset')
parser.add_argument('--test_path', type=str, help='The path of test dataset')
parser.add_argument('--log_dir', type=str, help='The path of model log')

if __name__ == "__main__":
    args = parser.parse_args()

    image_names = []
    image_paths = []
    match_masks = []
    test_arguments = []

    image_names_path = '/home/jisukim/generative_inpainting/flist/' + args.dataset_name + '/image_names_' + args.dataset_name + '.flist'
    f = open(image_names_path, 'r')
    image_names = f.read().splitlines()
    f.close()
    
    image_paths_path = '/home/jisukim/generative_inpainting/flist/' + args.dataset_name + '/image_paths_' + args.dataset_name + '.flist'
    f = open(image_paths_path, 'r')
    image_paths = f.read().splitlines()
    f.close()
    
    match_masks_path = '/home/jisukim/generative_inpainting/flist/' + args.dataset_name + '/match_masks_' + args.dataset_name + '.flist'
    f = open(match_masks_path, 'r')
    match_masks = f.read().splitlines()
    f.close()

    for image_name, image_path, match_mask in zip(image_names, image_paths, match_masks):
        test_argument = 'python test.py --image ' + args.test_path + '/masked_' + image_name + ' --mask ' + match_mask + ' --output /home/jisukim/generative_inpainting/test_output/' + args.dataset_name + '/' + image_name + ' ' + '--checkpoint_dir ' + args.log_dir
        test_arguments.append(test_argument)

    test_arguments_path = './flist/' + args.dataset_name + '/test_arguments_' + args.dataset_name + '.flist'
    f = open(test_arguments_path, 'w')
    f.write('\n'.join(test_arguments))
    f.close()