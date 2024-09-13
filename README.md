# OptimisingControlForASS
The repository used for an internship where I was tasked with optimising the efficacy of the automatic swabbing system (ASS)  
## motors

### Zaber X-NMS23-E08P1
+ Belt driven part of the automatic swabbing system
+ Can be found here https://www.zaber.com/products/stepper-motors/X-NMS-E/specs?part=X-NMS23-E08P1
### Zaber T-NA08A50
+ Lead screw part of automatic swabbing system
+ can be found here https://www.zaber.com/products/linear-actuators/T-NA/specs?part=T-NA08A50
+ Please note that this hardware has been discontinued by the manufacturer 

### Motor control software.  
Zaber provideds two main ways of interacting with hardware: ASCII protocol and Binary protocol. Neither of these devices work with the ASCII protocol and as such the binary has to be used. Documentation for both can be found here: https://www.zaber.com/protocol-manual?protocol=Binary

Zaber also provide a series of APIs for different programming platforms. The one used here is MatLab. A guide to the installation and use of the Zaber MatLab API can be found here: https://software.zaber.com/motion-library/docs/tutorials/install/matlab
you will need the latter to edit and run the code in the matlab app designer.

## Camera 
### Intel Realsense camera 
This camera is possibly one of the worst documented peices of hardware I've ever had the misfortune of working with. For what it's worth a guide can be found here: https://dev.intelrealsense.com/docs/matlab-wrapper
You will want to download the software developement kit 2.0 whose latest version as of right now does not support any of the matlab side of things like it's supposed to. Instead the release you'll want is 2.54.1 which can be found here https://github.com/IntelRealSense/librealsense/releases
from there you'll want to find the matlab folder of the SDK. On windows by default this is located at C:\Program Files (x86)\Intel RealSense SDK 2.0\matlab
However this may be different for you. 
take this filepath and add it to the search path in matlab. A guide for doing so can be found here: https://uk.mathworks.com/help/matlab/matlab_env/add-remove-or-reorder-folders-on-the-search-path.html

## Force sensor 
Fortunately the force sensor does not require it's own library. However a script version of the code has been included for testing and convenience.

## MatLab app designer and the application itself 
This application is written in MatLab app designer which is a workspace with a few quirks.
+Firstly, simply clicking on the .mlapp file will not in fact open the designer. It will isntead open the application itself. To actually edit the file. open MatLab, go to the apps tab, and click on the design app button on the left hand side and then, once the app designer has opened, procede to open the file. 
+ The next thing you'll notice is that the first thing which opens is a GUI designer. There is a seperate tab for a programatic view of the app.
+ Unfortunately it is extremely handholding when it comes to how you can write your code. deleting and creating callbacks and functions must be done via the menue instead of the text editor.
+ It is also extremely hostile to libraries. If you wish to use a library in a specific function you must import that library at the start of said function. There is no global import scope.
Once you get past these quirks its Ok to work with.

the application itself requires that you have all three devices (linear actuators, camera, force sensor) plugged in at once to work. Please make sure:
+ all three devices are plugged in
+ the linear actuators are not currently moving,being told to move, or being controlled in another application (you can tell if they're moving because the LED light present on either one of them will be flashing)
+ the camera is plugged into a USB3.0 port as any other simply won't do for intel.
+ make sure you know which com ports are which and are named correctly in the program (there are two seperate functions which name the same com port for motor control (startup and move) make sure this is done for both of them)
+ MAKE SURE THE MOTORS HAVE POWER (I have made this mistake too many times myself and do not want you to do the same)

## CAD files 
Alongside the actual program itself are a series of links to onshape. Onshape is a cloud and broswer based 3D modelling cad software. Accounts are free and these documents should be publicly viewable and downloadable into a file format of your chosing.
## silicone moulding 
The end effector of the robot which this firmware was made for is made of silicone rubber.
+ A link to the supplier of this silicone can be found here: https://www.smooth-on.com/product-line/ecoflex/
+ please follow the listed instructions for curing and degassing
+ as some of these silicones have a pot time (time where silicone is still a liquid) of as short at 18 mins I recommend using a wide but shallow container to degass in before pouring VERY carefully into your skinnier mould.

