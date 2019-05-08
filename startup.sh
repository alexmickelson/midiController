#!/bin/bash

jackd -P70 -p16 -t200 -dalsa -dhw:1 -p128 -n3 -r44100 -s &
sleep .5s

slgui &
sleep 3s

jack_connect system:capture_2 sooperlooper:common_in_1
jack_connect sooperlooper:common_out_1 system:playback_1
aconnect 129:0 128:0

echo '

READY TO GO

'
