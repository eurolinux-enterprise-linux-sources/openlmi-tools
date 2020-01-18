Builtin features
================
This section describes built-in features of the LMIShell.

Configuration file
------------------
The LMIShell has a tiny configuration file with location ``~/.lmishellrc``.
In configuration file, you can set these properties:

.. code-block:: python

    # location of the history used by interactive mode
    history_file = "~/.lmishell_history"
    # length of history file, -1 for unlimited
    history_length = -1
    # default value for cache usage
    use_cache = True
    # default value for exceptions
    use_exceptions = False

Inspecting a script
-------------------
If you want to inspect a script after it has been interpreted by the LMIShell,
run this:

.. code-block:: shell

    $ lmishell -i some_script.lmi
    # some stuff done
    >

**NOTE:** Prefered extension of LMIShell's scripts is ``.lmi``.

LMI Is Instance
---------------
LMIShell is able to verify, if a :py:class:`LMIInstance` or
:py:class:`LMIInstanceName` object passed to :py:func:`.lmi_isinstance` is a
instance of :py:class:`LMIClass`.

The function is similar to python's :py:func:`.isinstance`:

.. code-block:: python

    > lmi_isinstance(inst, cls)
    True/False
    >

LMI Associators
---------------
LMIShell can speed up associated objects' traversal by manual joining, instead
of calling :py:meth:`.LMIInstance.associators`. The call needs to get a list of
**association** classes, for which the referenced objects will be joined. The
list must contain objects of :py:class:`LMIClass`.

See following example:

.. code-block:: python

    > associators = lmi_associators(list_of_association_classes)
    >
