.. _registry:

####################
OCI Image Registries
####################

It is common for users of {Project} to use `OCI
<https://opencontainers.org/>`__ registries as sources for their container
images. Some registries require credentials to access certain images or even the
registry itself. One method is to supply credentials for each command or set
environment variables to contain the credentials for a single registry. See
:ref:`Authentication via Interactive Login
<sec:authentication_via_docker_login>` and :ref:`Authentication via Environment
Variables <sec:authentication_via_environment_variables>`.

Alternatively, users can supply credentials on a per-registry basis with the ``registry`` command.

Users can login to an OCI registry with the ``registry login`` command by
specifying a ``docker://`` prefix to the registry hostname:

.. code:: console

   $ {command} registry login --username myuser docker://docker.com
   Password / Token:
   INFO:    Token stored in /home/myuser/.apptainer/remote.yaml

   $ {command} registry list

   URI                  SECURE?
   docker://docker.com  ✓

{Project} will automatically supply the configured credentials when
interacting with DockerHub. The checkmark in the ``SECURE?`` column indicates
that {Project} will use TLS when communicating with the registry.

A user can be logged-in to multiple OCI registries at the same time:

.. code:: console

   $ {command} registry login --username myuser docker://registry.example.com
   Password / Token:
   INFO:    Token stored in /home/myuser/.apptainer/remote.yaml

   $ {command} registry list

   URI                            SECURE?
   docker://docker.com            ✓
   docker://registry.example.com  ✓

{Project} will supply the correct credentials for the registry based on the
hostname used, whenever one of the following commands is used with a
``docker://`` or ``oras://`` URI:

`pull
<cli/{command}_pull.html>`__,
`push
<cli/{command}_push.html>`__,
`build
<cli/{command}_build.html>`__,
`exec
<cli/{command}_exec.html>`__,
`shell
<cli/{command}_shell.html>`__,
`run
<cli/{command}_run.html>`__,
`instance
<cli/{command}_instance.html>`__.

.. note::

   It is important for users to be aware that the ``registry login`` command
   will store the supplied credentials or tokens unencrypted in their home
   directory.

