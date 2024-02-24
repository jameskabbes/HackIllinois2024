.. {-{package_name}-} documentation master file, created by
   sphinx-quickstart on Thu Mar 23 15:36:13 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

John Deere | HackIllinois 2024 
==============================

Overview
--------

Starter code for this project in found in the ``HackIllinois2024/code`` folder of the repository. Follow along below.

Quickstart
----------

1. Setup one system on your vehicle at a time. Test each with ``test_<system>.py``. For example, connect a motor to the raspberry pi, and run ``test_motor.py``.

2. Once your systems have been tested and plugged in, run ``main.py`` where ``brain_type = 'human_driver'`` to test drive your vehicle.

3. Design the logic for your autonomous vehicle by writing instructitons into your autonomous brain's ``logic()`` method.

4. Run ``main.py`` where ``brain_type = 'autonomous'`` to test your autonomous brain's functionality.


``main.py``
-----------

The main python script for running the vehicle. This script does the following:

1. Loads the ``src/config.json`` file

2. Initalize supporting classes

   * Initialize camera
   * Initialize distance sensors
   * Initialize LEDs
   * Initialize switches
   * Initialize vehicle

3. Initalize a brain instance, from your given ``brain_type``

4. Run the brain instance

Test Scripts
------------

Each of the test scripts below contains functionality used for testing each individual system. Run tests from your raspberry pi with ``python test_<system>.py``.

``test_camera.py``
^^^^^^^^^^^^^^^^^^

Assure that your camera is capturing data with this module. A successful camera setup on your raspberry pi should show an image array being printed in each loop.

``test_distance_sensor.py``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assure that your distance sensors are operating properly with this module. A successful setup enables a sensor to detect how far away an object is. Try putting your hand in front of the sensor and moving it closer and farther away.

``test_led.py``
^^^^^^^^^^^^^^^^^

Test out an LED's functionality by cycling its ``on()`` and ``off()`` methods.

``test_motor.py``
^^^^^^^^^^^^^^^^^

The H-Bridge and one motor must be connected to run this script. Test out the functionality of one motor as it cycles through various speeds and both directions.

``test_switch.py``
^^^^^^^^^^^^^^^^^^

Flip the switch on and off while executing this script. Note whether the print statements reflect the state of the switch.

``test_vehicle.py``
^^^^^^^^^^^^^^^^^^^

The H-Bridge and both motors must be connected to run this script. Cycles through various drive functions of the vehicle.


``src`` package
-----------

Modules to be imported by scripts in the ``HackIllinois/code`` directory

brains
^^^^^^

Contains modules that contain `Brain` classes, each with different functionality.

autonomous
""""""

The autonomous brain module. Designed to use information from sensors to make decisions on how to drive.

base
""""

The base brain module. Contains classes to be inherited by child modules.

human_driver
""""""""""""

The human_driver brain module. Uses keyboard input to steer the vehicle. Useful for testing purposes.

camera
^^^^^^

Module providing functionality on access the raspberry pi's camera module.

config.json
^^^^^^^^^^^

Pin layout and other configuration settings.

distance_sensor
^^^^^^^^^^^^^^^

Module providing functionality for ultrasonic distance sensors.

motor
^^^^^

Module providing functionality for controlling an individual motor's speed and direction.

params
^^^^^^

Module containing other Python variables not contained in ``config.json``

vehicle
^^^^^^^

Module containing functionality for controlling a vehicle, that is, a left and a right motor.



.. autosummary::
   :toctree: _autosummary

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
