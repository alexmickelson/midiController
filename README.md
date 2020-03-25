## STEPS:
1. start jack server
2. start sooperloopser slgui 
3. start qjackctl
4. run python midi controler program

## COMMANDS:
| Command | Description |
| - | - |
| slgui (&) | starts sooperlooper |
| jack_lsp | lists jack ports (-c to show connections) |
| jack_connect | connects jack ports |
| aconnect | connects alsa ports (midi) |
| -li | list inputs |
| -lo | list outputs |

## CONNECTIONS:
- system:capture_2 -> sooperlooper:common_in_1
- sooperlooper:common_out_1/2 -> system:playback_1

