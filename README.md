# Air Canvas
 
# VP
 
Ever wanted to draw your imagination by just waving your finger in the air. The project titled “Air Canvas” is a desktop application allowing the user to draw doodles,  numbers, shapes, and various objects out of thin air.
Air Canvas project incorporates real-time video tracking of the pointer(bead),which the user moves throughout the canvas by pointing a specific and pre-defined object in front of their webcam.

# Basic Working

 Air Canvas is a fairly simple project to use but has a fairly intriguing and complex mechanism of working. First and foremost, the project includes the reading of frames sent by webcam(internal or external). As computers capture frames, the project plays a series of images together which appears as video capturing to the user.
These captured frames are converted into HSV frames in real-time which assists in the process of color recognition of a selected object for the machine. As the webcams come in various resolutions the projects perform morphological operations on the frames continuously by dilating and eroding the pixels in the captured frames and creating a smooth picture.
Color recognition is followed by determining the contours of the object, which are then sorted to find the center of the largest contour in the frame. The center of the largest contour defines the coordinates, therefore creating a bead around the largest contour.
After the coordinates have been determined, they are constantly pushed into dequeues calling the part of the code to draw lines on the coordinates that the bead passes through.
Air Canvas project makes use of dequeues to hold the values of coordinates for various color options offered by the project. Due to which the user can make use of the various colors in the same paint window to highlight a portion of the drawing/doodle.

# Requirements and Specifications

## SOFTWARE REQUIREMENTS:

-	Python    (3.6	and	higher)
-	Open Computer Vision
-	NumPy
-	Git
-	Microsoft Windows
-	The  software  can  be  run  on  any  system  that  supports  python.

## HARDWARE REQUIREMENTS:

-It  can  work  on  any  system  with  support  of  internal  or  external  web  camera  as  Python  is  platform  independent.

# Algorithm

*	Start reading the frames and convert the captured frames to HSV color space. (Easy for color detection)
*	Prepare the canvas frame and put the respective ink buttons on it. 
*	Adjust the trackbar values for finding the mask of colored objects.
*	Preprocess the mask with morphological operations. (Erosion and dilation)
*	Detect the contours, find the center coordinates of largest contour and keep storing them in the dequeue for successive frames.
*	Finally draw the points stored in dequeues on the frames and canvas.

# Demo

![Virtual_Paint](https://user-images.githubusercontent.com/54413011/103149837-65e1e600-4793-11eb-8d24-ca88100a3712.png)

