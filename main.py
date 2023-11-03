from PIL import Image, ImageFilter

OriImage = Image.open('input.jpeg')
gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
# OriImage.show()
# gaussImage.show()

gaussImage.save('output.jpg')
