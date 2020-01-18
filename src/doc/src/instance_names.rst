Instance Names
==============
:py:class:`LMIInstanceName` is a object, which holds a set of primary keys and
their values. This type of object exactly identifies an instance.

.. _instance_names_key_properties:

Key properties
--------------
To get a list of key properties, see following example:

.. code-block:: python

    > instance_name.print_key_properties()
    ...
    > instance_name.key_properties()
    ...
    > instance_name.SomeKeyProperty
    ...
    >

.. _instance_names_conversion:

Conversion to a LMIInstance
---------------------------
This type of object may be returned from a method call. Each instance name can
be converted into the instance, see next example:

.. code-block:: python

    > instance = instance_name.to_instance()
    >

Useful Properties
-----------------

Following part describes :py:class:`LMIInstanceName` useful properties.

Class name
^^^^^^^^^^
To get a class name of the instance name, execute:

.. code-block:: python

    > instance_name.classname
    >

Path
^^^^
To get a path string from the instance name, execute following:

.. code-block:: python

    > instance_name.path
    ...
    >
