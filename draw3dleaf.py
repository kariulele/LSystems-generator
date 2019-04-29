import bpy
import random
import bmesh

def draw_leaf(location):
    if (not("PKHG" in bpy.data.materials)):
        mat = bpy.data.materials.new("PKHG")
        mat.diffuse_color = (0,1,0)
    else:
        mat = bpy.data.materials["PKHG"]
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