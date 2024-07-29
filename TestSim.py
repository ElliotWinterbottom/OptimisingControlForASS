import pybullet as p
from time import sleep
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.resetSimulation(p.RESET_USE_DEFORMABLE_WORLD)

p.setGravity(0, 0, -10)

planeOrn = [0,0,0,1]#p.getQuaternionFromEuler([0.3,0,0])
planeId = p.loadURDF("plane.urdf", [0,0,-2],planeOrn)

boxId = p.loadURDF("cube.urdf", [0,3,2],useMaximalCoordinates = True)


ballId = p.loadSoftBody("Silicone_swabberV2.obj", basePosition = [0,0,5], scale = 100, mass = 1., useNeoHookean = 0, useBendingSprings=1,useMassSpring=1, springElasticStiffness=100, springDampingStiffness=.1, springDampingAllDirections = 1, useSelfCollision = 1, frictionCoeff = .5, useFaceContact=1, collisionMargin = 0.04)
p.changeVisualShape
p.setTimeStep(0.001)
p.setPhysicsEngineParameter(sparseSdfVoxelSize=0.25)


#logId = p.startStateLogging(p.STATE_LOGGING_PROFILE_TIMINGS, "perf.json")

while p.isConnected():
  p.stepSimulation()  
  #there can be some artifacts in the visualizer window, 
  #due to reading of deformable vertices in the renderer,
  #while the simulators updates the same vertices
  #it can be avoided using
  #p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING,1)
  #but then things go slower
  p.setGravity(0,0,-10)
  sleep(1./240.)
  
#p.resetSimulation()
#p.stopStateLogging(logId)

## big list of what I need to make the damn thing function ##

#1 obj file (what is this how does it work)
#  1.1 seem like just a data file which holds data about a grid of points arranged in space and the surfaces which form between them.
#  1.2 alot of the time they'll come with mtl files which hold data about the material being used. that is to say, colour, texture ect. I don't think they actually hold and material properties 

#2 maybe a texture on the object? others seemed to have that 

#3 the material properties of silicone need to be somehow related to the mesh so that the simulation is acurate

