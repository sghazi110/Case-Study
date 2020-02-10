import PIL.Image
im=PIL.Image.open('xyz.gif')
cropped=im.crop((150,150,300,300))
cropped.show()
cropped.save('cs_22.png')
