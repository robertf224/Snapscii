from PIL import Image

 
ascii = list('`\'..-,:\"_!~/\\;*|^<+7r?v=iJLlYc)T{(}tsIVCxF325]1[uU4nzAXjfoZSyPweaKEHkGOh0M$N9#dq6RmDW%bpQ8Bg@&')
 

def itoa(filename, columns=None, lines=None):

    im=Image.open(filename)
    #width=im.size[0]/8*8
    #height=im.size[1]/13*13
    if not columns or not lines:
        columns = im.size[0]/8
        lines = im.size[1]/13
    im=im.resize((columns*8, lines*13), Image.ANTIALIAS)
    im=im.convert('L')
     

    # build box intensities to be averaged later
    box_intensities = [[0 for i in xrange(columns)] for n in xrange(lines)]
    for y in xrange(lines*13):
        for x in xrange(columns*8):
            lum = im.getpixel((x,y))
            box_intensities[y/13][x/8] += lum
            

    # build string from average intensities
    string = ''
    for row in box_intensities:
        for intensity in row:
            char = ascii[int(round( (float(intensity)/(13*8)) / (float(255)/len(ascii)) ))-1]
            string += char
        string += '\n'
    
    return string