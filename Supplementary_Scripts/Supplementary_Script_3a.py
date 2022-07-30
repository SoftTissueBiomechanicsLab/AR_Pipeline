# 29 July 2022 - Mrudang Mathur
# Soft Tissue Biomechanics Lab - UT Austin 

import bpy
from mathutils import *
from math import *

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
    
bpy.ops.outliner.orphans_purge()
bpy.ops.outliner.orphans_purge()
bpy.ops.outliner.orphans_purge()

pathName = "PrecedingDirectoryHere/AR_Pipeline/PLY_Files/Continuum/"

fileName = "Continuum_USDZ"
startFrame = 0
endFrame = 20
numRange = range(endFrame,startFrame-1,-1)
isoScale = 1

key_index = 1
key_index = 1
init_frame = 1
step  = 2
nloops = 8 
counter = init_frame 

for i in numRange:
    
    # IMPORT OBJECTS 
    tempfileName = pathName+fileName+"_"+str(i)+".ply"
    print(tempfileName)
    bpy.ops.import_mesh.ply(filepath=tempfileName)
    
    # TRANSFORM OBJECTS
    bpy.context.object.scale[0] = 0.01
    bpy.context.object.scale[1] = 0.01
    bpy.context.object.scale[2] = 0.01
    bpy.context.object.location[0] = 0.
    bpy.context.object.location[1] = 0.
    bpy.context.object.location[2] = 0.25
    bpy.ops.object.shade_smooth()

    # ADD TEXTURE MAP 
    temp_matName = "Material_"+str(i)
    new_mat = bpy.data.materials.new(name=temp_matName)
    bpy.context.object.data.materials.append(new_mat)
    new_mat.use_nodes = True
    nodes = new_mat.node_tree.nodes
    material_output = nodes.get("Material Output")
    material_input = nodes.get("Material Input")
    node_attribute = nodes.new(type="ShaderNodeAttribute")
    node_attribute.attribute_name = "Col"
    new_mat.node_tree.links.new(node_attribute.outputs[0], bpy.data.materials[temp_matName].node_tree.nodes["Principled BSDF"].inputs[0])
    
# ANIMATE OBJECTS

for obj in bpy.data.collections['Collection'].all_objects:
    obj.select_set(True)

bpy.ops.object.join_shapes()

for j in range(0,nloops):

    for i in range(startFrame+1,endFrame+1):

        tempName = fileName+"_"+str(i)
        bpy.context.object.active_shape_key_index = key_index
        bpy.data.shape_keys["Key"].key_blocks[tempName].value = 0
        bpy.data.shape_keys["Key"].key_blocks[tempName].keyframe_insert("value",frame=counter)
        bpy.data.shape_keys["Key"].key_blocks[tempName].value = 1
        bpy.data.shape_keys["Key"].key_blocks[tempName].keyframe_insert("value",frame=counter+step)
        bpy.data.shape_keys["Key"].key_blocks[tempName].value = 0
        bpy.data.shape_keys["Key"].key_blocks[tempName].keyframe_insert("value",frame=counter+2*step)

        counter = counter+step
        key_index = key_index+1

bpy.context.scene.frame_end = init_frame + (endFrame-startFrame)*step*nloops+step

for obj in bpy.data.collections['Collection'].all_objects:
    obj.select_set(False)

#bpy.ops.object.select_all(action='TOGGLE')

# DELETE EXTRA FRAMES
for i in range(endFrame,startFrame,-1):
    bpy.data.objects[fileName+"_"+str(i)].select_set(True)
    bpy.ops.object.delete()

bpy.data.collections['Collection'].objects[fileName+"_"+str(startFrame)].select_set(True)

# ADD LIGHTING
#light_data = bpy.data.lights.new(name="my-light-data", type='POINT')
#light_data.energy = 100
#light_object = bpy.data.objects.new(name="LIGHT", object_data=light_data)
#bpy.context.collection.objects.link(light_object)
#light_object.location = (0, 0, 0.5)
#bpy.data.collections['Collection'].objects['LIGHT'].select_set(True)

bpy.ops.wm.usd_export(filepath=pathName+fileName+"_Dynamic.usdc", export_animation= True, selected_objects_only = True)