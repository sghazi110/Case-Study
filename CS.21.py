import PIL.Image
def convert(file):
    im=PIL.Image.open(file)
    cropped=im.crop((200,200,500,500))
    cropped.show()
    cropped.save('cs_21.gif')
convert('abcd.jpg')
