.. _endpoint:

################
Remote Endpoints
################

********
Overview
********

The ``remote`` command group allows users to manage the service
endpoints {Project} will interact with for many common command
flows. This includes managing credentials for image storage services
and keyservers used to locate public keys for SIF
image verification. Currently, there are three main types of remote
endpoints managed by this command group: `Library API Registries
<https://singularityhub.github.io/library-api/#/?id=library-api>`_,
OCI registries, and keyservers.

You are most likely interacting with remote endpoints on a regular basis using
various {Project} commands:
`pull
<cli/{command}_pull.html>`__,
`push
<cli/{command}_push.html>`__,
`build
<cli/{command}_build.html>`__,
`key
<cli/{command}_key.html>`__,
`search
<cli/{command}_search.html>`__,
`verify
<cli/{command}_verify.html>`__,
`exec
<cli/{command}_exec.html>`__,
`shell
<cli/{command}_shell.html>`__,
`run
<cli/{command}_run.html>`__,
or `instance
<cli/{command}_instance.html>`__.

.. _sec:managing-remote-endpoints:

*************************
Managing Remote Endpoints
*************************

A fresh installation of {Project} is configured with the ``DefaultRemote``,
which does not support the Library API as it is only configured with a
functioning key server, ``https://keys.openpgp.org``. Users or administrators
should configure one of the Library API implementations listed `here
<https://singularityhub.github.io/library-api/#/?id=library-api>`_ if they would
like to use a Library API registry.

Users can setup and switch between multiple remote endpoints, which are
stored in their ``~/.{command}/remote.yaml`` file. Alternatively,
remote endpoints can be set system-wide by an administrator.

Generally, users and administrators should manage remote endpoints using
the ``{command} remote`` command, and avoid editing ``remote.yaml``
configuration files directly.

List Remotes
============

To ``list`` existing remote endpoints, run the following:

.. code:: console

   $ {command} remote list

   NAME           URI                  DEFAULT?  GLOBAL?  EXCLUSIVE?  SECURE?
   DefaultRemote  cloud.apptainer.org  ✓         ✓                    ✓

The ``✓`` in the ``DEFAULT?`` column for ``DefaultRemote`` shows that this
is the current default remote endpoint.

.. _remote_add_and_login:

Add & Login To Remotes
======================

To ``add`` a remote endpoint (for the current user only):

.. code:: console

   $ {command} remote add <remote_name> <remote_uri>

For example, if you have an installation of {Project} enterprise
hosted at enterprise.example.com:

.. code:: console

   $ {command} remote add myremote https://enterprise.example.com

   INFO:    Remote "myremote" added.
   Generate an access token at https://enterprise.example.com/auth/tokens, and paste it here.
   Token entered will be hidden for security.
   Access Token:

You will be prompted to setup an API key as the remote is added. As the example
above shows, the output of the ``add`` subcommand will provide you with the web
address you need to visit in order to generate your new access token.

To ``add`` a global remote endpoint (available to all users on the
system), an administrative user should run:

.. code:: console

   $ sudo {command} remote add --global <remote_name> <remote_uri>

   # example...
   $ sudo {command} remote add --global company-remote https://enterprise7.example.com
   INFO:    Remote "company-remote" added.
   INFO:    Global option detected. Will not automatically log into remote.

.. note::

   Global remote configurations can only be modified by the root user and are
   stored in the ``etc/{command}/remote.yaml`` file under the {Project}
   installation location.

To ``login`` to a remote, for the first time or if your token expires or
was revoked:

.. code:: console

   # Login to the default remote endpoint
   $ {command} remote login

   # Login to another remote endpoint
   $ {command} remote login <remote_name>

   # example...
   $ {command} remote login myremote
   {command} remote login myremote
   INFO:    Authenticating with remote: myremote
   Generate an API Key at https://enterprise.example.com/auth/tokens, and paste here:
   API Key:
   INFO:    API Key Verified!

If you ``login`` to a remote that you already have a valid token for,
you will be prompted, and the new token will be verified, before it
replaces your existing credential. If you enter an incorrect token your
existing token will not be replaced:

.. code:: console

   $ {command} remote login
   An access token is already set for this remote. Replace it? [N/y]y
   Generate an access token at https://enterprise.example.com/auth/tokens, and paste it here.
   Token entered will be hidden for security.
   Access Token:
   FATAL:   while verifying token: error response from server: Invalid Credentials

   # Previous token is still in place

.. note::

   It is important for users to be aware that the login command will
   store the supplied credentials or tokens unencrypted in your home
   directory.


Remove Remotes
==============

To ``remove`` an endpoint:

.. code:: console

   $ {command} remote remove <remote_name>

Use the ``--global`` option as the root user to remove a global
endpoint:

.. code:: console

   $ sudo {command} remote remove --global <remote_name>

Insecure (HTTP) Endpoints
-------------------------

If you are using a endpoint that only exposes its service discovery file 
over an insecure HTTP connection, it can be added by specifying 
the ``--insecure`` flag:

.. code:: console

   $ sudo {command} remote add --global --insecure test http://test.example.com
   INFO:    Remote "test" added.
   INFO:    Global option detected. Will not automatically log into remote.

This flag causes HTTP to be used instead of HTTPS *for service discovery only*. The
protocol used to access individual library-, build- and keyservice-URLs is
determined by the contents of the service discovery file.

Set the Default Remote
======================

To use a given remote endpoint as the default for commands such as ``push``,
``pull``, etc., use the ``remote use`` command:

.. code:: console

   $ {command} remote use <remote_name>

The remote designated as default shows up with a ``YES`` under the ``ACTIVE``
column in the output of ``remote list``:

.. code:: console

   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME            URI                      DEFAULT?  GLOBAL?  EXCLUSIVE?  SECURE?
   DefaultRemote   cloud.apptainer.org                ✓                    ✓
   company-remote  enterprise7.example.com            ✓                    ✓
   myremote        enterprise.example.com   ✓                              ✓
   test            test.example.com                   ✓                    ✓

   $ {command} remote use myremote
   INFO:    Remote "myremote" now in use.

   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME            URI                      DEFAULT?  GLOBAL?  EXCLUSIVE?  SECURE?
   DefaultRemote   cloud.apptainer.org      ✓         ✓                    ✓
   company-remote  enterprise7.example.com            ✓                    ✓
   myremote        enterprise.example.com                                  ✓
   test            test.example.com                   ✓                    ✓

In the example above, the default remote at the start (before being changed to
``DefaultRemote``) was ``myremote``. That is because adding a new remote endpoint
automatically makes the newly-added endpoint the default one, and the same user
had previously used the ``remote add`` command to add the ``myremote`` endpoint.
This behavior can be suppressed by passing the ``--no-default`` flag to the
``remote add`` command, which will then add a new remote endpoint but leave the
default endpoint unchanged:

.. code:: console

   $ {command} remote add --no-default myotherremote https://enterprise2.example.com
   INFO:    Remote "myotherremote" added.
   Generate an access token at https://enterprise2.example.com/auth/tokens, and paste it here.
   Token entered will be hidden for security.
   Access Token:

  $ {command} remote list

   NAME            URI                      DEFAULT?  GLOBAL?  EXCLUSIVE?  SECURE?
   DefaultRemote   cloud.apptainer.org      ✓         ✓                    ✓
   company-remote  enterprise7.example.com            ✓                    ✓
   myotherremote   enterprise2.example.com                                 ✓
   myremote        enterprise.example.com                                  ✓
   test            test.example.com                   ✓                    ✓


An administrator can make a remote
the only usable remote for the system, using the ``--exclusive`` flag:

.. code:: console

   $ sudo {command} remote use --exclusive company-remote
   INFO:    Remote "company-remote" now in use.
   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME            URI                      DEFAULT?  GLOBAL?  EXCLUSIVE?  SECURE?
   DefaultRemote   cloud.apptainer.org                ✓                    ✓
   company-remote  enterprise7.example.com  ✓         ✓        ✓           ✓
   myotherremote   enterprise2.example.com                                 ✓
   myremote        enterprise.example.com                                  ✓
   test            test.example.com                   ✓                    ✓

This, in turn, prevents users from changing the remote they use:

.. code:: console

   $ {command} remote use myremote
   FATAL:   could not use myremote: remote company-remote has been set exclusive by the system administrator

If you do not want to switch remote with ``remote use``, you can:

-  Instruct ``push`` and ``pull`` commands to use an alternative library server
   using the ``--library`` option (for example:
   ``{command} pull -F --library https://library.example.com library://alpine``).
   Note that the URL provided to the ``--library`` option is the URL of the
   library service itself, not the service discovery URL for the entire remote.
-  Instruct certain subcommands of the ``key`` command to use an alternative
   keyserver using the ``--url`` option (for example:
   ``{command} key search --url https://keys.example.com foobar``).

.. _no_default_remote:
.. _restoring_pre-{command}_library_behavior:

Restoring pre-{Project} library behavior
========================================

{Project}'s default remote endpoint configures only a public key
server, it does not support the ``library://`` protocol.
Formerly the default was set to point to Sylabs servers, but the
read/write support of the ``oras://`` protocol by for example the
:ref:`GitHub Container Registry <github_container_registry>`
makes it unnecessary.
The remote endpoint was also formerly used for builds using the
build ``--remote`` option, but {Project} does not support that.
Instead, it supports :ref:`unprivileged local builds <build>`.

If you would still like to have the previous default,
these are the commands to restore the library
behavior from before {Project}, where using the ``library://`` URI would
download from the Sylabs Cloud anonymously:

.. code::

   $ {command} remote add --no-login SylabsCloud cloud.sycloud.io
   INFO:    Remote "SylabsCloud" added.
   $ {command} remote use SylabsCloud
   INFO:    Remote "SylabsCloud" now in use.
   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  NO      YES     NO
   SylabsCloud    cloud.sycloud.io     YES     NO      NO

   Keyservers
   ==========

   URI                                 GLOBAL  INSECURE  ORDER
   https://keys.production.sycloud.io  YES     NO        1*

   * Active cloud services keyserver

To set the defaults system-wide see the corresponding section in the
`admin guide
<{admindocs}/configfiles.html#restoring-pre-{command}-library-behavior>`_.

************************
Keyserver Configurations
************************

By default, {Project} will use the keyserver defined by the active remote's
service discovery file. This behavior can be changed or supplemented via the
``add-keyserver`` and ``remove-keyserver`` subcommands. These commands allow an
administrator to create a global list of keyservers that will be used to verify
container signatures by default, where ``order 1`` will be the first in the
list. Other operations performed by {Project} that reach out to a keyserver
will only use the first, or ``order 1``, keyserver.

When listing the default remotes, we can see that the default keyserver is
``https://keys.openpgp.org`` and the asterisk next to its order indicates that it
is the keyserver associated with the current remote endpoint. We can also see
the ``INSECURE`` column indicating that {Project} will use TLS when
communicating with the keyserver.

.. code:: console

   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  YES     YES     NO

   Keyservers
   ==========

   URI                       GLOBAL  INSECURE  ORDER
   https://keys.openpgp.org  YES     NO        1*

   * Active cloud services keyserver

We can add a key server to list of keyservers as follows:

.. code:: console

   $ sudo {command} remote add-keyserver https://pgp.example.com
   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  YES     YES     NO

   Keyservers
   ==========

   URI                       GLOBAL  INSECURE  ORDER
   https://keys.openpgp.org  YES     NO        1*
   https://pgp.example.com   YES     NO        2

   * Active cloud services keyserver

Here, we see that the ``https://pgp.example.com`` keyserver was
added to the list. We can specify the order in the list in which this keyserver
should be added, by using the ``--order`` flag:

.. code:: console

   $ sudo {command} remote add-keyserver --order 1 https://pgp.example.com
   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  YES     YES     NO

   Keyservers
   ==========

   URI                      GLOBAL  INSECURE  ORDER
   https://pgp.example.com  YES     NO        1
   https://keys.openpgp.org YES     NO        2*

   * Active cloud services keyserver

Since we specified ``--order 1``, the ``https://pgp.example.com`` keyserver was
added as the first entry in the list, and the default keyserver was moved to
second in the list. With this keyserver configuration, all default image
verification performed by {Project} will, when searching for public keys,
reach out to ``https://pgp.example.com`` first, and only then to
``https://keys.openpgp.org``.

If a keyserver requires authentication prior to being used, users can login
as follows, supplying the password or an API token at the prompt:

.. code:: console

   $ {command} remote login --username myname https://pgp.example.com
   Password (or token when username is empty):
   INFO:    Token stored in /home/myname/.{command}/remote.yaml

The output of `remote list` will now show that we are logged in to
``https://pgp.example.com``:

.. code:: console

   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  YES     YES     NO

   Keyservers
   ==========

   URI                       GLOBAL  INSECURE  ORDER
   https://pgp.example.com   YES     NO        1
   https://keys.openpgp.org  YES     NO        2*

   * Active cloud services keyserver

   Authenticated Logins
   =================================

   URI                     INSECURE
   https://pgp.example.com NO

.. note::

   It is important for users to be aware that the ``remote login`` command will
   store the supplied credentials or tokens unencrypted in your home directory.

***********************
Managing OCI Registries
***********************

It is common for users of {Project} to use
`OCI <https://opencontainers.org/>`__ registries as sources for their container
images. Some registries require credentials to access certain images or even the
registry itself. Previously, the only method in {Project} to supply
credentials to registries was to supply credentials for each command or set
environment variables to contain the credentials for a single registry. See
:ref:`Authentication via Interactive Login
<sec:authentication_via_docker_login>` and :ref:`Authentication via Environment
Variables <sec:authentication_via_environment_variables>`.


{Project} supports the ability for users to supply credentials
on a per-registry basis with the ``remote`` command group.

Users can login to an OCI registry with the ``remote login`` command by
specifying a ``docker://`` prefix to the registry hostname:

.. code:: console

   $ {command} remote login --username myname docker://docker.io
   Password (or token when username is empty):
   INFO:    Token stored in /home/myname/.{command}/remote.yaml

   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  YES     YES     NO

   Keyservers
   ==========

   URI                       GLOBAL  INSECURE  ORDER
   https://keys.openpgp.org  YES     NO        1*

   * Active cloud services keyserver

   Authenticated Logins
   =================================

   URI                 INSECURE
   docker://docker.io  NO

An entry for ``docker://docker.io`` now shows up under ``Authenticated Logins``,
and {Project} will automatically supply the configured credentials when
interacting with DockerHub. We can also see the ``INSECURE`` column indicating
that {Project} will use TLS when communicating with the registry.

We can be logged-in to multiple OCI registries at the same time:

.. code:: console

   $ {command} remote login --username myname docker://registry.example.com
   Password (or token when username is empty):
   INFO:    Token stored in /home/myname/.{command}/remote.yaml

   $ {command} remote list
   Cloud Services Endpoints
   ========================

   NAME           URI                  ACTIVE  GLOBAL  EXCLUSIVE
   DefaultRemote  cloud.apptainer.org  YES     YES     NO

   Keyservers
   ==========

   URI                       GLOBAL  INSECURE  ORDER
   https://keys.openpgp.org  YES     NO        1*

   * Active cloud services keyserver

   Authenticated Logins
   =================================

   URI                            INSECURE
   docker://docker.io             NO
   docker://registry.example.com  NO

{Project} will supply the correct credentials for the registry based
on the hostname used, whenever using the following commands with a
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
or `instance
<cli/{command}_instance.html>`__.

.. note::

   It is important for users to be aware that the ``remote login`` command will
   store the supplied credentials or tokens unencrypted in your home directory.

