# 22 July 2023 - Mrudang Mathur
# Soft Tissue Biomechanics Lab - UT Austin 

import bpy
from mathutils import *
from math import *

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
    
# CLEAR WORKSPACE OF UNWANTED OBJECTS
bpy.ops.outliner.orphans_purge()
bpy.ops.outliner.orphans_purge()
bpy.ops.outliner.orphans_purge()

pathName = "PrecedingDirectoryHere/AR_Pipeline/Workshop_Materials/Walkthrough_2/PLY/"

fileName_Shell = "Solid"
fileName_Fluid = "Fluid_Streamline"

# IMPORT SHELL 
tempfileName = pathName+fileName_Shell+".ply"
print(tempfileName)
bpy.ops.import_mesh.ply(filepath=tempfileName)
    
# TRANSFORM SHELL
bpy.context.object.scale[0] = 1.
bpy.context.object.scale[1] = 1.
bpy.context.object.scale[2] = 1.
bpy.context.object.location[0] = 0.
bpy.context.object.location[1] = 0.
bpy.context.object.location[2] = 1.
bpy.ops.object.shade_smooth()

# ADD COLOUR MAP 
temp_matName = "Material_0"
new_mat = bpy.data.materials.new(name=temp_matName)
bpy.context.object.data.materials.append(new_mat)
new_mat.use_nodes = True
nodes = new_mat.node_tree.nodes
material_output = nodes.get("Material Output")
material_input = nodes.get("Material Input")
node_attribute = nodes.new(type="ShaderNodeAttribute")
node_attribute.attribute_name = "Col"
new_mat.node_tree.links.new(node_attribute.outputs[0], bpy.data.materials[temp_matName].node_tree.nodes["Principled BSDF"].inputs[0])

# THICKEN GEOMETRY (TO IMPROVE VISIBILITY)
bpy.ops.object.modifier_add(type='SOLIDIFY') #Note: Some versions of Blender use "Solidify" 
bpy.context.object.modifiers["Solidify"].thickness = 0.0001 #Note: Some versions of Blender use "SOLIDIFY" 

# IMPORT FLUID
tempfileName = pathName+fileName_Fluid+".ply"
print(tempfileName)
bpy.ops.import_mesh.ply(filepath=tempfileName)
    
# TRANSFORM FLUID
bpy.context.object.scale[0] = 1.
bpy.context.object.scale[1] = 1.
bpy.context.object.scale[2] = 1.
bpy.context.object.location[0] = 0.
bpy.context.object.location[1] = 0.
bpy.context.object.location[2] = 1.
bpy.ops.object.shade_smooth()

# ADD COLOUR MAP 
temp_matName = "Material_1"
new_mat = bpy.data.materials.new(name=temp_matName)
bpy.context.object.data.materials.append(new_mat)
new_mat.use_nodes = True
nodes = new_mat.node_tree.nodes
material_output = nodes.get("Material Output")
material_input = nodes.get("Material Input")
node_attribute = nodes.new(type="ShaderNodeAttribute")
node_attribute.attribute_name = "Col"
new_mat.node_tree.links.new(node_attribute .outputs[0], bpy.data.materials[temp_matName].node_tree.nodes["Principled BSDF"].inputs[0])

# EXPORT FILE
bpy.ops.export_scene.gltf(filepath = pathName+"/"+fileName_Fluid+"_Static.glb")