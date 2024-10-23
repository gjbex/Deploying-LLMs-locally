.. _singularity_compatibility:

#########################
Singularity Compatibility
#########################

Since the community decided to `move the project into the Linux Foundation
<https://apptainer.org/news/community-announcement-20211130>`_ with the
constraint of a name change to the project, it has been a goal of the
project to minimize the impact to the user base. If you experience issues making
the move, please reach out to the `community <https://apptainer.org/help>`_ so
we can help you!


***********************
SIF Image Compatibility
***********************

The {Project} project has decided to make no changes related to the project
renaming at the image format level. This means that default metadata within
SIF images and their filesystems will retain the ``singularity`` name without
change. This will ensure that containers built with {Project} will continue
to work with installations of Singularity.

This decision was made to ensure that users can continue to package their
applications and data with {Project} without concerns of image format
incompatibility when running in a different computing environment or
collaborating with colleagues that still use a Singularity installation.


.. _singularity_environment_variable_compatibility:

*************************************************
Singularity Prefixed Environment Variable Support
*************************************************

{Project} respects environment variables with the ``SINGULARITY_`` and
``SINGULARITYENV_`` prefixes when their respective ``{ENVPREFIX}_`` and
``{ENVPREFIX}ENV_`` counterparts are not set.


This first command does not use any environment variable compatibility behavior
as it is using the ``{ENVPREFIX}ENV_`` prefix to command {Project} to create an
environment variable in the container with the name ``FOO`` and the value
``BAR``:

.. code::

  $ {ENVPREFIX}ENV_FOO=BAR {command} exec docker://alpine env
  [...]
  FOO=BAR

We can see from the ``env`` output that this environment variable was properly
set inside the container.

Next we can use the ``SINGULARITYENV_`` prefix to do the same thing, but this
time we wil have the intended value be ``BAZ``:

.. code::

  $ SINGULARITYENV_FOO=BAZ {command} exec  docker://alpine env
  WARNING: DEPRECATED USAGE: Forwarding SINGULARITYENV_FOO as environment variable will not be supported in the future, use {ENVPREFIX}ENV_FOO instead
  [...]
  FOO=BAZ

Notice that we have a warning for ``DEPRECATED USAGE`` when doing so. This is
because a future version of {Project} may stop supporting environment variable
compatibility once it is past this current period of transition.

Finally, if both are set, the value set by the ``{ENVPREFIX}ENV_`` variable will
take priority over the ``SINGULARITYENV_`` variable.

.. code::

  $ {ENVPREFIX}ENV_FOO=BAR SINGULARITYENV_FOO=BAZ {command} exec iqube_latest.sif env
  WARNING: Skipping environment variable [SINGULARITYENV_FOO=BAZ], FOO is already overridden with different value [BAR]
  [...]
  FOO=BAR

In this case a warning is emitted to let the user know that two variables were
set to create the same environment variable in the container in case they were
unaware of one of them existing in their environment.


***************************
Singularity Command Symlink
***************************

With the same intention as the environment variable handling, {Project}
installations will include a symlink to the ``{command}`` binary named
``singularity``. This will allow existing tooling and scripts using the
``singularity`` command to continue to operate after a migration to {Project}
has taken place. Below is an example of running the ``version`` command using
either program name and getting the same output because we are running the same
underlying binary:

.. code::

  $ {command} --version
  {command} version {InstallationVersion}
  $ singularity --version
  {command} version {InstallationVersion}


**************************************
Automatic User Configuration Migration
**************************************

{Project} stores user configuration in files and directories under
``~/.{command}``. Invocation of the ``{command}`` command will automatically
trigger {Project} to create this directory, if it doesn't exist. In order to
ease the transition of users from Singularity to {Project}, {Project} will look
for a ``~/.singularity`` directory when the ``~/.{command}`` directory is being
created and will migrate user configuration files and keyrings automatically.
The following data will be migrated if it is found:

- Remote endpoint configurations
- OCI registry configurations stored in the Docker config format
- Singularity Public PGP keyring
- Singularity Private PGP keyring

Below we can see example output from when user configuration is being migrated:

.. code::

  $ {command} exec docker://alpine echo
  INFO:    Detected Singularity user configuration directory
  INFO:    Detected Singularity remote configuration, migrating...
  INFO:    Detected Singularity docker configuration, migrating...
  INFO:    Detected public Singularity pgp keyring, migrating...
  INFO:    Detected private Singularity pgp keyring, migrating...
  INFO:    Converting OCI blobs to SIF format
  INFO:    Starting build...
  [...]

We can also see that subsequent use of {Project} will not perform this
migration again:

.. code::

  $ {command} exec docker://alpine echo
  WARNING: /usr/local/etc/singularity/ exists, migration to {command} by system administrator is not complete
  INFO:    Using cached SIF image
  [...]


.. note::

  {Project} will not migrate cached container data such as OCI blobs and SIF
  images. User caches will need to be manually migrated or reconstructed through
  normal use of {Project}.

The default remote configuration has changed in {Project}, so if you did
not previously set any remotes and want to continue to use the previous
default for ``library://`` and/or pgp keys, see
:ref:`Restoring pre-{Project} library behavior <restoring_pre-{command}_library_behavior>`.
