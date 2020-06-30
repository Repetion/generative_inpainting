import argparse
import os
import cv2
import random

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, help='The name of dataset')

if __name__ == "__main__":
    args = parser.parse_args()

    test_images = []
    match_masks = []

    test_image_path = '/home/jisukim/generative_inpainting/flist/test_' + args.dataset_name + '.flist'
    f = open(test_image_path, 'r')
    test_images = f.read().splitlines()
    f.close()

    count = 1

    for test_image in test_images:
        rmask_num = random.randint(1, 5000) # Number of masks : 10000
        mask_name = '/home/dataset/freeform_mask/mask' + str(rmask_num) + '.png'
        match_masks.append(mask_name)
        
        image = cv2.imread(test_image)
        mask = cv2.imread(mask_name)

        height, width, channel = image.shape
        mask = cv2.resize(mask, dsize=(width, height), interpolation=cv2.INTER_LINEAR)
        result = cv2.bitwise_not(cv2.bitwise_and(cv2.bitwise_not(image), cv2.bitwise_not(mask)))

        result_path = '/home/dataset/' + args.dataset_name + '/test_masked/test' + str(count) + '.png'

        cv2.imwrite(result_path, result)

        print(str(count) + ' : ' + test_image + ' / ' + str(mask_name) + '\n=>' + result_path)

        count += 1
    
    mask_matching_path = '/home/jisukim/generative_inpainting/test_data/flist/mask_matching_' + args.dataset_name + '.flist'
    f = open('./match_masks_list.flist', 'w')
    f.write('\n'.join(match_masks))
    f.close()
