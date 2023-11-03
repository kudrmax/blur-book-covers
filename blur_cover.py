from PIL import Image, ImageFilter
import glob
from pathlib import Path

##### ИЗМЕНЯТЬ ЭТО #####
blur_ratio = 20  # коэффициент размытия
output_image_proportions = 16, 9 # пропорции итогового изображение
input_image_directory = './images/'  # путь к существующей (!) папке с исходными изображениями
output_image_directory = './images/output/'  # путь к существующей (!) папке с заблюренными изображениями, который отличается от input_image_directory (!)

##### АЛГОРИТМ #####
for extension in ['jpg', 'jpeg', 'png']:
    for in_name in glob.glob(input_image_directory + '*.' + extension):
        in_image = Image.open(in_name)  # исходная картинка
        blured_image = in_image.filter(ImageFilter.GaussianBlur(blur_ratio))  # блюрим картинку

        in_width, in_height = in_image.size  # размеры исходной картинки
        out_height, out_width = in_height, int(output_image_proportions[0] * in_height / output_image_proportions[1])  # размеры того, что должно у нас получится на выходе

        multiplier = out_width / in_width  # коэфициент растяжения заблюренной картинки до итоговой картинки
        new_size = (int(blured_image.size[0] * multiplier), int(blured_image.size[1] * multiplier))  # растягиваем
        blured_image = blured_image.resize(new_size)  # растягиваем

        out_image = Image.new('RGB', (out_width, out_height))  # пустое итоговое изображение
        out_image.paste(blured_image, (0, int(- blured_image.size[0] / 2)))  # вставляем заблюренную картинку в итоговую
        out_image.paste(in_image, (int(out_width / 2 - in_width / 2), 0))  # вставляем оригинальную картинку в итоговую

        out_image.save(output_image_directory + Path(in_name).stem + '_blured.jpg')  # сохраняем итоговое изображение
