# vpython_optics_bench
A 3D optics bench using VPython

Preliminary version of a 3D optics bench.  At present only transparent spheres and boxes can be placed in the world but there are future plans to add convex and concave lenses and mirrors.  You can create single light rays, point sources, and a beam (bundle) of light rays.  The code is currently a little rough around the edges but stop back for updates in the near future.

# Classes

* ray(start_point,direction,color)

A single light ray.  This is used by all other classes to draw rays but you can create a single ray using this class.  It must be added to the **world()** class to be drawn.  The length is set in the **world()** class.

* beam(**position**, **direction**, **width**)

Draws a beam of rays centered at **position**.  This class will call the **ray()** class to draw a series of rays.  The density of rays in currently hard-coded into the class.

* pointSource(**position**)

Draws a point source centered at **position**.  This calls the **ray()** class.  The density of rays is currently hard-coded into the class.

* world()

The **world()** class is what makes everything happen.  The world must be instantiated before you can start drawing anything.  All rays and objects must be added to this class after instantiation for the rays and objects to interact.  The **world()** class draws each ray a length **dL** and checks to see if it has crossed a boundary.  If it crosses a boundary it uses Snell's law to refract the ray and continues drawing the ray until it reaches a set maximum length.

* ball(**position**, **radius**)

This is a  transparent sphere.  Because we use Snell's law at the boundaries the sphere does display spherical aberrations.  

* block(**position**, **axis**, **up**, **length**, **width**, **height**, **material**, **opacity**)

**position**, **axis**, and **up** are the same properties that the VPython **box()** class has.  The only material currently supported is "glass".


