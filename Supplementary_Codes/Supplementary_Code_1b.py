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

pathName = "PrecedingDirectoryHere/AR_Pipeline/PLY_Files/Shell/"

fileName = "Shell"
Frame = 27
isoScale = 1

# IMPORT OBJECTS 
tempfileName = pathName+fileName+"_"+str(Frame)+".ply"
print(tempfileName)
bpy.ops.import_mesh.ply(filepath=tempfileName)
    
# TRANSFORM OBJECTS
bpy.context.object.scale[0] = 0.0
bpy.context.object.scale[1] = 0.0
bpy.context.object.scale[2] = 0.0
bpy.context.object.location[0] = -.7
bpy.context.object.location[1] = .64
bpy.context.object.location[2] = .56
bpy.ops.object.shade_smooth()

# ADD COLOUR MAP 
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

# DECIMATE GEOMETRY (TO REDUCE FINAL FILESIZE)
#bpy.ops.object.modifier_add(type='DECIMATE')
#bpy.context.object.modifiers["Decimate"].ratio = 0.25

# THICKEN GEOMETRY (TO IMPROVE VISIBILITY)
bpy.ops.object.modifier_add(type='Solidify')
bpy.context.object.modifiers["Solidify"].thickness = 0.001

# ADD LIGHTING
#light_data = bpy.data.lights.new(name="my-light-data", type='POINT')
#light_data.energy = 100
#light_object = bpy.data.objects.new(name="LIGHT", object_data=light_data)
#bpy.context.collection.objects.link(light_object)
#light_object.location = (0, 0, 0.5)
#bpy.data.collections['Collection'].objects['LIGHT'].select_set(True)

# EXPORT FILE
bpy.ops.export_scene.gltf(filepath = pathName+"/"+fileName+"_Dynamic.glb",export_nla_strips=False)