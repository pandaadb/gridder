from PIL import Image, ImageDraw, ImageOps, ImageFont
import argparse

def main(in_file):
    border_size = 100

    image = Image.open(in_file)

    width,height = image.size

    basewidth = 500
    wpercent = (basewidth/float(width))
    hsize = int((float(height)*float(wpercent)))
    image = image.resize((basewidth,hsize), Image.ANTIALIAS)

    width,height = image.size

    image = ImageOps.expand(image,border=100,fill='white')
    width,height = image.size

    font = ImageFont.truetype("arial.ttf", 24)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height

    longer = width if width > height else height

    step_size = int(longer / 10)

    counter = 1
    for x in range(border_size, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill='white', width=2)
        if x + step_size / 2 < image.width - border_size:
            draw.text( (x + step_size / 2, y_start + 50), str(counter), (0,0,0), font = font)
            counter = counter + 1

    x_start = 0
    x_end = image.width

    counter = 1

    for y in range(border_size, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill='white', width = 2)
        if y + step_size / 2 < image.height - border_size:
            draw.text( (x_start + 50, y + step_size / 2), str(counter), (0,0,0), font = font)
            counter = counter + 1

    del draw

    image = ImageOps.grayscale(image)

    # threshold = 60
    # image = image.point(lambda p: p > threshold and 255)

    image.show()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Gridder draws a numbered grid..')
    parser.add_argument('-i','--input', help='Input file', required=True)
    
    args = vars(parser.parse_args())
    
    main(args['input'])