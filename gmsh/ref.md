C. Geuzaine and J.-F. Remacle. Gmsh: a three-dimensional finite element mesh generator with built-in pre- and post-processing facilities. International Journal for Numerical Methods in Engineering 79(11), pp. 1309-1331, 2009.

pip install --upgrade gmsh

python -c "import gmsh; gmsh.initialize(); gmsh.fltk.run(); gmsh.finalize()"


<!-- File Version 2 -->
$MeshFormat
version-number file-type data-size
$EndMeshFormat
$Nodes
number-of-nodes
node-number x-coord y-coord z-coord
…
$EndNodes
$Elements
number-of-elements
elm-number elm-type number-of-tags < tag > … node-number-list
…
$EndElements
$PhysicalNames
number-of-names
phyical-number "physical-name"
…
$EndPhysicalNames
$NodeData
number-of-string-tags
< "string-tag" >
…
number-of-real-tags
< real-tag >
…
number-of-integer-tags
< integer-tag >
…
node-number value …
…
$EndNodeData
$ElementData
number-of-string-tags
< "string-tag" >
…
number-of-real-tags
< real-tag >
…
number-of-integer-tags
< integer-tag >
…
elm-number value …
…
$EndElementData
$ElementNodeData
number-of-string-tags
< "string-tag" >
…
number-of-real-tags
< real-tag >
…
number-of-integer-tags
< integer-tag >
…
elm-number number-of-nodes-per-element value …
…
$ElementEndNodeData