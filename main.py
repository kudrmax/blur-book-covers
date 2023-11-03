from PIL import Image, ImageFilter

in_image = Image.open('input.jpeg')  # исходная картинка
blur_image = in_image.filter(ImageFilter.GaussianBlur(10))  # блюрим картинку

in_width, in_height = in_image.size  # размеры исходной картинки
out_height, out_width = in_height, int(16 * in_height / 9)  # размеры того, что должно у нас получится на выходе

multiplier = out_width / in_width  # коэфициент растяжения заблюренной картинки до итоговой картинки
new_size = (int(blur_image.size[0] * multiplier), int(blur_image.size[1] * multiplier))  # растягиваем
blur_image = blur_image.resize(new_size)  # растягиваем

out_image = Image.new('RGB', (out_width, out_height))  # пустое итоговое изображение
out_image.paste(blur_image, (0, int(- blur_image.size[0] / 2)))  # вставляем заблюренную картинку в итоговую
out_image.paste(in_image, (int(out_width / 2 - in_width / 2), 0))  # вставляем оригинальную картинку в итоговую

out_image.save('merged.jpg')  # сохраняем итоговое изображение
