import PIL.Image
import PIL.ImageFilter
def warhol(pic):
    photo=PIL.Image.open(pic)
    width, height = photo.size    
    res = PIL.Image.new(photo.mode, (2*width, 2*height))
    res.paste(photo, (0, 0, width, height))
    contour = photo.filter(PIL.ImageFilter.CONTOUR)
    res.paste(contour, (width, 0, 2*width, height))
    emboss = photo.filter(PIL.ImageFilter.EMBOSS)
    res.paste(emboss, (0, height, width, 2*height))
    edges = photo.filter(PIL.ImageFilter.FIND_EDGES)
    res.paste(edges, (width, height, 2*width, 2*height))
    res.show()
warhol('abcd.jpg')
