import sys
from PIL import Image, ImageFilter

input_image = Image.open('input.jpeg')
blur_image = input_image.filter(ImageFilter.GaussianBlur(5))

# blur_image.save('output.jpg')

# images = [Image.open(x) for x in ['input.jpeg', 'output.jpg']]
input_width, input_height = list(input_image.size)

output_height = int(input_height)
output_width = int(16 * output_height / 9)

output_image = Image.new('RGB', (output_width, output_height))

multiplier = output_width / input_width
new_size = (int(blur_image.size[0] * multiplier), int(blur_image.size[1] * multiplier))
output_image.paste(blur_image.resize(new_size), (0, -500))
# output_image.paste(blur_image_resized, (int(output_width / 2), 0))
output_image.paste(input_image, (int(output_width / 2 - input_width / 2), 0))

# x_offset = 0
# for im in images:
#     new_im.paste(im, (300, 0))
#     x_offset += im.size[0]

output_image.save('merged.jpg')
