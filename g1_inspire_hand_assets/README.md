# Unitree G1 + Inspire Hand Assets (MuJoCo)

This repository contains a **Unitree G1 model with Inspire hands** for MuJoCo-based simulation workflows.

## What is included

- `g1_29dof_inspire_hand.xml` - Main MuJoCo robot model (G1 body + Inspire hands)
- `scene_inspire_hand.xml` - Ready-to-run MuJoCo scene that includes the model
- `g1_body29_hand14.urdf` - URDF version of the G1 + Inspire hand configuration
- `meshes/` - Mesh assets used by the G1 body/robot model
- `inspire_hand_meshes/` - Mesh assets for Inspire hand visual/collision geometry

## What was removed

All exoskeleton-related assets were removed so this folder only keeps the G1 + Inspire hand setup.

## Quick start (MuJoCo)

From this folder, launch the scene in MuJoCo:

```bash
mjpython viewer.py scene_inspire_hand.xml
```

or with the MuJoCo viewer CLI (if installed):

```bash
python -m mujoco.viewer --mjcf=scene_inspire_hand.xml
```

If your local setup uses a different viewer entrypoint, load `scene_inspire_hand.xml` as the scene file.

## Current usage

This asset pack is currently being used for **robot-ide.com** MuJoCo-based simulations.

It is also being used to:

- Learn and study **Inspire Hand movement behaviors** on Unitree G1.
- Teach **Vision-Language-Action (VLA) task concepts** using Unitree G1 with Inspire Hands for **RoboStores** and **RoboUniversity**.

## Demo video

Primary (browser-friendly): [media/g1_inspire_hand_demo.mp4](media/g1_inspire_hand_demo.mp4)

Original recording: [media/g1_inspire_hand_demo.mov](media/g1_inspire_hand_demo.mov)

<video controls width="960">
	<source src="media/g1_inspire_hand_demo.mp4" type="video/mp4">
	<source src="media/g1_inspire_hand_demo.mov" type="video/quicktime">
	Your browser does not support embedded video playback. Use the links above.
</video>

## Notes

- Paths are organized for local use from this directory.
- If you move files, update mesh/include paths in the XML/URDF files accordingly.

## License and attribution

- License: no open-source license is included in this folder.
- Ownership/credits: Unitree G1 and Inspire Hand model/asset rights remain with their respective owners.
- Usage: intended for MuJoCo simulation workflows (including robot-ide.com integration) under your authorized usage terms.
