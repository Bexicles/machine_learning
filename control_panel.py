image_size = (28, 28)
image_pixels = image_size[0] * image_size[1]

training_split = 0.75   # proportion of original data set, set aside for training the model

alpha = 0.001 # learning rate
solutions_number = 2   # no. of possible answers is two (me or peet; 0 or 1)
batch_size = 50