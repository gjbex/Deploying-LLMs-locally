.. _build-a-container:

#################
Build a Container
#################

.. _sec:build_a_container:

The ``build`` command is the "Swiss army knife" of container creation.
You can use it to download and assemble existing containers from
external resources like `Docker Hub <https://hub.docker.com/>`_ and other OCI registries.
You can use it to convert containers
between the formats supported by {Project}. And you can use it in
conjunction with a :ref:`{Project} definition <definition-files>`
file to create a container from scratch and customized it to fit your
needs.

********
Overview
********

The ``build`` command accepts a target as input and produces a container
as output.

The type of target given determines the method that ``build`` will use
to create the container. It can be one of the following:

-  URI beginning with **docker://** to build from Docker Hub
-  URI beginning with **oras://** to build from an OCI registry that supports OCI Artifacts
-  URI beginning with **library://** to build from the Container Library
-  URI beginning with **shub://** to build from Singularity Hub
-  path to an **existing container** on your local machine
-  path to a **directory** to build from a sandbox
-  path to a :ref:`{Project} definition file <definition-files>`

``build`` can produce containers in two different formats, which can be
specified as follows:

-  a compressed read-only **Singularity Image File (SIF)** format,
   suitable for production *(default)*
-  a writable **(ch)root directory** called a sandbox, for interactive
   development ( ``--sandbox`` option)

Because ``build`` can accept an existing container as a target and
create a container in either supported format, you can use it to convert
existing containers from one format to another.


.. note::
   {Project} leverages the user namespace kernel feature to give the illusion 
   of elevated privileges while building containers. On some systems, the user 
   namespace may be incompletely configured for individual users. In this case, 
   {Project} may bind mount the ``fakeroot`` program from the host into the 
   container during the build, and this might fail in some containers with 
   mismatching libraries. See the :ref:`fakeroot documentation <fakeroot>` for 
   more details.

*************************************************
Downloading an existing container from Docker Hub
*************************************************

You can use ``build`` to download layers from Docker Hub and assemble
them into {Project} containers.

.. code::

   $ {command} build alpine.sif docker://alpine

*************************************************************
Downloading an existing container from a Library API Registry
*************************************************************

If you have set up a library remote endpoint as described in
:ref:`Managing Remote Endpoints <sec:managing-remote-endpoints>`,
you can use the build command to download a container from the Container
Library.

.. code::

   $ {command} build lolcow.sif library://lolcow

The first argument (``lolcow.sif``) specifies the path and name for your
container. The second argument (``library://lolcow``) gives the
Container Library URI from which to download. By default, the container
will be converted to a compressed, read-only SIF. If you want your
container in a writable format, use the ``--sandbox`` option.

.. _create_a_writable_container:

*******************************************
Creating writable ``--sandbox`` directories
*******************************************

If you want to create a container within a writable directory (called a
*sandbox*) you can do so with the ``--sandbox`` option.

.. code::

   $ {command} build --sandbox alpine/ docker://alpine

The resulting directory operates just like a container in a SIF file. To
make persistent changes within the sandbox container, use the
``--writable`` flag when you invoke your container.

.. code::

   $ {command} shell --writable alpine/

************************************************
Converting containers from one format to another
************************************************

If you already have a container saved locally, you can use it as a
target to build a new container. This allows you convert containers from
one format to another. For example, if you had a sandbox container
called ``development/`` and you wanted to convert it to a SIF container
called ``production.sif``, you could do so as follows:

.. code::

   $ {command} build production.sif development/

Use care when converting a sandbox directory to the default SIF format.
If changes were made to the writable container before conversion, there
is no record of those changes in the {Project} definition file,
which compromises the reproducibility of your container. It is therefore
preferable to build production containers directly from {aProject}
definition file instead.

*******************************************************
Building containers from {Project} definition files
*******************************************************

{Project} definition files are the most powerful type of target when
building a container. For detailed information on writing {Project}
definition files, please see the :doc:`Container Definitions
documentation <definition_files>`. Suppose you already have the
following container definition file called, ``lolcow.def``, and you want
to use it to build a SIF container:

.. code:: {command}

   Bootstrap: docker
   From: ubuntu:20.04

   %post
       apt-get -y update
       apt-get -y install cowsay lolcat

   %environment
       export LC_ALL=C
       export PATH=/usr/games:$PATH

   %runscript
       date | cowsay | lolcat

You can do so with the following command.

.. code::

   $ {command} build lolcow.sif lolcow.def

.. note::

   Beware that it is possible to build an image on a host and have the
   image not work on a different host. This could be because of the
   default compressor supported by the host. For example, when building
   an image on a host in which the default compressor is ``xz`` and then
   trying to run that image on a node where the only
   compressor available is ``gzip``.

*****************************
Building encrypted containers
*****************************

With {Project} it is possible to build and run encrypted
containers. Encrypted containers are decrypted at runtime entirely in memory,
meaning that no intermediate decrypted data is ever written to disk. See
:ref:`encrypted containers <encryption>` for more details.

*************
Build options
*************

``--build-arg``
===============

Specifies values of :ref:`defined template variables <arguments>` in the 
definition file. Values passed via ``--build-arg`` follow the form of 
``variable=value``. Multiple ``--build-arg`` options are acceptable for build command.

``--build-arg-file``
====================

Similar to ``--build-arg`` but specifiles values of defined template variables 
via a file, which contains multiple ``variable=value`` entries. 

``--warn-unused-build-args``
============================

By default, when users provide unused variables to the build process, fatal
errors will return. This option makes the build process show warnings instead of 
returning fatal errors.

``--encrypt``
=============

Specifies that {Project} should use a secret saved in either the
``{ENVPREFIX}_ENCRYPTION_PASSPHRASE`` or
``{ENVPREFIX}_ENCRYPTION_PEM_PATH`` environment variable to build an
encrypted container. See :ref:`encrypted containers <encryption>` for
more details.

``--fakeroot``
==============

Gives users a way to build containers without root privileges.
This option is implied when an unprivileged user invokes build
on a definition file.
See :ref:`the fakeroot feature <fakeroot>` for details.

``--force``
===========

The ``--force`` option will delete and overwrite an existing
{Project} image without presenting the normal interactive
confirmation prompt.

``--json``
==========

The ``--json`` option will force {Project} to interpret a given
definition file as JSON.

``--library``
=============

This command allows you to set a different image library. Look
:ref:`here <library_api_registries>` for more information.

``--notest``
============

If you don't want to run the ``%test`` section during the container
build, you can skip it using the ``--notest`` option. For instance, you
might be building a container intended to run in a production
environment with GPUs, while your local build resource does not have
GPUs. You want to include a ``%test`` section that runs a short
validation, but you don't want your build to exit with an error because
it cannot find a GPU on your system. In such a scenario, passing the
``--notest`` flag would be appropriate.

``--passphrase``
================

This flag allows you to pass a plaintext passphrase to encrypt the
container filesystem at build time. See :ref:`encrypted containers
<encryption>` for more details.

``--pem-path``
==============

This flag allows you to pass the location of a public key to encrypt the
container file system at build time. See :ref:`encrypted containers
<encryption>` for more details.

``--sandbox``
=============

Build a sandbox (container in a directory) instead of the default SIF
format.

``--section``
=============

Instead of running the entire definition file, only run a specific
section or sections. This option accepts a comma-delimited string of
definition file sections. Acceptable arguments include ``all``, ``none``
or any combination of the following: ``setup``, ``post``, ``files``,
``environment``, ``test``, ``labels``.

Under normal build conditions, the {Project} definition file is
saved into a container's metadata so that there is a record of how the
container was built. The ``--section`` option may render this metadata
inaccurate, compromising reproducibility, and should therefore be used
with care.

``--update``
============

You can build into the same sandbox container multiple times (though the
results may be unpredictable, and under most circumstances, it is
preferable to delete your container and start from scratch).

By default, if you build into an existing sandbox container, the
``build`` command will prompt you to decide whether or not to overwrite
existing container data. Instead of this behavior, you can use the
``--update`` option to build *into* an existing container. This will
cause {Project} to skip the definition-file's header, and build any
sections that are in the definition file into the existing container.

The ``--update`` option is only valid when used with sandbox containers.

``--nv``
========

This flag allows you to mount the Nvidia CUDA libraries from your host
environment into your build environment. Libraries are mounted during
the execution of ``post`` and ``test`` sections.

.. note::

    This option can't be set via the environment variable `{ENVPREFIX}_NV`.
    {Project} will attempt to bind binaries listed in {ENVPREFIX}_CONFDIR/nvliblist.conf,
    if the mount destination doesn't exist inside the container, they are ignored.

``--nvccli``
============

Experimental option to use Nvidia's ``nvidia-container-cli`` for GPU setup.
See more details in the :ref:`GPU Support<gpu>` section.

``--rocm``
==========

This flag allows you to mount the AMD Rocm libraries from your host
environment into your build environment. Libraries are mounted during
the execution of ``post`` and ``test`` sections.

.. note::

    This option can't be set via the environment variable `{ENVPREFIX}_ROCM`.
    {Project} will attempt to bind binaries listed in `{ENVPREFIX}_CONFDIR/rocmliblist.conf`,
    if the mount destination doesn't exist inside the container, they are ignored.

``--bind``
==========

This flag allows you to mount a directory, file or image during build.
It works the same way as ``--bind`` for the ``shell``, ``exec`` and
``run`` subcommands of {Project}, and can be specified multiple
times. See :ref:`user defined bind paths <user-defined-bind-paths>`.
Bind mounts occur during the execution of ``post`` and ``test``
sections.

.. note::

    This option can't be set via the environment variables `{ENVPREFIX}_BIND` and `{ENVPREFIX}_BINDPATH`

**Beware that the mount points must exist in the built image** prior to executing ``post`` and ``test``.
So if you want to bind ``--bind /example`` and it doesn't exist in the bootstrap image, you have to
workaround that by adding a ``setup`` section:

.. code-block:: none

    %setup
      mkdir ${ENVPREFIX}_ROOTFS/example

.. note::

    Binding your directory to `/mnt` is another workaround, as this directory is often present in
    distribution images and is intended for that purpose, you could avoid the directory creation
    in the definition file.

``--writable-tmpfs``
====================

This flag will run the ``%test`` section of the build with a writable
``tmpfs`` overlay filesystem in place. This allows the tests to create
files, which will be discarded at the end of the build. Other portions
of the build do not use this temporary filesystem.

*****************
More Build topics
*****************

-  If you want to **customize the cache location** (where Docker layers
   are downloaded on your system), specify Docker credentials, or apply
   other custom tweaks to your build environment, see :ref:`build
   environment <build-environment>`.

-  If you want to make internally **modular containers**, check out the
   Getting Started guide `here <https://sci-f.github.io/tutorials>`_.

-  If you want to **build a container with an encrypted file system**
   consult the {Project} documentation on encryption :ref:`here
   <encryption>`.
