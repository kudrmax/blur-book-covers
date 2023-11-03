import sys
from PIL import Image, ImageFilter

OriImage = Image.open('input.jpeg')
gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
# OriImage.show()
# gaussImage.show()

gaussImage.save('output.jpg')

images = [Image.open(x) for x in ['input.jpeg', 'output.jpg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

cover_width = 1920
cover_height = 1080

new_im = Image.new('RGB', (cover_width, cover_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('merged.jpg')