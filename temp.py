import math
import numpy as np
from PIL import Image, ImageDraw

min_num_vertex = 4
max_num_vertex = 12

mean_angle = 2 * math.pi / 5
angle_range = 2 * math.pi / 15

min_width = 12
max_width = 40

mask = Image.open('Places365_test_00025207.jpg')
W, H = mask.size
mask_save = Image.new('L', (W, H), 0)
average_radius = math.sqrt(H * H + W * W) / 8

for _ in range(np.random.randint(1, 4)):
    num_vertex = np.random.randint(min_num_vertex, max_num_vertex)
    angle_min = mean_angle - np.random.uniform(0, angle_range)
    angle_max = mean_angle + np.random.uniform(0, angle_range)
    angles = []
    vertex = []

    for i in range(num_vertex):
        if i % 2 == 0:
            angles.append(2 * math.pi - np.random.uniform(angle_min, angle_max))
        else:
            angles.append(np.random.uniform(angle_min, angle_max))

    vertex.append((int(np.random.randint(0, W)), int(np.random.randint(0, H))))

    for i in range(num_vertex):
        r = np.clip(np.random.normal(loc=average_radius, scale=average_radius // 2), 0, 2 * average_radius)
        new_x = np.clip(vertex[-1][0] + r * math.cos(angles[i]), 0, W)
        new_y = np.clip(vertex[-1][1] + r * math.sin(angles[i]), 0, H)
        vertex.append((int(new_x), int(new_y)))

    draw = ImageDraw.Draw(mask)
    draw_save = ImageDraw.Draw(mask_save)
    width = int(np.random.uniform(min_width, max_width))
    draw.line(vertex, fill=(255, 255, 255), width=width)
    draw_save.line(vertex, fill=255, width=width)

    for v in vertex:
        draw.ellipse((v[0] - width // 2, v[1] - width // 2, v[0] + width // 2, v[1] + width // 2), fill=(255, 255, 255))
        draw_save.ellipse((v[0] - width // 2, v[1] - width // 2, v[0] + width // 2, v[1] + width // 2), fill=255)

if np.random.normal() > 0:
    mask.transpose(Image.FLIP_LEFT_RIGHT)
if np.random.normal() > 0:
    mask.transpose(Image.FLIP_TOP_BOTTOM)

mask_image_name = './fuck.png'
mask.save(mask_image_name)
mask_save.save('./fuck_mask.png')
'''
mask = np.asarray(mask, np.float32)
mask = np.reshape(mask, (H, W, 1))'''
