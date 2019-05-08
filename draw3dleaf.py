import bpy
import random
import bmesh
from draw import draw_cylinder

def draw_apple(location):
    if (not("brow" in bpy.data.materials)):
        mat = bpy.data.materials.new("brow")
        mat.diffuse_color = (0.55,0.27,0.074)
        red = bpy.data.materials.new("red")
        red.diffuse_color = (1,0,0)
    else:
        mat = bpy.data.materials["brow"]
        red = bpy.data.materials["red"]
    draw_cylinder(location, (location[0], location[1], location[2] - 0.15), 0.03, mat)
    loc = (location[0], location[1], location[2] - 0.3)
    bpy.ops.mesh.primitive_uv_sphere_add(size=0.2, location=loc)
    o = bpy.context.selected_objects[0] 
    o.active_material = red

def draw_leaf(location):
    color = random.randint(0,3)
    c = "FEU" + str(color)
    if (not(c in bpy.data.materials)):
        mat = bpy.data.materials.new(c)
        if (color == 0):
            mat.diffuse_color = (0,1,0)
        elif (color == 1):
            mat.diffuse_color = (0.13,0.55,0.13)
        elif (color == 2):
            mat.diffuse_color = (0,0.5,0)
        elif (color == 3):
            mat.diffuse_color = (0,0.39,0)
    else:
        mat = bpy.data.materials[c]
    x = location[0]
    y = location[1]
    z = location[2]
    dir = random.randint(0,3)
    v0 = ((x, y, z), (x + 0.1, y - 0.1, z + 0.1), (x + 0.2, y - 0.1, z + 0.2), (x + 0.3, y, z + 0.3), (x + 0.2, y + 0.1, z + 0.2), (x + 0.1, y + 0.1, z + 0.1))
    v1 = ((x, y, z), (x - 0.1, y - 0.1, z + 0.1), (x - 0.2, y - 0.1, z + 0.2), (x - 0.3, y, z + 0.3), (x - 0.2, y + 0.1, z + 0.2), (x - 0.1, y + 0.1, z + 0.1))
    v2 = ((x, y, z), (x + 0.1, y - 0.1, z + 0.1), (x + 0.1, y - 0.2, z + 0.2), (x, y - 0.3, z + 0.3), (x - 0.1, y - 0.2, z + 0.2), (x - 0.1, y - 0.1, z + 0.1))
    v3 = ((x, y, z), (x + 0.1, y + 0.1, z + 0.1), (x + 0.1, y + 0.2, z + 0.2), (x, y + 0.3, z + 0.3), (x - 0.1, y + 0.2, z + 0.2), (x - 0.1, y + 0.1, z + 0.1))
    vt = [v0, v1, v2, v3]
    verts = vt[dir]
    bm = bmesh.new()
    for v in verts:
        bm.verts.new(v)
    bm.faces.new(bm.verts)
    bm.normal_update()

    me = bpy.data.meshes.new("")
    bm.to_mesh(me)

    ob = bpy.data.objects.new("", me)
    ob.active_material = mat
    bpy.context.scene.objects.link(ob)
    bpy.context.scene.update()

def draw_flower(location, color):
    clr = ["FLWR", "FLWB", "FLWO", "FLWR"]
    co = clr[color]
    var = random.randint(0,2)
    co = co + str(var)
    if (not(co in bpy.data.materials)):
        mat = bpy.data.materials.new(co)
        if (color == 0):
            if (var == 0):
                mat.diffuse_color = (1,0.6,0.65)
            elif (var == 1):
                mat.diffuse_color = (1,0.41,0.71)
            elif (var == 2):
                mat.diffuse_color = (1,0.08,0.58)
        elif (color == 1):
            if (var == 0):
                mat.diffuse_color = (0.53,0.81,0.98)
            elif (var == 1):
                mat.diffuse_color = (0,0.75,1)
            elif (var == 2):
                mat.diffuse_color = (0.12,0.56,1)
        elif (color == 2):
            if (var == 0):
                mat.diffuse_color = (1,0.65,0)
            elif (var == 1):
                mat.diffuse_color = (1,0.55,0)
            elif (var == 2):
                mat.diffuse_color = (1,0.5,0.31)
        elif (color == 3):
            if (var == 0):
                mat.diffuse_color = (0.86,0.08,0.24)
            elif (var == 1):
                mat.diffuse_color = (0.55,0,0)
            elif (var == 2):
                mat.diffuse_color = (0.7,0.13,0.13)            
    else:
        mat = bpy.data.materials[co]
    x = location[0]
    y = location[1]
    z = location[2]
    v0 = ((x, y, z), (x + 0.05, y - 0.05, z + 0.1), (x + 0.1, y - 0.05, z + 0.2), (x + 0.15, y, z + 0.3), (x + 0.1, y + 0.05, z + 0.2), (x + 0.05, y + 0.05, z + 0.1))
    v1 = ((x, y, z), (x - 0.05, y - 0.05, z + 0.1), (x - 0.1, y - 0.05, z + 0.2), (x - 0.15, y, z + 0.3), (x - 0.1, y + 0.05, z + 0.2), (x - 0.05, y + 0.05, z + 0.1))
    v2 = ((x, y, z), (x + 0.05, y - 0.05, z + 0.1), (x + 0.05, y - 0.1, z + 0.2), (x, y - 0.15, z + 0.3), (x - 0.05, y - 0.1, z + 0.2), (x - 0.05, y - 0.05, z + 0.1))
    v3 = ((x, y, z), (x + 0.05, y + 0.05, z + 0.1), (x + 0.05, y + 0.1, z + 0.2), (x, y + 0.15, z + 0.3), (x - 0.05, y + 0.1, z + 0.2), (x - 0.05, y + 0.05, z + 0.1))
    v0b = ((x, y, z), (x + 0.05, y - 0.05, z + 0.2), (x + 0.1, y - 0.05, z + 0.3), (x + 0.15, y, z + 0.4), (x + 0.1, y + 0.05, z + 0.3), (x + 0.05, y + 0.05, z + 0.2))
    v1b = ((x, y, z), (x - 0.05, y - 0.05, z + 0.2), (x - 0.1, y - 0.05, z + 0.3), (x - 0.15, y, z + 0.4), (x - 0.1, y + 0.05, z + 0.3), (x - 0.05, y + 0.05, z + 0.2))
    v2b = ((x, y, z), (x + 0.05, y - 0.05, z + 0.2), (x + 0.05, y - 0.1, z + 0.3), (x, y - 0.15, z + 0.4), (x - 0.05, y - 0.1, z + 0.3), (x - 0.05, y - 0.05, z + 0.2))
    v3b = ((x, y, z), (x + 0.05, y + 0.05, z + 0.2), (x + 0.05, y + 0.1, z + 0.3), (x, y + 0.15, z + 0.4), (x - 0.05, y + 0.1, z + 0.3), (x - 0.05, y + 0.05, z + 0.2))
    vt = [v0, v1, v2, v3, v0b, v1b, v2b, v3b]
    bm = bmesh.new()
    for verts in vt:
        for v in verts:
            bm.verts.new(v)
        bm.faces.new(bm.verts)
        bm.normal_update()

    me = bpy.data.meshes.new("")
    bm.to_mesh(me)

    ob = bpy.data.objects.new("", me)
    ob.active_material = mat
    bpy.context.scene.objects.link(ob)
    bpy.context.scene.update()
