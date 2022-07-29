# Augemented Reality Visualization Pipeline
<center><img src="/Images/Figure_Summary.png" width="90%" ></center>

## Software Requirements
* To create augmented reality (AR) models you will require the following software:
  * ParaView 5.10
  * Blender 2.83
  * USDZExport addon for Blender 
  * Apple Reality Converter (for MacOS users)
  * Apple usdzconvert utility (for Windows/Unix users)
* To view the augmented reality models you will need a smartphone compatible with [model-viewer](https://modelviewer.dev/). 

<center><img src="/Images/Paper_AR_Instructions.png" width="90%" ></center>

## Code Description
We provide Abaqus input files used to run simulations of the healthy, diseased, and repaired tricuspid valve. For additional details on simulation settings and element choices please refer to the main text. This repository includes the following input files: 

* Healthy_QuasiStatic.inp
  * Healthy tricuspid valve modeled from end-diastole to end-systole.
* Healthy_Dynamic.inp
  * Healthy tricuspid valve model running over one cardiac cycle i.e from end-diastole to end-diastole.
* Diseased_QuasiStatic.inp
  * Regurgitant tricuspid valve model loaded to pathological pressures at end-systole.
* Annuloplasty_QuasiStatic.inp
  * Regurgitant tricuspid valve model repaired via annuloplasty, loaded to pathological pressures at end-systole.
* Clipping_QuasiStatic.inp
  * Regurgitant tricuspid valve model repaired via clip-based repair, loaded to pathological pressures at end-systole.

Additionally, we provide a user defined material model (Leaflet_Material.f) that must be used to successfully run the input files listed above. We recommend all models be run using double precision in Abaqus/Explicit


This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
