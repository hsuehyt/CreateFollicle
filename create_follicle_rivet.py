import maya.cmds as cmds

# Get selected face
selection = cmds.ls(sl=True, fl=True)
if not selection:
    cmds.warning("Select a face first!")
else:
    mesh = selection[0].split('.')[0]  # Get mesh name

    # Create follicle
    follicle = cmds.createNode('follicle')
    follicleTransform = cmds.listRelatives(follicle, parent=True)[0]

    # Connect mesh to follicle
    cmds.connectAttr(mesh + ".outMesh", follicle + ".inputMesh")
    cmds.connectAttr(mesh + ".worldMatrix[0]", follicle + ".inputWorldMatrix")
    cmds.connectAttr(follicle + ".outTranslate", follicleTransform + ".translate")
    cmds.connectAttr(follicle + ".outRotate", follicleTransform + ".rotate")

    # Adjust follicle UV parameters
    cmds.setAttr(follicle + ".parameterU", 0.5)
    cmds.setAttr(follicle + ".parameterV", 0.5)

    cmds.select(follicleTransform)
    print("Follicle successfully created!")
