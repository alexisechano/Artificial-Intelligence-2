# K Means image clustering lab
# Alexis Echano, KIM P7

from PIL import Image

import urllib.request, io, sys, math, random

def load_image_URL(url):
    f = io.BytesIO(urllib.request.urlopen(url).read())
    img = Image.open(f)
    return img

def load_image_file(filename):
    return Image.open(filename)

def find_means(k, size, pix):   #size is a tuple
    means = []

    for i in range(k):
        means.append(pix[random.randint(0, size[0]), random.randint(0, size[1])])

    return means #returns lists of pixels in each mean cluster

def determine_mean(group, pix):   #list, old means
    lengths = len(group)
    totals = [0, 0, 0]    #R,G,B

    for pixel in group:
        totals[0] += pixel[0]
        totals[1] += pixel[1]
        totals[2] += pixel[2]

    avg_RGB = (totals[0] / lengths, totals[1] / lengths, totals[2] / lengths)
    return avg_RGB

def update_means(groupings, pix, diff, means):    #find new means according to the groupings
    new_means = []
    i = 0

    for thing in groupings:
        if diff[i] != 0 and len(thing) != 0:
            new_mean = determine_mean(thing, pix)
            new_means.append(new_mean)
        else:
            new_means.append(means[i])
        i += 1

    return new_means    #RGB means

def pregrouping(size, pix):  #sets up color dictionary
    colored = {}
    for x in range(size[0]):
        for y in range(size[1]):
            current = pix[x,y]
            if current not in colored:
                colored[current] = [(x,y)]
            else:
                colored[current].append((x, y))

    return colored

def grouping(means, size, pix, dict): #diff are the num of pixels jumping/entering
    #finds the RGB vals of the certain mean pixel
    rgb_means = means
    groups = []     #key is the mean RGB VALUE, value is a list of the pixels (x,y)
    pixel_vals = []

    for rgb in rgb_means:
        groups.append([])       #plain blank list for initiation
        pixel_vals.append([])   #plain blank list for initiation

    for color in dict.keys():
        differences = []
        for m in rgb_means:
            differences.append(find_distance(m, color, pix))

        diff = min(differences)
        ind = differences.index(diff)

        for x, y in dict[color]:
            groups[ind].append(pix[x, y])         # postion values, not colors
            pixel_vals[ind].append((x, y))

    return groups, rgb_means, means, pixel_vals  #if done group diff = [0,0,0,0]

def find_distance(mean_color, curr_color, pix):     #pixel is just x,y...you need to find RGB in here

    red_dist = (mean_color[0] - curr_color[0])**2
    green_dist = (mean_color[1] - curr_color[1])**2
    blue_dist = (mean_color[2] - curr_color[2])**2

    total = red_dist + green_dist + blue_dist
    return math.sqrt(total)

def find_most_common(pix, size):
    colors = {}

    for x in range(size[0]):
        for y in range(size[1]):
            current_color = pix[x, y]
            if current_color not in colors: colors[current_color] = 1
            else: colors[current_color] += 1

    max_count = 0
    max_value = (0, 0, 0)

    for value in colors.keys():
        count = colors[value]
        if max_count <= count:
            max_count = count
            max_value = value

    return max_value, max_count #returns most recurring pixel

def check_done(k, diff):
    check = [0] * k
    if diff == check:
        return True
    return False

def distinct_pixels(pix, size):
    used = set()
    counter = 0

    for x in range(size[0]):
        for y in range(size[1]):
            current_color = pix[x, y]
            if current_color not in used: counter += 1
            used.add(current_color)

    return counter  #returns  number of distinct pixels

def update_diffs(old_groups, new_groups): #lengths
    newD = []
    for i in range(len(new_groups)):
        length = len(new_groups[i])
        old_len = len(old_groups[i])
        newD.append(old_len - length)

    return newD

def init_diff(k):
    creation = []
    for i in range(k):
        creation.append([0])
    return creation

def classify_points(pixles, means):
    new_points = {}

    for k in range(len(pixles)):
        point_list = pixles[k]
        for p in point_list:
            new_points[p] = (int(means[k][0]), int(means[k][1]), int(means[k][2]))    #color
    return new_points

def add_directions(x,y, size, done):
    new_region = set()
    new_region.add((x, y - 1))
    new_region.add((x - 1, y - 1))
    new_region.add((x + 1, y - 1))
    new_region.add((x, y + 1))
    new_region.add((x - 1, y + 1))
    new_region.add((x + 1, y + 1))
    new_region.add((x - 1, y))
    new_region.add((x + 1, y))
    return new_region

def regions(pix, size, means):
    visited = {}
    region_counts = {}

    for mean in means:
        region_counts[(int(mean[0]), int(mean[1]), int(mean[2]))] = 0
    for x in range(size[0]):
        for y in range(size[1]):
            if (x,y) not in visited:
                new_region = {(x,y)}
                current = pix[x,y]
                while (new_region):
                    popped = new_region.pop()
                    x1, y1 = popped[0], popped[1]
                    if x1>=0 and x1<size[0] and y1>=0 and y1<size[1] and pix[x1, y1] == current and popped not in visited:
                        sub_region = add_directions(popped[0], popped[1], size, visited)
                        for s in sub_region:
                            new_region.add(s)
                        visited[(x1, y1)] = 0
                region_counts[current] += 1

    regionCt = []
    for r in region_counts:
        regionCt.append(region_counts[r])
    return str(regionCt)

def main():
    args = sys.argv[1:]
    k_val = int(args[0])    #how many clusters in the image to be inputted
    input_text = str(args[1])

    if "https" in input_text:
        curr_img = load_image_URL(input_text)
    else:
        curr_img = load_image_file(input_text)

    pic = curr_img.load()   #the actual picture so pixel retrieval is good
    the_size = curr_img.size
    pixel_ct = the_size[0]*the_size[1]
    the_means = find_means(k_val, the_size, pic)    #returns list of tuples

    print("Size:", the_size[0], "x", the_size[1])
    print("Pixels:", pixel_ct)
    print("Distinct pixel count:", distinct_pixels(pic, the_size))
    comm = find_most_common(pic, the_size)
    print("Most common pixel:", comm[0], "=>", comm[1])

    sffid = init_diff(k_val)
    color_dict = pregrouping(the_size, pic) #returns dictionary
    find_differences = []
    groupings, rgb_ms, the_means, pix_coords = grouping(the_means, the_size, pic, color_dict)  # USE RGB_MS
    diffs = update_diffs(sffid, groupings)
    find_differences.append(diffs)

    while not check_done(k_val, diffs):
        sffid = groupings
        new_meens = update_means(groupings, pic, diffs, rgb_ms)
        groupings, rgb_ms, the_means, pix_coords = grouping(new_meens, the_size, pic, color_dict)  # USE RGB_MS
        diffs = update_diffs(sffid, groupings)
        find_differences.append(diffs)

    points = classify_points(pix_coords, the_means)
    print("Differences:")
    for d in find_differences:
        print(d)
    print("Final means:")

    for meen in range(len(the_means)):
        print(meen + 1, ":", the_means[meen], "=>", len(groupings[meen]))

    for x in range(the_size[0]):
        for y in range(the_size[1]):
            pic[x,y] = points[x,y]

    print("Region counts:", regions(pic, the_size, the_means))
    #curr_img.show()
    curr_img.save("kmeans/{}.png".format('2020aechano'), "PNG")

main()