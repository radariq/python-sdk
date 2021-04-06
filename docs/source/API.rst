.. module:: radariq


RadarIQ Class
=============
.. autoclass:: RadarIQ
  :members:


Constants
=========

Capture Modes
#############

    The RadarIQ-M1 sensor has the option to run in two modes.

    .. data:: MODE_POINT_CLOUD

        Run the RadarIQ sensor is Point Cloud mode.

    .. data:: MODE_OBJECT_TRACKING

        Run the RadarIQ sensor in Object Tracking mode.

Moving filter
#############

    Filter objects by moving/stationary.

    .. data:: MOVING_BOTH

        Return both moving and stationary objects

    .. data:: MOVING_OBJECTS_ONLY

        Return only objects which move (which includes fine movements)

Reset codes
###########
    Codes for resetting the sensor.

    .. data:: RESET_REBOOT

        Reboot the sensor.

    .. data:: RESET_FACTORY_SETTINGS

        Reset the sensor to the factory defaults.

Point density options
######################

    Adjusts the density of the Point Cloud.

    .. warning:: Point Cloud mode only.

    .. data:: DENSITY_NORMAL

        Do not perform any aggregation of point.

    .. data:: DENSITY_DENSE

        Perform some aggregation of points. Note: Aggregation may introduce a small
        amount of lag in data capture.

    .. data:: DENSITY_VERY_DENSE

        Perform agressive aggregation of points. Note: Aggregation may introduce a small
        amount of lag in data capture.

Data output formats
###################

    Output formats describe the way the :meth:`get_data` method returns data.

    .. data:: OUTPUT_LIST

        When set, :meth:`get_data` returns a list of dictionaries.
        See :meth:`get_data` for further details.

    .. data:: OUTPUT_NUMPY

        When set, :meth:`get_data` returns a an ndarray of values.
        See :meth:`get_data` for further details.

Certainty values
################

    Certainty values describe the amount of pre-processing done on the sensor.
    This involves: Threshold for detections,
    0 = Least certain

    1 = Least certain

    2 = Least certain

    3 = Least certain

    4 = Least certain

    5 = Least certain

    6 = Least certain

    7 = Least certain

    8 = Least certain

    9 = Most certain
    @todo explain what each means


Object type modes
#################

    These modes optimise the sensor for specific types of objects.

    .. warning:: Object tracking mode only.

    .. data:: OBJECT_TYPE_DOG

        Dog or other similar sized object.

    .. data:: OBJECT_TYPE_PERSON

        Person walking or other similar object.

    .. data:: OBJECT_TYPE_CYCLIST

        Person on a bicycle or other similar object.

    .. data:: OBJECT_TYPE_SLOW_VEHICLE

        Vehicle traveling less than 30km/h or other similar object.

    .. data:: OBJECT_TYPE_FAST_VEHICLE

        Vehicle traveling greater than 30km/h or other similar object.

