# Field4D User Guide

Interactive user guide for the **Field4D IoT sensor system**, built with Streamlit.

The application provides step-by-step instructions for installing, configuring, operating, and troubleshooting the Field4D system across a variety of environmental and experimental measurement setups.

## Overview

Field4D is an IoT-based sensing system designed for collecting environmental measurements using wireless sensors.

This repository contains the interactive user guide for the system.

The guide walks users through the complete setup process, from preparing the required hardware to connecting the sensors and starting data collection.

Some sections are intended for regular users, while additional technical sections are available for developers.

## Guide Contents

### 1. First Step

Initial setup information and access to the Field4D web platform.

### 2. Hardware

Overview of the equipment required to operate the system, including:

- Raspberry Pi
- Raspberry Pi power supply
- CC2650 LaunchPad
- CC2650 SensorTags
- MicroSD card
- Network cables
- Batteries
- Optional debugging equipment

### 3. Firmware

Developer-oriented instructions for:

- Installing the Raspberry Pi operating system
- Flashing LaunchPad firmware
- Flashing SensorTag firmware

This section is password protected.

### 4. Software

Developer-oriented information including:

- SSH access
- Linux services and daemons
- Useful backend commands
- Example InfluxDB and MongoDB queries

This section is password protected.

### 5. Connect

Step-by-step instructions for setting up and activating the Field4D system, including:

- Network configuration
- Raspberry Pi connection
- LaunchPad connection
- SensorTag activation
- Dashboard access
- Sensor configuration
- Sensor positioning

### 6. FAQ

Troubleshooting information, system diagrams, maintenance resources, and answers to common setup questions.

## Project Structure

```text
Field4D_UserGuide/
├── .streamlit/
│   └── config.toml
│
├── Connect/
├── FAQ/
├── Firmware/
├── FirstStep/
├── Hardware/
│
├── pages/
│   ├── 02_First step.py
│   ├── 03_Hardware.py
│   ├── 04_Firmware (Developers) 🔒.py
│   ├── 05_Software (Developers) 🔒.py
│   ├── 06_Connect.py
│   ├── 07_FAQ.py
│   └── *.stl
│
├── f4d.png
├── fieldarray.png
├── moris.jpg
├── requirements.txt
└── UserGuide.py