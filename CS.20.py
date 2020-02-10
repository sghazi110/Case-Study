import PIL.Image
def resize(x,y):
    photo=PIL.Image.open('abcd.jpg')
    img=photo.resize((x,y))
    print(img.show())
    print(img.size)

resize(500,500)
