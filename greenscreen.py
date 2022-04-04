###
### Author: Simran Sall
### Course: CSc 110
### Description: This program takes two image files and overlays them. One image
###              file that is inputted is the greenscreen file and will be overlapping
###              the fill image, which is the background image. The contents of the file
###              are evaluated, specifically the r, g, and b values, and those are
###              compared among each file. Whichever color value is brighter is the one
###              that will be replaced with in the new file.
###

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file .readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name, pixels):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    image_file = open(file_name, 'r')
    # iterate through the file
    image_file.readline()
    image_file.readline()
    image_file.readline()

    # get the width and height of the file
    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    # append r, g, b values to a list
    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)
    return pixels

def greenscreen(pixel_gs, pixel_fi, channel, channel_diff, replace_color, replace_color_list):
    ''' This function implements the algorithm for determining the overlay of the images.
    It takes the input of the user (if the user wants to evaluate red, blue, or green), and
    compares the r/g/b values between the two files. The color that is determined will
    be added to the new ppm file.
    pixel_gs: list of pixels of the greenscreen image
    pixel_fi: list of pixels of the fill image
    channel: the user inputs if they want r, g, or b.
    channel_diff: the user inputs a float between 1.0 and 10.0
    replace_color: empty string that will be replaced with the actual value once determined
        by this algorithm
    replace_color_list: list that the color values will be appended to.
    '''
    # cast the string input of channel difference to a float so it can be used to compare
    channel_diff = float(channel_diff)
    # go through the rows of the list
    for i in range(len(pixel_gs)):
        # go through the columns of the list
        for j in range(len(pixel_gs[i])):
            # evaluate numbers based on if the user inputs r, g, or b
            if channel == 'r':
                # determine if pixel in the new image should be the one from the\
                # green screen file or the fill image file
                if pixel_gs[i][j][0] > (pixel_gs[i][j][1] * channel_diff) \
                and pixel_gs[i][j][0] > (pixel_gs[i][j][2] * channel_diff):
                    replace_color = pixel_fi[i][j][0], pixel_fi[i][j][1], pixel_fi[i][j][2]
                    replace_color_list.append(replace_color)
                else:
                    replace_color = pixel_gs[i][j][0], pixel_gs[i][j][1], pixel_gs[i][j][2]
                    replace_color_list.append(replace_color)
            elif channel == 'g':
                # determine if pixel in the new image should be the one from the\
                # green screen file or the fill image file
                if pixel_gs[i][j][1] > (pixel_gs[i][j][0] * channel_diff) \
                and pixel_gs[i][j][1] > (pixel_gs[i][j][2] * channel_diff):
                    replace_color = pixel_fi[i][j][0], pixel_fi[i][j][1], pixel_fi[i][j][2]
                    replace_color_list.append(replace_color)
                else:
                    replace_color = pixel_gs[i][j][0], pixel_gs[i][j][1], pixel_gs[i][j][2]
                    replace_color_list.append(replace_color)
            elif channel == 'b':
                # determine if pixel in the new image should be the one from the\
                # green screen file or the fill image file
                if pixel_gs[i][j][2] > (pixel_gs[i][j][0] * channel_diff) \
                and pixel_gs[i][j][2] > (pixel_gs[i][j][1] * channel_diff):
                    replace_color = pixel_fi[i][j][0], pixel_fi[i][j][1], pixel_fi[i][j][2]
                    replace_color_list.append(replace_color)
                else:
                    replace_color = pixel_gs[i][j][0], pixel_gs[i][j][1], pixel_gs[i][j][2]
                    replace_color_list.append(replace_color)
    return replace_color_list

def write_to_file(out_file, replace_color_list, gs_file):
    ''' This function takes the color values that were determined in the
    greenscreen algorithm and appends them to the new file that represents
    the new image.
    out_file: the output file that all of the new contents will be written to
    replace_color_list: the list of all of the new rgb pixel values
    gs_file: the greenscreen file that is used to get the width and height dimensions
    '''
    # open up the output file and write to it
    output_file = open(out_file, 'w')
    # add the format for the ppm file
    output_file.write('P3\n')
    # add the width and height for the ppm file
    dimensions = get_image_dimensions_string(gs_file)
    output_file.write(str(dimensions)+ '\n')
    int_dimensions = dimensions.split(' ')
    width = int(int_dimensions[0])
    # add the max brightness for the ppm file
    output_file.write('255\n')
    count = 0
    # add the rgb pixel values for the ppm file
    for rgb_value in replace_color_list:
        output_file.write(str(rgb_value[0]) + ' ' + str(rgb_value[1]) + ' ' + str(rgb_value[2]) + ' ')
        count += 1
        if count == width:
            output_file.write('\n')
            count = 0

def main():
    pixels = []
    replace_color = ' '
    replace_color_list = []
    pixel_gs = []
    pixel_fi = []

    channel = input('Enter color channel\n')
    if channel != 'r' and channel != 'g' and channel != 'b':
        print('Channel must be r, g, or b. Will exit.')
        exit()

    channel_diff = input('Enter color channel difference\n')
    if float(channel_diff) < 1.0 or float(channel_diff) > 10.0:
        print('Invalid channel difference. Will exit.')
        exit()

    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    get_image_dimensions_string(gs_file)
    get_image_dimensions_string(fi_file)
    if get_image_dimensions_string(gs_file) != get_image_dimensions_string(fi_file):
        print('Images not the same size. Will exit.')
        exit()

    out_file = input('Enter output file name\n')
    print('Output file written. Exiting.')

    load_image_pixels(gs_file, pixel_gs)
    load_image_pixels(fi_file, pixel_fi)
    greenscreen(pixel_gs, pixel_fi, channel, channel_diff, replace_color, replace_color_list)
    write_to_file(out_file, replace_color_list, gs_file)

main()