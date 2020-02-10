import PIL.Image
im=PIL.Image.open('abcd.jpg')
print(f'the size of the picture is:{im.size}')
print(f'the format of the picture is: {im.format}')
print(f'the mode of the picture is: {im.mode}')
