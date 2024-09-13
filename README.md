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
from there you'll want to add the 

