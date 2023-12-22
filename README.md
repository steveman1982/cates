Note: I gobbled this together in a hurry, do not take inspiration here for any coding standard.

# cates
Detect cats on a raspberry pi using motion and YOLOV8

Or detect one of the other categories available in the pre-trained model.

In my case I'm interested in cats, one particular friendly cat to be exact :)
However, the default model (even the largest one) tends to detect cats as a one of ['cat', 'dog', 'bear'].
Transfer learning and training on my own samples may be a followup step.


Motion provides the option to get the center x and y positions, and the width and height of the detections. 
I try to use this to direct the YOLO model to a region of interest, creating a snippet of 640x380 pixels.
Without this step YOLO would resize the 1920x1080 image to 640x380, which is a rather significant loss of resolution.

In my setup there are actually two raspberry pis involved, a model 4b with the camera, and a model 5 running the detections. It should be well possible to run all this on a single rpi. 

And because I want to know when to step into the garden and pet my favourite cat, I added a telegram notification message, including the image in which a cat (dog, bear...) was supposedly found.


Things to keep in mind:

-if you want to repell cats from your property, please make sure you don't harm the little fellas.
-replace any <...> placeholders with your specific situation. Things like image folders, urls, tokens.
-if you notice a lot of stored images without any cats, play around with the motion threshold, and the number of frames that need to contain motion in the motion.conf file.
-you may want to remove stored images
-if in your set up cats tend to go undetected by the YOLO model, try a larger one n, s, m, l, x are the defaults. It's also possible to train a model yourself, but you'll probably need several hundreds of samples.
There are great instruction videos on this online.
-using docker is optional
-using telegram is optional
-come to think of it: this is all very much optional
