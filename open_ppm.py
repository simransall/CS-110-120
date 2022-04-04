from graphics import graphics
import os

# Change the string to the file directory where your image is if it isn't in the default (mu_code)
# Don't forget to use \\ not just \!
os.chdir('C:\\Users\\your_name\\mu_code\\sub_folder')

# Totally not-borrowed code...
def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def main():
    file_name = input('Enter name of PPM file:\n')
    SF = SCALE_FACTOR = float(input('Enter scale factor:\n'))

    image = load_image_pixels(file_name)
    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    gui = graphics(width*SF, height*SF, file_name)

    y = 0
    for row in image:
        x = 0
        for pixel in row:
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            color = gui.get_color_string(r, g, b)
            gui.rectangle(x*SF, y*SF, 1*SF, 1*SF, color)
            x += 1
        y += 1
main()