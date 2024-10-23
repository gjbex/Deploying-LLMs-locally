.. _bind-paths-and-mounts:

#####################
Bind Paths and Mounts
#####################

.. _sec:bindpaths:

Unless `disabled by the system administrator
<{admindocs}/configfiles.html#bind-mount-management>`_,
{Project} allows you to map directories on your host system to
directories within your container using bind mounts. This allows you to
read and write data on the host system with ease.

********
Overview
********

When {Project} 'swaps' the host operating system for the one inside
your container, the host file systems becomes inaccessible. However, you
may want to read and write files on the host system from within the
container. To enable this functionality, {Project} will bind
directories back into the container via two primary methods:
system-defined bind paths and user-defined bind paths.

*************************
System-defined bind paths
*************************

The system administrator has the ability to define which bind paths will be
included automatically inside each container. Some bind paths are derived (e.g.
a user's home directory), and some are statically defined with a ``bind path``
entry in the {Project} configuration.

In the default configuration, the default bind mounts are:

- The user's home directory (``$HOME``)
- The current working directory (``CWD``), unless its path contains symlinks
  resolving to different locations on the host vs inside the container.
- ``/dev``
- ``/etc/hosts``
- ``/etc/localtime`` 
- ``/proc``
- ``/sys``
- ``/tmp``
- ``/var/tmp``

Additionally, customized system configuration files ``/etc/resolv.conf``,
``/etc/group``, and ``/etc/passwd`` are mounted into the container. These are
adapted at container startup to match the requested configuration of the
container.

Disabling System Binds
======================

The ``--no-mount`` flag allows specific system mounts to be disabled, even if
they are set in the ``{command}.conf`` configuration file by the
administrator.

For example, if {Project} has been configured with ``mount hostfs =
yes`` then every filesystem on the host will be bind mounted to the
container by default. If, e.g. a ``/project`` filesystem on your host
conflicts with a ``/project`` directory in the container you are
running, you can disable the ``hostfs`` binds:

.. code:: console

   $ {command} run --no-mount hostfs mycontainer.sif

Multiple system mounts can be disabled by specifying them separated by commas:

.. code:: console

   $ {command} run --no-mount tmp,sys,dev mycontainer.sif

When the administrator has configured custom ``bind path`` entries in
``{command}.conf``, to mount specific paths into the container by default, you
can disable them individually. To do this, specify the path(s) to disable with
the ``--no-mount`` flag. For example, if the adminstrator has configured
``{command}.conf`` to always mount ``/data2``. you can disable this with
``--no-mount /data2``:

.. code:: console

   $ {command} run --no-mount /data2 mycontainer.sif

To disable all ``bind path`` entries set in ``{command}.conf``, use
``--no-mount bind-paths``:

.. code:: console

   $ {command} run --no-mount bind-paths mycontainer.sif


.. _user-defined-bind-paths:

***********************
User-defined bind paths
***********************

Unless the system administrator has `disabled user control of binds
<{admindocs}/configfiles.html#bind-mount-management>`_,
you will be able to request your own bind paths within your container.

The {Project} action commands (``run``, ``exec``, ``shell``, and
``instance start``) will accept the ``--bind/-B`` command-line option to
specify bind paths, and will also honor the ``${ENVPREFIX}_BIND`` and
``${ENVPREFIX}_BINDPATH`` environment variables (in that order).
The argument for this
option is a comma-delimited string of bind path specifications in the
format ``src[:dest[:opts]]``, where ``src`` and ``dest`` are paths
outside and inside of the container respectively. If ``dest`` is not
given, it is set equal to ``src``. Mount options (``opts``) may be
specified as ``ro`` (read-only) or ``rw`` (read/write, which is the
default). The ``--bind/-B`` option can be specified multiple times, or a
comma-delimited string of bind path specifications can be used.

{Project} also has a ``--mount`` flag, which provides a
longer-form method of specifying binds in ``--mount
type=bind,src=<source>,dst=<destination>[,<option>]...`` format. This is
compatible with the ``--mount`` syntax for binds in Docker and other OCI
runtimes.

``--bind`` Examples
===================

Here's an example of using the ``--bind`` option and binding ``/data``
on the host to ``/mnt`` in the container (``/mnt`` does not need to
already exist in the container):

.. code::

   $ ls /data
   bar  foo

   $ {command} exec --bind /data:/mnt my_container.sif ls /mnt
   bar  foo

You can bind multiple directories in a single command with this syntax:

.. code::

   $ {command} shell --bind /opt,/data:/mnt my_container.sif

This will bind ``/opt`` on the host to ``/opt`` in the container and
``/data`` on the host to ``/mnt`` in the container.

Using the environment variable instead of the command line argument,
this would be:

.. code::

   $ export {ENVPREFIX}_BINDPATH="/opt,/data:/mnt"

   $ {command} shell my_container.sif

Using the environment variable ``${ENVPREFIX}_BINDPATH``, you can bind paths
even when you are running your container as an executable file with a
runscript. If you bind many directories into your {Project}
containers and they don't change, you could even benefit by setting this
variable in your ``.bashrc`` file.

.. note::

   Inside {aProject} container all the paths that were bound in are set
   in the ``${ENVPREFIX}_BIND`` variable.  That means they will be
   automatically bound in again by default if another {command} command is
   run nested inside the first container.  You can change that variable
   if you choose before that point, but if you want to avoid interfering
   with nested containers it's better to use ``${ENVPREFIX}_BINDPATH``.

``--mount`` Examples
====================

The ``--mount`` flag takes a mount specification in the format
``type=bind,src=<source>,dst=<dest>``. Additional options can be
specified, comma delimited.

{Project} only supports the ``bind`` type for ``--mount``, and will
infer ``type=bind`` if it is not provided.

``src`` or ``source`` can be used interchangeably. ``dst``,
``destination``, or ``target`` are also equivalent.

To mount ``data`` on the host to ``/mnt`` inside the container:

.. code::

   $ {command} exec \
       --mount type=bind,src=/data,dst=/mnt \
       my_container.sif ls /mnt
   bar  foo

To mount the same directory read-only in the container, add the ``ro``
option:

.. code::

   $ {command} exec \
       --mount type=bind,source=/data,dest=/mnt,ro \
       my_container.sif touch /mnt/test
   touch: cannot touch '/mnt/test': Permission denied

You can bind multiple directories in a single command with multiple
``--mount`` flags:

.. code::

   $ {command} shell --mount type=bind,src=/opt,dst=/opt \
                       --mount type=bind,src=/data,dst=/data \
                       my_container.sif

This will bind ``/opt`` on the host to ``/opt`` in the container and
``/data`` on the host to ``/mnt`` in the container.

The mount string can be quoted and escaped according to CSV rules,
wrapping each field in double quotes if necessary characters.
``--mount`` allows bind mounting paths that are not possible with the
``--bind`` flag. For example:

.. code::

   # Mount a path containing ':' (not possible with --bind)
   $ {command} run \
       --mount type=bind,src=/my:path,dst=/mnt \
       mycontainer.sif

   # Mount a path containing a ','
   $ {command} run \
       --mount type=bind,"src=/comma,dir",dst=/mnt \
       mycontainer.sif

Mount specifications are also read from then environment variable
``${ENVPREFIX}_MOUNT``. Multiple bind mounts set via this environment
variable should be separated by newlines (``\n``).

Using ``--bind`` or ``--mount`` with the ``--writable`` flag
============================================================

To mount a bind path inside the container, a *bind point* must be
defined within the container. The bind point is a directory or file within the
container that {Project} can use as a destination to bind a
directory or file from the host system.
Under most circumstances, {Project} will automatically create any missing
bind points within the container using an overlay.

However, binding paths to non-existent points within the container can
result in unexpected behavior when used in conjunction with the
``--writable`` flag, and is therefore disallowed. If you need to specify
bind paths in combination with the ``--writable`` flag, please ensure
that the appropriate bind points exist within the container. If they do
not already exist, it will be necessary to modify the container and
create them.

Using ``--no-home`` and ``--containall`` flags
==============================================

``--no-home``
-------------

When starting a container, {Project} allows you to mount your current
working directory (``CWD``) without mounting your host ``$HOME`` directory by
using the ``--no-home`` flag. This is equivalent to ``--no-mount home``:

.. code::

   $ {command} shell --no-home my_container.sif

   -or-

   $ {command} shell --no-mount home my_container.sif

Disabling the mount of ``$HOME`` may be useful if your container image has files
at ``$HOME``, which would otherwise be hidden by the bind mount from the host.

.. note::

  If your current working directory is under ``$HOME``, and you do not want to
  mount it, you will need to disable both ``cwd`` and ``home`` mounts:

  .. code::

    $ {command} shell --no-mount home,cwd my_container.sif

``--contain`` / ``--containall``
--------------------------------

When using the ``--contain`` / ``--containall`` (or ``-c`` / ``-C`` for short)
flags, ``$HOME`` from the host is not mounted, and an in-memory temporary
directory is created at the ``$HOME`` point inside the container instead. An
in-memory temporary directory is also used for ``/tmp`` and ``/var/tmp`` inside
the container.

If the container image includes files within ``$HOME``, the mounted temporary
directory will hide them unless you also specify ``--no-home`` or ``--no-mount
home``:

.. code::

   $ {command} shell --containall my_container.sif
   {Project}> ls -lah $HOME
   total 4K
   drwxr-xr-x    2 user group      60 Sep  1 11:45 .
   drwxr-xr-x    1 user group      60 Sep  1 11:44 ..

   $ {command} shell --containall --no-home my_container.sif
   {Project}> ls -lah $HOME
   total 52K
   drwxr-xr-x    2 user group        60 Sep  1 11:45 .
   drwxr-xr-x    1 user group        60 Sep  1 11:44 ..
   drwxr-xr-x    1 user group     38672 Sep  1 11:44 mydata.csv
   drwxr-xr-x    1 user group     14235 Sep  1 11:44 myimage.jpg

***********
FUSE mounts
***********

Filesystem in Userspace (FUSE) is an interface to allow filesystems to
be mounted using code that runs in userspace, rather than in the Linux
Kernel. Unprivileged (non-root) users can mount filesystems that have
FUSE drivers. For example, the ``fuse-sshfs`` package allows you to
mount a remote computer's filesystem to your local host, over ssh:

.. code::

   $ mount.fuse sshfs#ythel:/home/dave other_host/

   # Now mounted to my local machine:
   $ ythel:/home/dave on /home/dave/other_host type fuse.sshfs (rw,nosuid,nodev,relatime,user_id=1000,group_id=1000)

{Project} has a ``--fusemount`` option, which allows
you to directly expose FUSE filesystems inside a container. The FUSE
command / driver that mounts a particular type of filesystem can be
located on the host, or in the container.

Requirements
============

The FUSE command invoked with the ``--fusemount`` option
*must* be based on libfuse3 3.3.0 or greater to work
correctly with {Project}. Older versions do not support the way in
which the {Project} runtime passes a pre-mounted file descriptor
into the container.

If you are using an older distribution that provides FUSE commands such
as ``sshfs`` based on FUSE 2 then you can install FUSE 3 versions of the
commands you need inside your container.

FUSE mount definitions
======================

A fusemount definition for {Project} consists of 3 parts:

.. code::

   --fusemount <type>:<fuse command> <container mountpoint>

-  **type** specifies how and where the FUSE mount will be run. The
   options are:

   -  ``host`` - use a FUSE command on the host, to mount a
      filesystem into the container, with the fuse process attached.

   -  ``container`` - use a FUSE command inside the container, to mount a
      filesystem into the container, with the fuse process attached.

   -  ``host-daemon`` - use a FUSE command on the host, to mount a
      filesystem into the container, with the fuse process detached.

   -  ``container-daemon`` - use a FUSE command inside the container, to
      mount a filesystem into the container, with the fuse process
      detached.

-  **fuse command** specifies the name of the executable that implements
   the FUSE mount, and any arguments. E.g. ``sshfs server:over-there/``
   for mounting a remote filesystem over SSH, where the remote source is
   ``over-there/`` in my home directory on the machine called
   ``server``.

-  **container mountpoint** is an *absolute path* at which the FUSE
   filesystem will be mounted in the container.

FUSE mount with a host executable
=================================

To use a FUSE ``sshfs`` mount in a container, where the ``fuse-sshfs``
package has been installed on my host, I run with the ``host`` mount
type:

.. code::

   $ {command} run --fusemount "host:sshfs server:/ /server" docker://ubuntu
   {Project}> cat /etc/hostname
   localhost.localdomain
   {Project}> cat /server/etc/hostname
   server

FUSE mount with a container executable
======================================

If the FUSE driver / command that you want to use for the mount has been
added to your container, you can use the ``container`` mount type:

.. code::

   $ {command} run --fusemount "container:sshfs server:/ /server" sshfs.sif
   {Project}> cat /etc/hostname
   localhost.localdomain
   {Project}> cat /server/etc/hostname
   server

************
Image Mounts
************

In {Project} you can mount a directory contained in an
image file into a container. This may be useful if you want to
distribute directories containing a large number of data files as a
single image file.

You can mount from image files in ext3 format, squashfs format, or SIF
format.

The ext3 image file format allows you to mount it into the container
read/write and make changes, while the other formats are read-only. Note
that you can only use a read/write image in a single container. You
cannot mount it to multiple container runs at the same time.

To mount a directory from an image file, use the ``-B/--bind`` option
and specify the bind in the format:

.. code::

   -B <image-file>:<dest>:image-src=<source>

Alternatively use the ``--mount`` option, and specify the bind in the
format:

.. code::

   --mount type=bind,src=<image-file>,dst=<dest>,image-src=<source>

This will bind the ``<source>`` path inside ``<image-file>`` to
``<dest>`` in the container.

If you do not add ``:image-src=<source>`` to your bind specification,
then the ``<image-file>`` itself will be bound to ``<dest>`` instead.

Ext3 Image Files
================

If you have a directory called ``inputs/`` that holds data files you
wish to distribute in an image file that allows read/write:

.. code:: sh

   # Create an image file 'inputs.img' of size 100MB and put the
   # files inputs/ into it's root directory
   $ mkfs.ext3 -d inputs/ inputs.img 100M
   mke2fs 1.45.6 (20-Mar-2020)
   Creating regular file inputs.img
   Creating filesystem with 102400 1k blocks and 25688 inodes
   Filesystem UUID: e23c29c9-7a49-4b82-89bf-2faf36b5a781
   Superblock backups stored on blocks:
       8193, 24577, 40961, 57345, 73729

   Allocating group tables: done
   Writing inode tables: done
   Creating journal (4096 blocks): done
   Copying files into the device: done
   Writing superblocks and filesystem accounting information: done

   # Run {Project}, mounting my input data to '/input-data' in
   # the container.
   $ {command} run -B inputs.img:/input-data:image-src=/ mycontainer.sif
   {Project}> ls /input-data
   1           3           5           7           9
   2           4           6           8           lost+found

   # Or with --mount instead of -B
   $ {command} run \
       --mount type=bind,src=inputs.img,dst=/input-data,image-src=/ \
       mycontainer.sif

SquashFS Image Files
====================

If you have a directory called ``inputs/`` that holds data files you
wish to distribute in an image file that is read-only, and compressed,
then the squashfs format is appropriate:

.. code:: sh

   # Create an image file 'inputs.squashfs' and put the files from
   # inputs/ into it's root directory
   $ mksquashfs inputs/ inputs.squashfs
   Parallel mksquashfs: Using 16 processors
   Creating 4.0 filesystem on inputs.squashfs, block size 131072.
   ...

   # Run {Project}, mounting my input data to '/input-data' in
   # the container.
   $ {command} run -B inputs.squashfs:/input-data:image-src=/ mycontainer.sif
   {Project}> ls /input-data/
   1  2  3  4  5  6  7  8  9

   # Or with --mount instead of -B
   $ {command} run \
       --mount type=bind,src=src-inputs.squashfs,dst=/input-data,image-src=/ \
       mycontainer.sif

SIF Image Files
===============

Advanced users may wish to create a standalone SIF image, which contains
an ``ext3`` or ``squashfs`` data partition holding files, by using the
``apptainer sif`` commands similarly to the :ref:`persistent overlays
instructions <overlay-sif>`:

.. code:: console

   # Create a new empty SIF file
   $ {command} sif new inputs.sif

   # Add the squashfs data image from above to the SIF
   $ {command} sif add --datatype 4 --partarch 2 --partfs 1 --parttype 3 inputs.sif inputs.squashfs

   # Run {Project}, binding data from the SIF file
   $ {command} run -B inputs.sif:/input-data:image-src=/ mycontainer.sif
   {Project}> ls /input-data
   1  2  3  4  5  6  7  8  9

   # Or with --mount instead of -B
   $ {command} run \
       --mount type=bind,src=inputs.sif,dst=/input-data,image-src=/ \
       mycontainer.sif

If your bind source is a SIF then {Project} will bind from the first
data partition in the SIF, or you may specify an alternative descriptor
by ID with the additional option ``id=n``, where n is the descriptor ID.
