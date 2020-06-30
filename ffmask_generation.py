import math
import numpy as np
from PIL import Image, ImageDraw

min_num_vertex = 2
max_num_vertex = 8
mean_angle = 2 * math.pi / 5
angle_range = 2 * math.pi / 15
min_width = 12
max_width = 24
average_radius = math.sqrt(256 * 256 + 256 * 256) / 8

for epoch in range(5000):
    mask = Image.new('1', (256, 256), 0)

    for _ in range(np.random.randint(1, 4)):
        num_vertex = np.random.randint(min_num_vertex, max_num_vertex)
        angle_min = mean_angle - np.random.uniform(0, angle_range)
        angle_max = mean_angle + np.random.uniform(0, angle_range)
        angles = []
        vertex = []

        for i in range(num_vertex):
            if i % 2 == 0:
                angles.append(
                    2 * math.pi - np.random.uniform(angle_min, angle_max))
            else:
                angles.append(np.random.uniform(angle_min, angle_max))

        vertex.append((int(np.random.randint(0, 256)), int(np.random.randint(0, 256))))

        for i in range(num_vertex):
            r = np.clip(np.random.normal(loc=average_radius, scale=average_radius // 2), 0, 2 * average_radius)
            new_x = np.clip(vertex[-1][0] + r * math.cos(angles[i]), 0, 256)
            new_y = np.clip(vertex[-1][1] + r * math.sin(angles[i]), 0, 256)
            vertex.append((int(new_x), int(new_y)))

        draw = ImageDraw.Draw(mask)
        width = int(np.random.uniform(min_width, max_width))
        draw.line(vertex, fill=255, width=width)

        for v in vertex:
            draw.ellipse((v[0] - width // 2, v[1] - width // 2, v[0] + width // 2, v[1] + width // 2), fill=255)

    if np.random.normal() > 0:
        mask.transpose(Image.FLIP_LEFT_RIGHT)
    if np.random.normal() > 0:
        mask.transpose(Image.FLIP_TOP_BOTTOM)

    mask_name = '/home/dataset/freeform_mask/' + 'mask' + str(epoch + 1) + '.png'
    mask.save(mask_name)