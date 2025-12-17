# tree_modules
This repo holds examples of Christmas tree design modules for
use on a Matt Parker inspired Christimas tree being run at
[title]Lowell Makes(https://lowellmakes.com) (starting in 2025, 
possibly continuing in future years.)

# Generators
The main principal of these modules is that they define a python
generator the yields a array of pixel values and a rotation speed
that will be applied to the Christmas tree.  Each iteration of the
generator can be thought of as a 'frame' (analogous to a video frame)
that gets displayed when it is yielded.

The signature of the generator looks like this:
    def generator(pixels,tree_speed,tree_angle,form_data):
The generator must be named "**generator**" so that it can be loaded.

*pixels* is a numpy array of np_int32s each element of which
can be set to represent the 24-bit RGB color of one pixel 
on the tree.  For each int, the first 8 bits are ignored.
The next 8 bits are red, followed by green and finally 
blue in the low order bits of the int. It's often easist
to think of this a 3 hex bytes like "0x00ff9911"

The passed in value of 'pixels' is a shared memory buffer
containing a numpy array.  It's better to modify this in
place so it doesn't have to be copied, but if you return a
copy, the right thing will happen in the caller.

*tree_speed* is used to select the speed of rotation and direction
of turning for the tree.  0-stopped, 1-very_low, 2-low, 3-medium, 
4-medium-fast and 5-fast. Negative numbers turn in the opposite 
direction. *tree_angle* is an input value providing a estimate of 
the angle of rotation in degrees from an arbitrary starting point.
Both of these values a shared memory objects. To check or update 
them, access their ".value" attributes.  As "tree_speed.value" or
"tree_angle.value"

*form_data* is a place holder for future expansion. The idea is
that evenually it will be updated with CGI form available on the 
tree web-server.

By importing 'coords' into a module, the module will gain access two lists
of coordinates and a scalar holding the number of pixels on the tree.
n
*coords_xyz* are 3D cartesian values for each pixel on the tree. Each coordinate is
a list of 3 floats representing the position in space. (in arbitrary units).
Z=0 is the bottom of the tree.  (So, this is a list of lists). The position in
the coordinate list coresponds to the position in the pixels list passed into the
generator. X=0 and Y=0 are the along the trunk.

*coords_rtz* are 3D cylindrical values for each pixel on the tree. Like the cartisian
coordinates, this is a list of lists.  Each point is represented as a radius (from the
center of the tree, and angle of rotation around the tree and a height.)

*num_pixels* is the number of LEDs. This is a convenince value. The same thing can
be learned from calling **len(pixels)**.

Use **sleep()** in the generator to control how long each frame is displayed.


# Inspiration
Although no code is shared, the idea for this tree started with a set of videos by
Standup-Mathmetician Matt Parker:
- [Matt Parker Christmas Tree Part I](https://www.youtube.com/watch?v=TvlpIojusBE)
- [Matt Parker Christmas Tree Part II](https://www.youtube.com/watch?v=WuMRJf6B5Q4)
- [Matt Parker Christmas Running Other Peoples Code](https://www.youtube.com/watch?v=v7eHTNm1YtU)

His code can be found here: https://github.com/standupmaths/xmastree2021
it might be interesting to look at his code and see if some of his pattern
generation can be modified to fit into design modules that will fun on the
Lowell Makes Tree.

# How To Notes
There is a [Programming Guide](https://docs.google.com/document/d/16mJt8lYL8lNGOJ-FOCAe4bINoPwcgUNgvE3Wvyt0svI/edit?usp=sharing) describing an example of how to write a simple module.
