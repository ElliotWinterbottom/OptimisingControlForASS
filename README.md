# OptimisingControlForASS
The repository used for an internship where I was tasked with optimising the efficacy of the automatic swabbing system (ASS)  
## Hardware

### Zaber LC40B-KM01
+ Belt driven part of the automatic swabbing system
+ User manual: https://www.zaber.com/manuals/LC40B-KM01

### Zaber X-NA08A50-E09
+ Lead screw part of automatic swabbing system
+ User manual: https://www.zaber.com/manuals/X-NA-E#m-8-trajectory-control-and-behaviour

## Software 
### Interaction with hardware 
+ (I assume) both of these work off an Ascii based serial comms to speak to the controlers which are built into the used hardware. https://www.zaber.com/protocol-manual?device=X-ASR050B050B-SE03D12&peripheral=ASR050B-E03%20(Lower%20Axis)&version=7.39&protocol=ASCII
+ An API is available in the form of several libraries for python, C++, Matlab etc. https://software.zaber.com/motion-library/api/matlab
+ The API is also available for the legacy binary version for older hardware.
### Virtual enviroment 
- as of right now the hardware listed above is not supported by the virtual eniviroment.
