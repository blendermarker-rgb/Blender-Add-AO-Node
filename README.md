# Blender Add AO Node

A small Blender add-on that quickly adds an Ambient Occlusion node setup to materials on simple objects.

It can add the AO setup to either:

- The currently selected object's active material
- All node-based materials in the Blender file

## What It Does

The add-on creates and connects:

- Ambient Occlusion node
- Color Ramp
- Mix node set to Multiply

The resulting setup is connected to the Base Color input of the Principled BSDF shader.

If the material already has an Image Texture connected to Base Color, the add-on includes that texture in the new AO setup.

## Installation

### Blender 4.5

1. Download `add_ao_node.py`.
2. Open Blender.
3. Go to **Edit > Preferences**.
4. Select **Add-ons**.
5. Open the menu in the upper-right corner.
6. Choose **Install from Disk**.
7. Select `add_ao_node.py`.
8. Enable **Add AO Node** if it is not already enabled.

## How To Use

1. Open the **Shading** workspace.
2. Open the sidebar in the Shader Editor by pressing **N**.
3. Select the **AO Node** tab.

You will see two buttons:

### Add AO Node Selected

Adds the AO node setup to the active material of the selected object.

### Add AO Node All

Adds the AO node setup to all node-based materials in the current Blender file.

## Why I Made It

I wanted a quick way to add the same Ambient Occlusion node setup to materials without rebuilding the node arrangement manually each time.

This add-on is intentionally simple and focused on that one task.

## Compatibility

Designed for:

**Blender 4.5**

## Author

**BlenderMark**

Created as a free utility for the Blender community.<img width="1289" height="405" alt="AO" src="https://github.com/user-attachments/assets/f9eed22e-044c-4cf7-bc13-83a173fe565f" />
