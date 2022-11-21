# Reverse Kitten

The remote system can be accessed through SSH using the non-privileged ``ctf`` user.
The flag is in the ``/home/ctf/flag`` file, not readable by ``ctf``.
There is a configuration in ``/etc/sudoers.d/tac`` allowing the ``ctf`` user to run ``tac`` as a privileged action on the ``flag`` file and read its contents.

# Solution

Connect through SSH using the ``ctf`` user and, while located in ``/home/ctf`` issue the command:

```
  sudo /usr/bin/tac flag
```

The solution script is ``sol/extract``; enter the ``sol/`` folder and run the ``extract`` script:

```
  $ ./extract
  SIS{sudo_make_me_a_sandwich}
  spawn ssh ctf@141.85.224.157 -p 2232 cd /home/ctf; sudo /usr/bin/tac flag
  ctf@141.85.224.157's password:
  SIS{sudo_make_me_a_sandwich}
```
