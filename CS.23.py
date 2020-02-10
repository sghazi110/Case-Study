import PIL.Image
im=PIL.Image.open('cs_22.png')
#im.show()
im2=PIL.Image.open('abc.jpg')
im2.paste(im,(80,210,230,360))
im2.show()
im2.save('cs_23.jpg')
