# Augemented reality (AR) visualization pipeline
<center><img src="/Images/Figure_Summary.png" width="90%" ></center>

## Software Requirements
* To create augmented reality (AR) models you will require the following software:
  * [ParaView 5.10](https://www.paraview.org/download/)
  * [Blender 2.83](https://download.blender.org/release/)
  * [USDZExport addon for Blender]() 
  * [MacOS users: Apple Reality Converter]()
  * [Windows/Unix users: Apple usdzconvert utility]()
* To view the augmented reality models you will need a smartphone compatible with [model-viewer](https://modelviewer.dev/). 

## File Description

## Code Description
We provide Abaqus input files used to run simulations of the healthy, diseased, and repaired tricuspid valve. For additional details on simulation settings and element choices please refer to the main text. This repository includes the following input files: 



Additionally, we provide a user defined material model (Leaflet_Material.f) that must be used to successfully run the input files listed above. We recommend all models be run using double precision in Abaqus/Explicit




This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
