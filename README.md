# Augemented reality (AR) visualization pipeline
<center><img src="/Images/Figure_Summary.png" width="90%" ></center>

## Software Requirements
* To create augmented reality (AR) models you will require the following packages:
  * [ParaView 5.10](https://www.paraview.org/download/)
  * [Blender 2.83](https://download.blender.org/release/)
  * [BlenderUSDZ addon](https://github.com/robmcrosby/BlenderUSDZ/tree/e8a002849b85df3daba339912f4cc91fb042fe6d) 
  * [MacOS users: Apple Reality Converter](https://developer.apple.com/augmented-reality/tools/)
  * [Windows/Unix users: Apple usdzconvert utility](https://github.com/tappi287/usdzconvert_windows)
* To host and render the AR models you will need to include  the [model-viewer](https://modelviewer.dev/) API within your webpage. 

## File Description
We provide '.ply' files of results from fintie element simulations discretized with i) continuum, ii) shell, and iii) beam finite elements. These files are located within similarly named subfolders under the "PLY_Files/" directory. Moreover, we provide '.glb' and '.usdz' files of the AR models corresponding to these results. 

## Code Description
We provide example python scripts to automatically create AR models from continuum, shell, and beam finite elements. These scripts may be run from the 'Scipting' window within Blender or from the command line. To execute these scripts, users will need the '.ply' files provided for each example. The pythons scrips are as follows: 

1. Static Models
  * Supplementary_Code_1a.py : Model with continuum elements
  * Supplementary_Code_1b.py : Model with shell elements
  * Supplementary_Code_1c.py : Model with beam elements 
2. Dynamic Models for Android
  * Supplementary_Code_2a.py : Model with continuum elements
  * Supplementary_Code_2b.py : Model with shell elements
  * Supplementary_Code_2c.py : Model with beam elements 
3. Dynamic Models for iOS
  * Supplementary_Code_3a.py : Model with continuum elements
  * Supplementary_Code_3b.py : Model with shell elements
  * Supplementary_Code_3c.py : Model with beam elements 

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
