import bpy

bl_info = {
    "name" : "Object Adder",
    "author" : "Quinn Dacre",
    "version" : (1,0),
    "blender" : (2,80,0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",

}


class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My first Addon"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add an object", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = "CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = "SPHERE")
        row = layout.row()
        row.operator("object.text_add")
        row.operator("mesh.primitive_cube_add")
       


class PanelA(bpy.types.Panel):
    bl_label = "Scaling"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My first Addon"
    bl_parent_id = "PT_TestPanel"
    bl_options = { "DEFAULT_CLOSED" }
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "This is Panel A", icon = 'FONTPREVIEW')
        
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My first Addon"
    bl_parent_id = "PT_TestPanel"
    bl_options = { "DEFAULT_CLOSED" }
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = "Select a sphere.", icon = 'FONTPREVIEW')
        row = layout.row()
        row.operator("transform.resize")
        col = layout.column()
        col.prop(obj, "scale")
        layout.scale_y = 1.4
        
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.register_class(PanelB)

if __name__ == "__main__":
    register()

