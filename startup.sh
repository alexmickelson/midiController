#!bin/bash

jackd -P70 -p16 -t200 -dalsa -dhw:1 -p128 -n3 -r44100 -s &

jack_connect system:capture_2 system:playback_1
