########################
{Project} User Guide
########################

Welcome to the {Project} User Guide!

This guide aims to give an introduction to {Project}, brief
installation instructions, and cover topics relevant to users building
and running containers.

For a detailed guide to installation and configuration, as well as upgrading or
uninstalling, please see the separate `Admin Guide <{admindocs}>`_ for this version of {Project}.

****************************************
Getting Started & Background Information
****************************************

.. toctree::
   :maxdepth: 2

   Introduction to {Project} <introduction>
   Quick Start <quick_start>
   Security in {Project} <security>

*******************
Building Containers
*******************

Learn how to write a definition file that can be used to build a
container. Understand the environment within a build and how to build
as a non-root user.

.. toctree::
   :maxdepth: 1

   Build a container <build_a_container>
   The Definition File <definition_files>
   Build Environment <build_env>
   Fakeroot feature <fakeroot>

******************************
Container Signing & Encryption
******************************

{Project} allows containers to be signed using a PGP key. The
signature travels with the container image, allowing you to verify that
the image is unmodified at any time. Encryption of containers
is also supported. Encrypted containers can be run without
decrypting them to disk first.

.. toctree::
   :maxdepth: 1

   Sign and Verify <signNverify>
   Key management commands <key_commands>
   Encrypted Containers <encryption>

*************************
Sharing & Online Services
*************************

.. toctree::
   :maxdepth: 1

   Remote Endpoints <endpoint>
   Keyserver Management <keyserver>
   OCI Registries <registry>
   Library API Registries <library_api>

**************
Advanced Usage
**************

Once you've understood the basics, explore all the options which
{Project} provides for accessing data, running persistent services
in containers, manipulating the container environment, and applying
networking and security configuration.

.. toctree::
   :maxdepth: 1

   Bind Paths and Mounts <bind_paths_and_mounts>
   Persistent Overlays <persistent_overlays>
   Instances - Running Services <running_services>
   Environment and Metadata <environment_and_metadata>
   Plugins <plugins>
   Security Options <security_options>
   Network Options <networking>
   Limiting Container Resources <cgroups>
   Application Checkpointing <checkpoint>

*************
Compatibility
*************

{Project} has unique benefits and supports easy access to GPUs and
other hardware. It also strives for compatibility with Docker/OCI
container formats. Understand the differences between {Project} and
Docker, as well as how to use containerized MPI and GPU applications.

.. toctree::
   :maxdepth: 1

   Singularity Compatibility <singularity_compatibility>
   Support for Docker / OCI Containers <docker_and_oci>
   OCI Runtime Support <oci_runtime>
   {Project} and MPI applications <mpi>
   GPU Support <gpu>

************
Get Involved
************

We'd love you to get involved in the {Project} community! Whether
through contributing feature and fixes, helping to answer questions from
other users, or simply testing new releases.

.. toctree::
   :maxdepth: 1

   Contributing <contributing>

*********
Reference
*********

.. toctree::
   :maxdepth: 2

   Appendix <appendix>

.. toctree::
   :maxdepth: 1

   Command Line Reference <cli>
   Licenses <license>
