.. _checkpoint:

##################
Checkpoint Feature
##################

********
Overview
********

The checkpoint feature allows users to transparently save the state of
containerized applications while they are executing and then restart them from
the saved state.

This is valuable for use cases that need to minimize the impact of ephemeral
environment failures, random hardware failures or job premption.

.. note::

    This feature is marked as **experimental** to allow flexibility as community
    feedback may warrant breaking changes to improve the overall usability for
    this feature set as it matures.

In order to enable checkpointing as a feature, the `DMTCP
<https://dmtcp.sourceforge.io/>`_ project has been chosen as the basis for an
integration. {Project} injects an installation of DMTCP from the host into the
container at container creation and uses it to wrap the launching of the
container process. When launching a process, DMTCP will monitor the spawned
application process and its children in order to fully checkpoint the state
of the application when triggered.

For interested readers, more detailed information about the technology can be
found in the publications listed on the `DMTCP website
<https://dmtcp.sourceforge.io/publications.html>`_.

Requirements
============

Due to the architecture of DMTCP, there are a couple requirements that must be
met to allow this integration to work correctly:

-  Applications that are the intended to be checkpointed must be dynamically
   linked.
-  dmtcp uses ``dladdr1()`` which is a GNU extension that requires ``glibc`` or
   ``glibc`` compatibility inside the container.

In addition to these requirements, the {Project} integration with DMTCP
requires that either:

-  The binaries and libraries required by DMTCP are within the user ``PATH`` and
   the ``ldconfig`` cache respectively.
-  The ``dmtcp-conf.yaml`` configuration file has been modified to contain
   the absolute paths of the listed binaries and libraries.

At time of release, the list of libraries and binaries in this configuration
is appropriate for the latest master branch of DMTCP. It can be modified by the
system administrator to add additional libraries if necessary. See the `admin
guide <{admindocs}/configfiles.html#dmtcp-conf-yaml>`_ for more details.

DMTCP Installation
==================

Installation instructions for DMTCP can be found on their git `repository
<https://github.com/dmtcp/dmtcp/blob/master/INSTALL.md>`_.
In order to maximize the portability of the DMTCP build, we recommend using the
``--enable-static-libstdcxx`` configure option.

A build and install of DMTCP from source will generally place libraries at
``/usr/local/lib/dmtcp``, which is not a standard path for the linker. You can
configure your linker to find these libraries and update its cache with the
following commands:

.. code::

    # echo /usr/local/lib/dmtcp > /etc/ld.so.conf.d/dmtcp.conf
    # ldconfig

Verify that the libraries are in the cache by ensuring there is output from the
following command:

.. code::

    $ ldconfig -p | grep dmtcp

The DMTCP project is currently working towards a ``3.0`` release. If you
encounter issues using a ``2.x`` installation of DMTCP, we recommend trying the
tip of the ``master`` branch to see if the issue has been resolved in the code
that will become the next release.

Example
=======

The following container (referred to as ``server.sif`` below) contains a simple
http server that allows a variable to be read and written with ``GET`` and
``POST`` requests respectively. This is not typical of applications packaged by
the {Project} community, but gives us an easy way to check that application
state has been successfully restored upon restart.

.. code::

    Bootstrap: docker
    From: python:3.10-bookworm
    
    %post
        mkdir /app
        cat > /app/server.py <<EOF
    import socketserver
    import argparse
    
    count = 0
    
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('port', type=int, help='A required integer port argument')
    args = parser.parse_args()
    
    class Handler(socketserver.BaseRequestHandler):
        def handle(self):
            global count
            count += 1
            response = bytes("request:{}\n".format(count), "ascii")
            self.request.sendall(response)
    
    if __name__ == "__main__":
        with socketserver.TCPServer(('', args.port), Handler) as server:
            server.allow_reuse_address = True
            server.serve_forever()
    EOF
    
    %startscript
        python3 /app/server.py $@

We can build this container using:

.. code::

    $ {command} build server.sif server.def


First things first, we need to create a ``checkpoint`` using the ``checkpoint``
command group. This initializes a location in your user home directory for
{Project} to store state related to DMTCP and the checkpoint images it will
generate.

.. code::

    $ {command} checkpoint create example-checkpoint
    INFO:    Checkpoint "example-checkpoint" created.

Now we can start an instance of our application with the ``--dmtcp-launch`` flag
naming the ``checkpoint`` we want to use to store state for this instance.

.. code::

    $ {command} instance start --dmtcp-launch example-checkpoint server.sif server 8888 # this last arg is the port the server will listen to.
    INFO:    instance started successfully

Once we have our application up and running, we can ``curl`` against it and read
the state of a variable on the server.

.. code::

    $ curl --http0.9 localhost:8888
    request:1

We can see that the request count value is ``1`` when this application is started
and accessed via curl. After making another call to the application, we can see that the request
count is ``2`` as expected.

.. code::

    $ curl --http0.9 localhost:8888
    request:2

Now that the request count variable on our server is in a new state, ``2``, we can use the
``checkpoint instance`` command and reference the instance via the
``instance://`` URI format:

.. code::

    $ {command} checkpoint instance server
    INFO:    Using checkpoint "example-checkpoint"

Now that we have checkpointed the state of our application, we can safely
stop the instance:

.. code::

    $ {command} instance stop server
    INFO:    Stopping server instance of /home/ian/server.sif (PID=209072)


We can restart our server and restore its state by starting a new instance using
the ``--dmtcp-restart`` flag and specifying the checkpoint to be used to restore
our application's state:

.. code::

    $ {command} instance start --dmtcp-restart example-checkpoint server.sif restarted-server 8888
    INFO:    instance started successfully


And now when we get access to the application again, the request count value is ``3`` as expected,
meaning that the previous request count value was ``2``.

.. code::

    $ curl --http0.9 localhost:8888
    $ request:3

We can repeat the previous two steps, i.e. stop the server instance and restart it via dmtcp to verify the restoration
of the value of the request count.

.. code::

    $ {command} instance stop server
    $ {command} instance start --dmtcp-restart example-checkpoint server.sif restarted-server 8888

Then access the application and see that the request count value is restored as expected. 

.. code::

    $ curl --http0.9 localhost:8888
    $ request:3

Finally, we can stop our instance running our restored application and delete our
checkpoint if we no longer need it to restart our application from this state:

.. code::

    $ {command} instance stop restarted-server
    INFO:    Stopping restarted-server instance of /home/ian/server.sif (PID=247679)
    $ {command} checkpoint delete example-checkpoint
    INFO:    Checkpoint "example-checkpoint" deleted.
