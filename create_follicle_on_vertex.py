import maya.cmds as cmds

def create_follicle_on_vertex():
    sel = cmds.ls(sl=True, fl=True)
    if not sel:
        cmds.warning("Select a vertex first!")
        return
    
    # Get mesh and vertex index
    mesh = sel[0].split('.')[0]  # Extract mesh name
    vertex_index = int(sel[0].split('[')[-1].split(']')[0])  # Extract vertex index

    # Get UV coordinates of the vertex
    uv = cmds.polyListComponentConversion(sel, fv=True, tuv=True)
    uv = cmds.ls(uv, fl=True)
    if not uv:
        cmds.warning("Vertex does not have UV coordinates!")
        return

    uv_coord = cmds.polyEditUV(uv[0], q=True)  # Get U and V coordinates
    u_val, v_val = uv_coord[0], uv_coord[1]

    # Create follicle
    follicle_shape = cmds.createNode("follicle")
    follicle_transform = cmds.listRelatives(follicle_shape, parent=True)[0]

    # Connect follicle to mesh
    cmds.connectAttr(f"{mesh}.outMesh", f"{follicle_shape}.inputMesh")
    cmds.connectAttr(f"{mesh}.worldMatrix[0]", f"{follicle_shape}.inputWorldMatrix")
    cmds.connectAttr(f"{follicle_shape}.outTranslate", f"{follicle_transform}.translate")
    cmds.connectAttr(f"{follicle_shape}.outRotate", f"{follicle_transform}.rotate")

    # Set follicle UV position
    cmds.setAttr(f"{follicle_shape}.parameterU", u_val)
    cmds.setAttr(f"{follicle_shape}.parameterV", v_val)

    cmds.select(follicle_transform)
    print(f"Follicle created at vertex {vertex_index} on {mesh}.")

# Run the function
create_follicle_on_vertex()
