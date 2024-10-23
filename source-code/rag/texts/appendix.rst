.. _appendix:

########
Appendix
########

..
   TODO oci & oci-archive along with http & https

.. _{command}-environment-variables:

*************************************
{Project}'s environment variables
*************************************

{Project} comes with some environment variables you can set or
modify depending on your needs. You can see them listed alphabetically
below with their respective functionality.

``A``
=====

#. **{ENVPREFIX}_ADD_CAPS**: To specify a list (comma separated string)
   of capabilities to be added. Default is an empty string.

#. **{ENVPREFIX}_ALL**: List all the users and groups capabilities.

#. **{ENVPREFIX}_ALLOW_SETUID**: To specify that setuid binaries should
   or not be allowed in the container. (root only) Default is set to
   false.

#. **{ENVPREFIX}_ALLOW_UNSIGNED**: Set to true to allow pushing unsigned SIF
   images to a ``library://`` destination. Default is false.

#. **{ENVPREFIX}_APP** and **{ENVPREFIX}_APPNAME**: Sets the name of an
   application to be run inside a container.

#. **{ENVPREFIX}_APPLY_CGROUPS**: Used to apply cgroups from an input
   file for container processes. (it requires root privileges)

#. **{ENVPREFIX}_PULL_ARCH**: Set the architecture
   (e.g. ``arm64``) of an image to pull from a ``library://`` or OCI source.
   Defaults to the host architecture.

``B``
=====

#. **{ENVPREFIX}_BIND** and **{ENVPREFIX}_BINDPATH**: Comma separated
   string ``source:<dest>`` list of paths to bind between the host and
   the container, applied in that order.
   Note that ``{ENVPREFIX}_BIND`` is also automatically set inside a
   container to list all the paths bound to it, so that by default all
   the same binds will be applied to nested {command} commands.

#. **{ENVPREFIX}_BLKIO_WEIGHT**: Specify a relative weight for block
   device access during contention. Range 10-1000. Default is 0 (disabled).

#. **{ENVPREFIX}_BLKIO_WEIGHT_DEVICE**: Specify a relative weight for
   block device access during contention on a specific device.
   Must be supplied in ``<device path>:weight`` format. Default is unset.

#. **{ENVPREFIX}_BOOT**: Set to false by default, considers if executing
   ``/sbin/init`` when container boots (root only).

``C``
=====

#. **{ENVPREFIX}_CACHEDIR**: Specifies the directory for image downloads
   to be cached in. See :ref:`sec:cache`.

#. **{ENVPREFIX}_CAP_GROUP**: Specify a group to modify when managing permitted
   capabilities with the ``capability`` command.

#. **{ENVPREFIX}_CAP_USER**: Specify a user to modify when managing permitted
   capabilities with the ``capability`` command.

#. **{ENVPREFIX}_CLEANENV**: Specifies if the environment should be
   cleaned or not before running the container. Default is set to false.

#. **{ENVPREFIX}_COMPAT**: Set to true to enable Docker/OCI compatibility mode.
   Equivalent to setting ``--containall --no-eval --no-init --no-umask
   --writable-tmpfs``. Default is false.

#. **{ENVPREFIX}_CONFIG_FILE**: Use a custom ``{command}.conf`` configuration
   file. Only supported for non-root users in non-setuid mode.

#. **{ENVPREFIX}_CONFIGDIR**: Specifies the directory to use for
   per-user configuration.  The default is ``$HOME/.{command}``.

#. **{ENVPREFIX}_CONTAIN**: To use minimal ``/dev`` and empty other
   directories (e.g. ``/tmp`` and ``$HOME``) instead of sharing
   filesystems from your host. Default is set to false.

#. **{ENVPREFIX}_CONTAINALL**: To contain not only file systems, but
   also PID, IPC, and environment. Default is set to false.

#. **{ENVPREFIX}_CONTAINLIBS**: Used to specify a string of file names
   (comma separated string) to bind to the ``/.singularity.d/libs``
   directory.

#. **{ENVPREFIX}_CPU_SHARES**: Specify a relative share of CPU time
   available to the container. Default is -1 (disabled).

#. **{ENVPREFIX}_CPUS**: Specify a fractional number of CPUs available
   to the container. Default is unset.

#. **{ENVPREFIX}_CPUSET_CPUS**: Specify a list or range of CPU cores
   available to the container. Default is unset.

#. **{ENVPREFIX}_CPUSET_MEMS**: Specify a list or range of memory nodes
   available to the container. Default is unset.

#. **{ENVPREFIX}_CWD** (deprecated **{ENVPREFIX}_PWD** and **{ENVPREFIX}_TARGET_PWD**): The initial
   working directory for payload process inside the container.

``D``
=====

#. **{ENVPREFIX}_DEBUG**: Enable debug output when set. Equivalent to ``-d /
   --debug``.

#. **{ENVPREFIX}_DEFFILE**: Shows the {Project} recipe that was used
   to generate the image.

#. **{ENVPREFIX}_DESC**: Contains a description of the capabilities.

#. **{ENVPREFIX}_DISABLE_CACHE**: To disable all caching of docker/oci,
   library, oras, etc. downloads and built SIFs. Default is set to
   false.

#. **{ENVPREFIX}_DNS**: A list of the DNS server addresses separated by
   commas to be added in ``resolv.conf``.

#. **{ENVPREFIX}_DOCKER_HOST**: Host address / socket to use when pulling images
   from a ``docker-daemon`` source. ``DOCKER_HOST`` without the
   ``{ENVPREFIX}_`` prefix is also accepted.

#. **{ENVPREFIX}_DOCKER_LOGIN**: To specify the interactive prompt for
   docker authentication.

#. **{ENVPREFIX}_DOCKER_PASSWORD**: To specify the password for docker
   authentication. ``DOCKER_PASSWORD`` without the ``{ENVPREFIX}_`` prefix is
   also accepted.

#. **{ENVPREFIX}_DOCKER_USERNAME**: To specify the username for docker
   authentication. ``DOCKER_USERNAME`` without the ``{ENVPREFIX}_`` prefix is
   also accepted.

#. **{ENVPREFIX}_DOWNLOAD_CONCURRENCY**: To specify how many concurrent streams
   when downloading (pulling) an image from cloud library.

#. **{ENVPREFIX}_DOWNLOAD_PART_SIZE**: To specify the size of each part (bytes)
   when concurrent downloads are enabled.

#. **{ENVPREFIX}_DOWNLOAD_BUFFER_SIZE**: To specify the transfer buffer size
   (bytes) when concurrent downloads are enabled.

#. **{ENVPREFIX}_DROP_CAPS**: To specify a list (comma separated string)
   of capabilities to be dropped. Default is an empty string.

``E``
=====

#. **{ENVPREFIX}_ENCRYPTION_PASSPHRASE**: Used to specify the plaintext
   passphrase to encrypt the container.

#. **{ENVPREFIX}_ENCRYPTION_PEM_DATA**: If it contains data from a public PEM 
   file, {Project} can use those data to encrypt a container. If it contains 
   data from a private PEM file, {Project} will try to use the data to run an 
   encrypted container. 

#. **{ENVPREFIX}_ENCRYPTION_PEM_PATH**: Used to specify the path of the
   file containing public or private key to encrypt the container in PEM
   format.

#. **{ENVPREFIX}_ENV_FILE**: Specify a file containing ``KEY=VAL`` environment
   variables that should be set in the container.

#. **{ENVPREFIX}_ENVIRONMENT**: Set during a build to the path to a file into
   which ``KEY=VAL`` environment variables can be added. The file is evaluated
   at container startup.

#. **{ENVPREFIX}ENV_\***: Allows you to transpose variables into the
   container at runtime. You can see more in detail how to use this
   variable in our :ref:`environment and metadata section
   <environment-and-metadata>`.

#. **{ENVPREFIX}ENV_APPEND_PATH**: Used to append directories to the end
   of the ``$PATH`` environment variable. You can see more in detail on
   how to use this variable in our :ref:`environment and metadata
   section <environment-and-metadata>`.

#. **{ENVPREFIX}ENV_PATH**: A specified path to override the ``$PATH``
   environment variable within the container. You can see more in detail
   on how to use this variable in our :ref:`environment and metadata
   section <environment-and-metadata>`.

#. **{ENVPREFIX}ENV_PREPEND_PATH**: Used to prepend directories to the
   beginning of ``$PATH`` environment variable. You can see more in
   detail on how to use this variable in our :ref:`environment and
   metadata section <environment-and-metadata>`.

``F``
=====

#. **{ENVPREFIX}_FAKEROOT**: Run or build a container using a user namespace
   with a root uid/gid mapping.

#. **{ENVPREFIX}_FIXPERMS**: Set to true to ensure owner has ``rwX`` permissions on
   all files in a container built from an OCI source.

#. **{ENVPREFIX}_FORCE**: Skip confirmation for destructive actions, e.g.
   overwriting a container image or killing an instance.

#. **{ENVPREFIX}_FUSESPEC**: A FUSE filesystem mount specification of the form
   '<type>:<fuse command> <mountpoint>', that will be mounted in the container.

``H``
=====

#. **{ENVPREFIX}_HELPFILE**: Specifies the runscript helpfile, if it
   exists.

#. **{ENVPREFIX}_HOME** : A home directory specification, it could be a
   source or destination path. The source path is the home directory
   outside the container and the destination overrides the home
   directory within the container.

#. **{ENVPREFIX}_HOSTNAME**: The container's hostname.

``I``
=====

#. **{ENVPREFIX}_IMAGE**: Filename of the container.

``J``
=====

#. **{ENVPREFIX}_JSON**: Use JSON as an input or output format. Applies to the
   ``build`` and ``instance list`` commands. Default is false.

``K``
=====

#. **{ENVPREFIX}_KEEP_PRIVS**: To let root user keep privileges in the
   container. Default is set to false.

``L``
=====

#. **{ENVPREFIX}_LABELS**: Specifies the labels associated with the
   image.

#. **{ENVPREFIX}_LIBRARY**: Specifies the library to pull from. Default
   is set to our Cloud Library.

#. **{ENVPREFIX}_LOCAL_VERIFY**: Set to true to only use the local keyring when
   verifying PGP signed SIF images. Disables retrieval of public keys from
   configured keyservers. Default is false.

#. **{ENVPREFIX}_LOGIN_USERNAME**: Set the username to use when logging in to a
   remote endpoint, registry, or keyserver.

#. **{ENVPREFIX}_LOGIN_PASSWORD**: Set the password to use when logging in to a
   remote endpoint, registry, or keyserver.

#. **{ENVPREFIX}_LOGIN_INSECURE**: Set to true to use HTTP (not HTTPS) when
   logging in to a remote endpoint. Default is false.

#. **{ENVPREFIX}_LOGS**: Set to true to show the path to instance log files in
   ``instance list`` output. Default is false.

``M``
=====

#. **{ENVPREFIX}_MEMORY**: Specify a memory limit in bytes for the
   container. Default is unset (no limit).

#. **{ENVPREFIX}_MEMORY_RESERVATION**: Specify a memory soft limit in
   bytes for the container. Default is unset (no limit).

#. **{ENVPREFIX}_MEMORY_SWAP**: Specify a limit for memory + swap usage by the
   container. Default is unset. Effect depends on **{ENVPREFIX}_MEMORY**.

#. **{ENVPREFIX}_MESSAGELEVEL**: Set numeric message level for output. 
   Message levels are `Fatal=-4, Error=-3, Warn=-2, Log=-1, Info=1, 
   Verbose=2, Verbose2=3, Verbose3=4, Debug=5`.

#. **{ENVPREFIX}_MOUNT**: To specify host to container mounts, using the
   syntax understood by the ``--mount`` flag. Multiple mounts should be
   separated by newline characters.

``N``
=====

#. **{ENVPREFIX}_NAME**: Specifies a custom image name.

#. **{ENVPREFIX}_NETWORK**: Used to specify a desired network. If more
   than one parameters is used, addresses should be separated by commas,
   where each network will bring up a dedicated interface inside the
   container.

#. **{ENVPREFIX}_NETWORK_ARGS**: To specify the network arguments to
   pass to CNI plugins.

#. **{ENVPREFIX}_NOCLEANUP**: To not clean up the bundle after a failed
   build, this can be helpful for debugging. Default is set to false.

#. **{ENVPREFIX}_NOCOLOR**: Print mesages without color output.
   Default is set to false unless stderr is not a terminal.

#. **{ENVPREFIX}_NO_HTTPS** and **{ENVPREFIX}_NOHTTPS**: Set to true to use HTTP
   (not HTTPS) to communicate with registry servers. Default is false.

#. **{ENVPREFIX}_NO_EVAL**: Set to true in order to prevent {Project}
   performing shell evaluation on environment variables / runscript
   arguments at startup.

#. **{ENVPREFIX}_NO_HOME**: Considers not mounting users home directory
   if home is not the current working directory. Default is set to
   false.

#. **{ENVPREFIX}_NO_INIT** and **{ENVPREFIX}_NOSHIMINIT**: Considers not
   starting the ``shim`` process with ``--pid``.

#. **{ENVPREFIX}_NO_MOUNT**: Disable an automatic mount that has been set in
   ``{command}.conf``. Accepts ``proc / sys / dev / devpts / home / tmp /
   hostfs / cwd``, or the source path for a system specific bind.

#. **{ENVPREFIX}_NO_NV**: Flag to disable Nvidia support. Opposite of
   ``{ENVPREFIX}_NV``.

#. **{ENVPREFIX}_NO_PID**: Set to true to disable the PID namespace, when it is
   inferred by other options (e.g.``--containall`` )

#. **{ENVPREFIX}_NO_PRIVS**: To drop all the privileges from root user
   in the container. Default is false.

#. **{ENVPREFIX}_NOTEST**: Set to true to disable execution of ``%test`` sections
   when building a container.

#. **{ENVPREFIX}_NO_UMASK**: Set to true to prevent host umask propagating
   to container, and use a default 0022 umask instead. Default is false.

#. **{ENVPREFIX}_NV**: To enable Nvidia GPU support. Default is
   set to false.

#. **{ENVPREFIX}_NVCCLI**: To use nvidia-container-cli for container GPU setup
   (experimental, only unprivileged).

``O``
=====

#. **{ENVPREFIX}_OOM_KILL_DISABLE**: Set to true to disable OOM killer for
   container processes, if possible. Default is false.

#. **{ENVPREFIX}_OVERLAY** and **{ENVPREFIX}_OVERLAYIMAGE**: To indicate
   the use of an overlay file system image for persistent data storage
   or as read-only layer of container.

``P``
=====

#. **{ENVPREFIX}_PULLDIR** and **{ENVPREFIX}_PULLFOLDER**: Specify destination
   directory when pulling a container image.

#. **{ENVPREFIX}_PID_FILE**: When starting an instance, write the instance PID
   to the specified file.

#. **{ENVPREFIX}_PIDS_LIMIT**: Specify maximum number of processes that
   the container may spawn. Default is 0 (no limit).

``Q``
=====

#. **{ENVPREFIX}_QUIET**: Suppresses all Info messages.
   Default is set to false.

``R``
=====

#. **{ENVPREFIX}_ROOTFS**: During a build ``{ENVPREFIX}_ROOTFS`` is set to the
   path of the rootfs for the container. It can be used within a definition file
   to manipulate the rootfs (e.g. from the ``%setup`` section).

#. **{ENVPREFIX}_ROCM**: Set to true to expose ROCm devices and libraries inside
   the container. Default is false.

#. **{ENVPREFIX}_RUNSCRIPT**: Specifies the runscript of the image.

``S``
=====

#. **{ENVPREFIX}_SANDBOX**: Set to true to specify that the format of the image
   should be a sandbox. Default is set to false.

#. **{ENVPREFIX}_SCRATCH** and **{ENVPREFIX}_SCRATCHDIR**: Used to
   include a scratch directory within the container that is linked to a
   temporary directory. (use -W to force location)

#. **{ENVPREFIX}_SECTION**: Set to specify a comma separated string of all
   the sections to be run from the deffile (setup, post, files,
   environment, test, labels, none)

#. **{ENVPREFIX}_SECURITY**: Used to enable security features. (SELinux,
   Apparmor, Seccomp)

#. **{ENVPREFIX}_SECRET**: Lists all the private keys instead of the
   default which display the public ones.

#. **{ENVPREFIX}_SHELL**: The path to the program to be used as an
   interactive shell.

#. **{ENVPREFIX}_SIGNAL**: Specifies a signal sent to the instance.

#. **{ENVPREFIX}_SILENT**: Suppresses all Info and Warning messages.
   Default is set to false.

#. **{ENVPREFIX}_SIGNAL**: Specifies the signal to send to an instance with
   ``{command} instance stop``.

#. **{ENVPREFIX}_SIGN_KEY**: Set the path to a key file to be used when signing
   a SIF image.

#. **{ENVPREFIX}_SPARSE**: Set to true to create sparse overlay image files with
   the ``{command} overlay create`` command.

#. **{ENVPREFIX}_SHARENS**: Share the namespace and image 
   with other containers launched from the same parent process.

``T``
=====

#. **{ENVPREFIX}_TEST**: Specifies the test script for the image.

#. **{ENVPREFIX}_TMPDIR**: Specify a location for temporary files to be used
   when pulling and building container images. See :ref:`sec:temporaryfolders`.

``U``
=====

#. **{ENVPREFIX}_UNSHARE_PID**: To specify that the container will run
   in a new PID namespace. Default is set to false.

#. **{ENVPREFIX}_UNSHARE_IPC**: To specify that the container will run
   in a new IPC namespace. Default is set to false.

#. **{ENVPREFIX}_UNSHARE_NET**: To specify that the container will run
   in a new network namespace (sets up a bridge network interface by
   default). Default is set to false.

#. **{ENVPREFIX}_UNSHARE_UTS**: To specify that the container will run
   in a new UTS namespace. Default is set to false.

#. **{ENVPREFIX}_UNSQUASH**: To convert SIF files to temporary sandboxes
   before running a container. Default is set to false.

#. **{ENVPREFIX}_UPDATE**: To run the definition over an existing
   container (skips the header). Default is set to false.

#. **{ENVPREFIX}_URL**: Specifies the key server ``URL``.

#. **{ENVPREFIX}_USER**: As root, specify a user to manage that user's instances
   with the ``instance`` commands.

#. **{ENVPREFIX}_USERNS** and **{ENVPREFIX}_UNSHARE_USERNS**: To specify
   that the container will run in a new user namespace, allowing
   {Project} to run completely unprivileged even with a setuid
   installation.
   Default is set to false.

``V``
=====

#. **{ENVPREFIX}_VERBOSE**: Print additional information.
   Default is set to false.

``V``
=====

#. **{ENVPREFIX}_VERIFY_CERTIFICATE**: Set the path to a PEM file containing the
   certificate to be used when verifying an x509 signed SIF image.

#. **{ENVPREFIX}_VERIFY_INTERMEDIATES**: Set the path to a PEM file containing
   an intermediate certificate / chain to be used when verifying an x509 signed
   SIF image.

#. **{ENVPREFIX}_VERIFY_KEY**: Set the path to a key file to be used when
   verifying a key signed SIF image.

#. **{ENVPREFIX}_VERIFY_OCSP**: Set to true to enable OCSP verification of
   certificates. Default is false.

#. **{ENVPREFIX}_VERIFY_ROOTS**: Set the path to a PEM file containing root
   certificate(s) to be used when verifying an x509 signed SIF image.

``W``
=====

#. **{ENVPREFIX}_WORKDIR**: The working directory to be used for
   ``/tmp``, ``/var/tmp`` and ``$HOME`` (if ``-c`` or ``--contain`` was
   also used)

#. **{ENVPREFIX}_WRITABLE**: By default, all {Project} containers
   are available as read only, this option makes the file system
   accessible as read/write. Default set to false.

#. **{ENVPREFIX}_WRITABLE_TMPFS**: Makes the file system accessible as
   read-write with non-persistent data (with overlay support only).
   Default is set to false.

.. _buildmodules:

*************
Build Modules
*************

.. _build-library-module:

``library`` bootstrap agent
===========================

.. _sec:build-library-module:

Overview
--------

You can use an existing container in a Container Library as your
"base" and then add customization. This allows you to build multiple
images from the same starting point. For example, you may want to build
several containers with the same custom python installation, the same
custom compiler toolchain, or the same base MPI installation. Instead of
building these from scratch each time, you could create a base container
in the Container Library and then build new containers from that
existing base container adding customizations in ``%post``,
``%environment``, ``%runscript``, etc.

This requires setting up a Container Library as shown in the
:ref:`Managing Remote Endpoints <sec:managing-remote-endpoints>`
section.

Keywords
--------

.. code:: {command}

   Bootstrap: library

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   From: <entity>/<collection>/<container>:<tag>

The ``From`` keyword is mandatory. It specifies the container to use as
a base. ``entity`` is optional and defaults to ``library``.
``collection`` is optional and defaults to ``default``. This is the
correct namespace to use for some official containers (``alpine`` for
example). ``tag`` is also optional and will default to ``latest``.

.. code:: {command}

   Library: http://custom/library

The Library keyword is mandatory. It is the URL for the library server.

.. code:: {command}

   Fingerprints: 22045C8C0B1004D058DE4BEDA20C27EE7FF7BA84

The Fingerprints keyword is optional. It specifies one or more comma
separated fingerprints corresponding to PGP public keys. If present, the
bootstrap image will be verified and the build will only proceed if it
is signed by keys matching *all* of the specified fingerprints.

.. _build-docker-module:

``docker`` bootstrap agent
==========================

.. _sec:build-docker-module:

Overview
--------

Docker images are comprised of layers that are assembled at runtime to
create an image. You can use Docker layers to create a base image, and
then add your own custom software. For example, you might use Docker's
Ubuntu image layers to create an Ubuntu {Project} container. You
could do the same with Fedora, Debian, Arch, Suse, Alpine, BusyBox, etc.

Or maybe you want a container that already has software installed. For
instance, maybe you want to build a container that uses CUDA and cuDNN
to leverage the GPU, but you don't want to install from scratch. You can
start with one of the ``nvidia/cuda`` containers and install your
software on top of that.

Or perhaps you have already invested in Docker and created your own
Docker containers. If so, you can seamlessly convert them to
{Project} with the ``docker`` bootstrap module.

Keywords
--------

.. code:: {command}

   Bootstrap: docker

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   From: <registry>/<namespace>/<container>:<tag>@<digest>

The ``From`` keyword is mandatory. It specifies the container to use as
a base. ``registry`` is optional and defaults to ``index.docker.io``.
``namespace`` is optional and defaults to ``library``. This is the
correct namespace to use for some official containers (ubuntu for
example). ``tag`` is also optional and will default to ``latest``

See :ref:`{Project} and Docker <docker-and-oci>` for more
detailed info on using Docker registries.

.. code:: {command}

   Registry: http://custom_registry

The Registry keyword is optional. It will default to
``index.docker.io``.

.. code:: {command}

   Namespace: namespace

The Namespace keyword is optional. It will default to ``library``.

Notes
-----

Docker containers are stored as a collection of tarballs called layers.
When building from a Docker container the layers must be downloaded and
then assembled in the proper order to produce a viable file system. Then
the file system must be converted to Singularity Image File (sif)
format.

For detailed information about setting your build environment see
:ref:`Build Customization <build-environment>`.

.. _build-shub:

``shub`` bootstrap agent
========================

Overview
--------

You can use an existing container on Singularity Hub as your "base" and
then add customization. This allows you to build multiple images from
the same starting point. For example, you may want to build several
containers with the same custom python installation, the same custom
compiler toolchain, or the same base MPI installation. Instead of
building these from scratch each time, you could create a base container
on Singularity Hub and then build new containers from that existing base
container adding customizations in ``%post`` , ``%environment``,
``%runscript``, etc.

Keywords
--------

.. code:: {command}

   Bootstrap: shub

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   From: shub://<registry>/<username>/<container-name>:<tag>@digest

The ``From`` keyword is mandatory. It specifies the container to use as
a base. ``registry is optional and defaults to ``singularity-hub.org``.
``tag`` and ``digest`` are also optional. ``tag`` defaults to ``latest``
and ``digest`` can be left blank if you want the latest build.

Notes
-----

When bootstrapping from a Singularity Hub image, all previous definition
files that led to the creation of the current image will be stored in a
directory within the container called
``/.singularity.d/bootstrap_history``. {Project} will also alert you
if environment variables have been changed between the base image and
the new image during bootstrap.

.. _build-oras:

``oras`` bootstrap agent
========================

Overview
--------

Using, this module, a container from supporting OCI Registries - Eg: ACR
(Azure Container Registry), local container registries, etc can be used
as your "base" image and later customized. This allows you to build
multiple images from the same starting point. For example, you may want
to build several containers with the same custom python installation,
the same custom compiler toolchain, or the same base MPI installation.
Instead of building these from scratch each time, you could make use of
``oras`` to pull an appropriate base container and then build new
containers by adding customizations in ``%post`` , ``%environment``,
``%runscript``, etc.

Keywords
--------

.. code:: {command}

   Bootstrap: oras

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   From: registry/namespace/image:tag

The ``From`` keyword is mandatory. It specifies the container to use as
a base. Also,``tag`` is mandatory that refers to the version of image
you want to use.

.. code:: {command}

   Fingerprints: 22045C8C0B1004D058DE4BEDA20C27EE7FF7BA84

The Fingerprints keyword is optional. It specifies one or more comma separated 
fingerprints corresponding to PGP public keys. If present, the SIF file will be 
verified and the build will only proceed if it is signed by keys matching *all*
of the specified fingerprints.

.. _build-localimage:

``localimage`` bootstrap agent
==============================

.. _sec:build-localimage:

This module allows you to build a container from an existing
{Project} container on your host system. The name is somewhat
misleading because your container can be in either image or directory
format.

Overview
--------

You can use an existing container image as your "base", and then add
customization. This allows you to build multiple images from the same
starting point. For example, you may want to build several containers
with the same custom python installation, the same custom compiler
toolchain, or the same base MPI installation. Instead of building these
from scratch each time, you could start with the appropriate local base
container and then customize the new container in ``%post``,
``%environment``, ``%runscript``, etc.

Keywords
--------

.. code:: {command}

   Bootstrap: localimage

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   From: /path/to/container/file/or/directory

The ``From`` keyword is mandatory. It specifies the local container to
use as a base.

.. code:: {command}

   Fingerprints: 22045C8C0B1004D058DE4BEDA20C27EE7FF7BA84

The Fingerprints keyword is optional. It specifies one or more comma
separated fingerprints corresponding to PGP public keys. If present, and
the ``From:`` keyword points to a SIF format image, it will be verified
and the build will only proceed if it is signed by keys matching *all*
of the specified fingerprints.

Notes
-----

When building from a local container, all previous definition files that
led to the creation of the current container will be stored in a
directory within the container called
``/.singularity.d/bootstrap_history``. {Project} will also alert you
if environment variables have been changed between the base image and
the new image during bootstrap.

.. _build-yum:

``yum`` bootstrap agent
=======================

.. _sec:build-yum:

This module allows you to build a Red Hat style
container from a mirror URI based on yum or dnf.

Overview
--------

Use the ``yum`` module to specify a base for a RHEL-like container.
You must also specify the URI for the mirror you would like to use.

Keywords
--------

.. code:: {command}

   Bootstrap: yum

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   OSVersion: 9

The OSVersion keyword is optional. It specifies the OS version you would
like to use. It is only required if you have specified a %{OSVERSION}
variable in the ``MirrorURL`` keyword.

.. code:: {command}

   MirrorURL: http://repo.almalinux.org/almalinux/%{OSVERSION}/BaseOS/x86_64/os

The MirrorURL keyword is mandatory. It specifies the URI to use as a
mirror to download the OS. If you define the ``OSVersion`` keyword, then
you can use it in the URI as in the example above.

.. code:: {command}

   Include: dnf

The Include keyword is optional. It allows you to install additional
packages into the core operating system. It is a best practice to supply
only the bare essentials such that the ``%post`` section has what it
needs to properly complete the build. One common package you may want to
install when using the ``yum`` build module is YUM or DNF itself.

Notes
-----

There is a major limitation with using YUM to bootstrap a container. The
RPM database that exists within the container will be created using the
RPM library and Berkeley DB implementation that exists on the host
system. If the RPM implementation inside the container is not compatible
with the RPM database that was used to create the container, RPM and YUM
commands inside the container may fail. This issue can be easily
demonstrated by bootstrapping an older RHEL compatible image by a newer
one (e.g. bootstrap a RHEL 8 container from a RHEL 9 host).

In order to use the ``yum`` build module, you must have ``yum``
installed on your system. It may seem counter-intuitive to install YUM
on a system that uses a different package manager, but you can do so.
For instance, on Ubuntu you can install it like so:

.. code::

   $ sudo apt-get update && sudo apt-get install yum

.. _build-debootstrap:

``debootstrap`` build agent
===========================

.. _sec:build-debootstrap:

This module allows you to build a Debian/Ubuntu style container from a
mirror URI.

Overview
--------

Use the ``debootstrap`` module to specify a base for a Debian-like
container. You must also specify the OS version and a URI for the mirror
you would like to use.

Keywords
--------

.. code:: {command}

   Bootstrap: debootstrap

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   OSVersion: xenial

The OSVersion keyword is mandatory. It specifies the OS version you
would like to use. For Ubuntu you can use code words like ``trusty``
(14.04), ``xenial`` (16.04), and ``yakkety`` (17.04). For Debian you can
use values like ``stable``, ``oldstable``, ``testing``, and ``unstable``
or code words like ``wheezy`` (7), ``jesse`` (8), and ``stretch`` (9).

   .. code:: {command}

      MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

The MirrorURL keyword is mandatory. It specifies a URI to use as a
mirror when downloading the OS.

.. code:: {command}

   Include: somepackage

The Include keyword is optional. It allows you to install additional
packages into the core operating system. It is a best practice to supply
only the bare essentials such that the ``%post`` section has what it
needs to properly complete the build.

Notes
-----

In order to use the ``debootstrap`` build module, you must have
``debootstrap`` installed on your system. On Ubuntu you can install it
like so:

.. code::

   $ sudo apt-get update && sudo apt-get install debootstrap

On RHEL you can install it from the epel repos like so:

.. code::

   $ sudo dnf update && sudo dnf install epel-release && sudo dnf install debootstrap.noarch

.. _build-arch:

``arch`` bootstrap agent
========================

.. _sec:build-arch:

This module allows you to build a Arch Linux based container.

Overview
--------

Use the ``arch`` module to specify a base for an Arch Linux based
container. Arch Linux uses the aptly named ``pacman`` package manager
(all puns intended).

Keywords
--------

.. code:: {command}

   Bootstrap: arch

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

The Arch Linux bootstrap module does not name any additional keywords at
this time. By defining the ``arch`` module, you have essentially given
all of the information necessary for that particular bootstrap module to
build a core operating system.

Notes
-----

Arch Linux is, by design, a very stripped down, light-weight OS. You may
need to perform a significant amount of configuration to get a usable
OS. Please refer to this `README.md
<https://github.com/{orgrepo}/blob/{repobranch}/examples/arch/README.md>`_
and the `Arch Linux example
<https://github.com/{orgrepo}/blob/{repobranch}/examples/arch/>`_
for more info.

.. _build-busybox:

``busybox`` bootstrap agent
===========================

.. _sec:build-busybox:

This module allows you to build a container based on BusyBox.

Overview
--------

Use the ``busybox`` module to specify a BusyBox base for container. You
must also specify a URI for the mirror you would like to use.

Keywords
--------

.. code:: {command}

   Bootstrap: busybox

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   MirrorURL: https://www.busybox.net/downloads/binaries/1.35.0-x86_64-linux-musl/busybox

The MirrorURL keyword is mandatory. It specifies a URI to use as a
mirror when downloading the OS.

Notes
-----

You can build a fully functional BusyBox container that only takes up
~700kB of disk space!

.. _build-zypper:

``zypper`` bootstrap agent
==========================

.. _sec:build-zypper:

This module allows you to build a Suse style container from a mirror
URI.

.. note::

   ``zypper`` version 1.11.20 or greater is required on the host system,
   as {Project} requires the ``--releasever`` flag.

Overview
--------

Use the ``zypper`` module to specify a base for a Suse-like container.
You must also specify a URI for the mirror you would like to use.

Keywords
--------

.. code:: {command}

   Bootstrap: zypper

The Bootstrap keyword is always mandatory. It describes the bootstrap
module to use.

.. code:: {command}

   OSVersion: 42.2

The OSVersion keyword is optional. It specifies the OS version you would
like to use. It is only required if you have specified a %{OSVERSION}
variable in the ``MirrorURL`` keyword.

.. code:: {command}

   Include: somepackage

The Include keyword is optional. It allows you to install additional
packages into the core operating system. It is a best practice to supply
only the bare essentials such that the ``%post`` section has what it
needs to properly complete the build. One common package you may want to
install when using the zypper build module is ``zypper`` itself.

.. _docker-daemon:

``docker-daemon`` bootstrap agent
=================================

Overview
--------

``docker-daemon`` allows you to build a SIF from any Docker image
currently residing in the Docker daemon's internal storage:

.. code:: console

   $ docker images alpine
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   alpine              latest              965ea09ff2eb        7 weeks ago         5.55MB

   $ {command} run docker-daemon:alpine:latest
   INFO:    Converting OCI blobs to SIF format
   INFO:    Starting build...
   Getting image source signatures
   Copying blob 77cae8ab23bf done
   Copying config 759e71f0d3 done
   Writing manifest to image destination
   Storing signatures
   2019/12/11 14:53:24  info unpack layer: sha256:eb7c47c7f0fd0054242f35366d166e6b041dfb0b89e5f93a82ad3a3206222502
   INFO:    Creating SIF file...
   {Project}>

The ``{ENVPREFIX}_DOCKER_HOST`` or ``DOCKER_HOST`` environment variables may be
set to instruct {{Project}} to pull images from a Docker daemon that is not
running at the default location. For example, when using a virtualized Docker you may be instructed to set ``DOCKER_HOST`` e.g.

.. code::

   To connect the Docker client to the Docker daemon, please set
   export DOCKER_HOST=tcp://192.168.59.103:2375

Keywords
--------

In a definition file, the ``docker-daemon`` bootstrap agent requires the source container reference to
be provided with the ``From:`` keyword:

.. code:: {command}

   Bootstrap: docker-daemon
   From: <image>:<tag>

where both ``<image>`` and ``<tag>`` are mandatory fields that must be
written explicitly.


.. _docker-daemon:

``docker-archive`` bootstrap agent
==================================

Overview
--------

The ``docker-archive`` boostrap agent allows you to create a {Project} image
from a docker image stored in a ``docker save`` formatted tar file:

.. code:: console

   $ docker save -o alpine.tar alpine:latest

   $ {command} run docker-archive:$(pwd)/alpine.tar
   INFO:    Converting OCI blobs to SIF format
   INFO:    Starting build...
   Getting image source signatures
   Copying blob 77cae8ab23bf done
   Copying config 759e71f0d3 done
   Writing manifest to image destination
   Storing signatures
   2019/12/11 15:25:09  info unpack layer: sha256:eb7c47c7f0fd0054242f35366d166e6b041dfb0b89e5f93a82ad3a3206222502
   INFO:    Creating SIF file...
   {Project}>

Keywords
--------

In a definition file, the ``docker-archive`` bootstrap agent requires the path
to the tar file containing the image to be specified with the ``From:`` keyword.

.. code:: {command}

   Bootstrap: docker-archive
   From: <path-to-tar-file>

.. _scratch-agent:

``scratch`` bootstrap agent
===========================

The scratch bootstrap agent allows you to start from a completely empty
container. You are then responsible for adding any and all executables,
libraries etc. that are required. Starting with a scratch container can
be useful when you are aiming to minimize container size, and have a
simple application / static binaries.

Overview
--------

A minimal container providing a shell can be created by copying the
``busybox`` static binary into an empty scratch container:

.. code:: {command}

   Bootstrap: scratch

   %setup
       # Runs on host - fetch static busybox binary
       curl -o /tmp/busybox https://www.busybox.net/downloads/binaries/1.31.0-i686-uclibc/busybox
       # It needs to be executable
       chmod +x /tmp/busybox

   %files
       # Copy from host into empty container
       /tmp/busybox /bin/sh

   %runscript
      /bin/sh

The resulting container provides a shell, and is 696KiB in size:

.. code::

   $ ls -lah scratch.sif
   -rwxr-xr-x. 1 dave dave 696K May 28 13:29 scratch.sif

   $ {command} run scratch.sif
   WARNING: passwd file doesn't exist in container, not updating
   WARNING: group file doesn't exist in container, not updating
   {Project}> echo "Hello from a 696KiB container"
   Hello from a 696KiB container

Keywords
--------

.. code:: {command}

   Bootstrap: scratch

There are no additional keywords for the scratch bootstrap agent.
