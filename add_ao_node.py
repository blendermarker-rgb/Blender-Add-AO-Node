bl_info = {
    "name": "Add AO Node",
    "author": "BlenderMark",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "Shading > N Panel > Add AO Node",
    "description": "Add an AO node to the material",
    "category": "Shading",
}

import bpy


# --------------------------------------------------
# Safe Layout Helper (NO COLLISION QUERIES)
# --------------------------------------------------

def stack_node(node, x, y):
    node.location = (x, y)
    return y - 180


# --------------------------------------------------
# Operators
# --------------------------------------------------

class AddAONodeSelected(bpy.types.Operator):
    bl_idname = "material.add_ao_node_selected"
    bl_label = "Add AO Node Selected"
    bl_description = "Add AO Node To Current Material"

    def execute(self, context):
        material = context.object.active_material
        if material:
            self.add_ao_node(material)
            return {'FINISHED'}
        else:
            self.report({'INFO'}, "No active material found")
            return {'CANCELLED'}

    def add_ao_node(self, material):
        if not material.use_nodes:
            return

        principled_node = material.node_tree.nodes.get('Principled BSDF')
        if not principled_node:
            return

        nodes = material.node_tree.nodes
        links = material.node_tree.links

        base_x, base_y = principled_node.location

        texture_node = None
        for link in principled_node.inputs['Base Color'].links:
            if link.from_node.type == 'TEX_IMAGE':
                texture_node = link.from_node
                break

        ao_node = nodes.new('ShaderNodeAmbientOcclusion')
        color_ramp_node = nodes.new('ShaderNodeValToRGB')
        color_ramp_node.color_ramp.elements[0].position = 0

        mix_node = nodes.new('ShaderNodeMix')
        mix_node.data_type = 'RGBA'
        mix_node.blend_type = 'MULTIPLY'

        y = base_y
        y = stack_node(ao_node, base_x - 900, y)
        y = stack_node(color_ramp_node, base_x - 650, y)
        stack_node(mix_node, base_x - 300, y)

        if texture_node:
            texture_node.location = (base_x - 650, base_y + 220)
            links.new(mix_node.inputs[6], texture_node.outputs[0])
        else:
            mix_node.inputs[6].default_value = principled_node.inputs['Base Color'].default_value

        links.new(color_ramp_node.inputs[0], ao_node.outputs[1])
        links.new(mix_node.inputs[7], color_ramp_node.outputs[0])
        links.new(principled_node.inputs['Base Color'], mix_node.outputs[2])


class AddAONodeAll(bpy.types.Operator):
    bl_idname = "material.add_ao_node_all"
    bl_label = "Add AO Node All"
    bl_description = "Add AO Node To All Materials"

    def execute(self, context):
        for material in bpy.data.materials:
            if material.use_nodes:
                self.add_ao_node(material)
        return {'FINISHED'}

    def add_ao_node(self, material):
        if not material.use_nodes:
            return

        principled_node = material.node_tree.nodes.get('Principled BSDF')
        if not principled_node:
            return

        nodes = material.node_tree.nodes
        links = material.node_tree.links

        base_x, base_y = principled_node.location

        texture_node = None
        for link in principled_node.inputs['Base Color'].links:
            if link.from_node.type == 'TEX_IMAGE':
                texture_node = link.from_node
                break

        ao_node = nodes.new('ShaderNodeAmbientOcclusion')
        color_ramp_node = nodes.new('ShaderNodeValToRGB')
        color_ramp_node.color_ramp.elements[0].position = 0

        mix_node = nodes.new('ShaderNodeMix')
        mix_node.data_type = 'RGBA'
        mix_node.blend_type = 'MULTIPLY'

        y = base_y
        y = stack_node(ao_node, base_x - 900, y)
        y = stack_node(color_ramp_node, base_x - 650, y)
        stack_node(mix_node, base_x - 300, y)

        if texture_node:
            texture_node.location = (base_x - 650, base_y + 220)
            links.new(mix_node.inputs[6], texture_node.outputs[0])
        else:
            mix_node.inputs[6].default_value = principled_node.inputs['Base Color'].default_value

        links.new(color_ramp_node.inputs[0], ao_node.outputs[1])
        links.new(mix_node.inputs[7], color_ramp_node.outputs[0])
        links.new(principled_node.inputs['Base Color'], mix_node.outputs[2])


# --------------------------------------------------
# Panel
# --------------------------------------------------

class AddAONodePanel(bpy.types.Panel):
    bl_label = "Add AO Node"
    bl_idname = "MATERIAL_PT_add_ao_node"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'AO Node'

    @classmethod
    def poll(cls, context):
        return context.object and context.object.active_material

    def draw(self, context):
        layout = self.layout
        layout.operator("material.add_ao_node_selected")
        layout.operator("material.add_ao_node_all")


# --------------------------------------------------
# Registration
# --------------------------------------------------

def register():
    bpy.utils.register_class(AddAONodeSelected)
    bpy.utils.register_class(AddAONodeAll)
    bpy.utils.register_class(AddAONodePanel)


def unregister():
    bpy.utils.unregister_class(AddAONodeSelected)
    bpy.utils.unregister_class(AddAONodeAll)
    bpy.utils.unregister_class(AddAONodePanel)


if __name__ == "__main__":
    register()
