from PIL import Image
import control_panel
import numpy as np
import os
from os import listdir
from os.path import isfile, join

size = control_panel.image_size
p = control_panel.image_pixels # number of features (pixels) in each image
X = np.zeros(shape=(1, p))  # initialise image matrix with zeros in one row


def get_thumbs(File_Path, Out_Path):
    photos = [f for f in listdir(File_Path) if isfile(join(File_Path, f))]
    for infile in photos:
        outfile = os.path.splitext(infile)[0]
        if infile != outfile:
            try:
                img = Image.open(File_Path + infile).convert("L")  # convert image to greyscale
                img = img.resize(size)  # resize image
                img.save(Out_Path + outfile + ".png", "PNG") # save as new image in the Processed folder
                a = np.asarray(img).reshape(-1) # reshape each matrix of image's pixel alpha values to a vector
                global X
                X = np.vstack([X,a])    # add vector of each image's pixel alpha values to new row of Image matrix

            except IOError as e:
                print("cannot create thumbnail for" +e, infile)


def test_thumbs(File_Path, Out_Path):
    photos = [f for f in listdir(File_Path) if isfile(join(File_Path, f))]
    for infile in photos:
        outfile = os.path.splitext(infile)[0]
        if infile != outfile:
            try:
                img = Image.open(File_Path + infile).convert("L")  # convert image to greyscale
                img = img.resize(size)  # resize image
                img.save(Out_Path + outfile + ".png", "PNG") # save as new image in the Processed folder

            except IOError as e:
                print("cannot create thumbnail for" +e, infile)


get_thumbs("Data/Raw_Bex/", "Data/Processed/")
X = np.delete(X, (0), axis=0)   # delete the first row of Image matrix (the zeros row)
n = X.shape[0]

get_thumbs("Data/Raw_Peet/", "Data/Processed/")
m = (X.shape[0]) - n

bex = np.ones((n,1), dtype=np.int)   # create vector to append to front of image matrix, to label who is in photo (1 = bex)
peet = np.zeros((m,1), dtype=np.int)   # create vector to append to front of image matrix, to label who is in photo (0 = peet)

x = np.vstack([bex, peet])
X = np.hstack([x, X])
np.save('Data/image_data', X)  # save newly created image matrix to a data file, so can import to neural net


# Creates thumbnails of Test Images
test_thumbs("Data/Test_Images/", "Data/Processed_Test/")
