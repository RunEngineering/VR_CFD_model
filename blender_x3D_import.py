import bpy 
#---------------------------------Definitions---------------------------------------# 
path_tox3d='/Users/jason/Desktop/test/' 
filename_ofx3d='interfaceX3D_' 
startframe_ofx3d=0 
endframe_ofx3d=10
#-----------------------------------------------------------------------------------# 

bpy.ops.object.add() 
bpy.data.objects['Empty'].select=True 
bpy.data.objects['Empty'].name="Aux_Empty" 
bpy.context.active_object.location =(0.0, 0.0, 0.0) 
bpy.data.objects['Aux_Empty'].select=False 
  

for currentframe in range(startframe_ofx3d,(endframe_ofx3d+1)):    
    bpy.context.scene.frame_set(currentframe) 
    bpy.data.objects['Aux_Empty'].select=True 
    bpy.context.scene.objects.active = bpy.data.objects['Aux_Empty'] 
    obj = bpy.context.object 
    obj.location[2] = 0.0 
    obj.keyframe_insert(data_path='location') 
    bpy.data.objects['Aux_Empty'].select=False 
    #---------------------------Import the x3d file--------------------------------# 
    bpy.ops.import_scene.x3d(filepath=path_tox3d+filename_ofx3d+str(currentframe)+'.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='Y') 
    #-------------------------------------------------------------------------------# 
	
    #------------rename the geometry to "imported geometry"----------------#
    #--Change the "ShapeIndexedFaceSet" according to your geometry--#
    bpy.data.objects['Shape_IndexedFaceSet'].name="imported_geometry" 
    bpy.data.objects['imported_geometry'].select=True 
    bpy.context.scene.objects.active = bpy.data.objects['imported_geometry'] 
    bpy.context.active_object.material_slots[0].material.use_vertex_color_paint=True 
    bpy.data.objects['imported_geometry'].select=False 
	
    #Delete all of the imported objects except for the"imported_geometry"----#
    bpy.ops.object.delete() 

    #--------------------------------End of the loop------------------------------#
bpy.data.objects['Aux_Empty'].select=True 
bpy.ops.object.delete()
