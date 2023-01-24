Reverse Kitten
==============

The remote system can be accessed through SSH using the non-privileged ``ctf`` user. The flag is in the ``/home/ctf/flag`` file, not readable by ``ctf``. There is a configuration in ``/etc/sudoers.d/tac`` allowing the ``ctf`` user to run ``tac`` as a privileged action on the ``flag`` file and read its contents.

Solution
--------

Connect through SSH using the ``ctf`` user and, while located in ``/home/ctf`` issue the command::

  sudo /usr/bin/tac flag

The solution script is ``sol/extract``; enter the ``sol/`` folder and run the ``extract`` script::

  $ ./extract
  SIS{sudo_make_me_a_sandwich}
  spawn ssh ctf@141.85.224.157 -p 2232 cd /home/ctf; sudo /usr/bin/tac flag
  ctf@141.85.224.157's password:
  SIS{sudo_make_me_a_sandwich}

There are two solutions in the script, both using interactive SSH to connect to the remote host and extract the flag from the archive:

* one solution uses ``sshpass``
* the other solution uses ``expect``

You need to install ``sshpass`` and/or ``expect`` for the solutions in the script to work.

Deployment
----------

You require a filesystem (as part of native OS installation or virtual machine or container) that runs an OpenSSH server. You need root acccess to the system.

You copy the ``remote/setup`` and ``remote/flag`` files to the remote end and then you run the ``setup`` script in the folder where the ``flag`` file is also located. The ``setup`` script copies the ``flag`` file in ``/home/ctf/flag`` and makes it unreadable for the ``ctf`` user; and it creates the ``/etc/sudoers.d/tac`` file allowing the ``ctf`` user to run ``tac`` to read the contents of the ``/home/ctf/flag`` file. Afterwards, as advised by the script, remove the ``setup`` and ``flag`` files.

Requirements
------------

For solution:

* ``sshpass`` installed and/or
* ``expect`` installed

For deployment:

* filesystem installation as part of a running OS-like instance: native, virtual machine or container
* root access to installation
* OpenSSH server running
* ``sudo`` installed
