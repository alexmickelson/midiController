#!/bin/bash

jackd -R -p10 -t200 -dalsa -dhw:1 -p128 -n3 -r48000 -s &
sleep .5s

slgui &
./midiDriver.py &
sleep 5s

jack_connect system:capture_2 			sooperlooper:common_in_1
jack_connect sooperlooper:common_out_1 	system:playback_1
jack_connect system:capture_2 			system:playback_1

aconnect 128:0 129:0

echo '

READY TO GO

'
