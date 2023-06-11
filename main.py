import json
import subprocess

from screen import Screen

screen_modes = {
    'mirror': {'label': 'mirror', 'cmd': []},
    'left': {'label': 'extend left', 'cmd': []},
    'right': {'label': 'extend right', 'cmd': []},
    'internal': {'label': 'internal only', 'cmd': []},
    'external': {'label': 'external only', 'cmd': []}
}


def get_connected_screens() -> list[Screen]:
    sway_connected_screens_json = json.loads(
        subprocess.run(['swaymsg', '-t', 'get_outputs'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

    connected_screens = [Screen(screen['make'], screen['model'], screen["serial"], output_port=screen['name'])
                         for screen in sway_connected_screens_json]

    return connected_screens


def select_mode_rofi() -> str:
    label_list = [screen_modes[key]['label'] for key in screen_modes.keys()]
    echo_screen_modes_cmd = subprocess.Popen(['echo', '\n'.join(label_list)], stdout=subprocess.PIPE)

    rofi_selection = subprocess.check_output(['rofi', '-dmenu'], stdin=echo_screen_modes_cmd.stdout).decode('utf-8')
    echo_screen_modes_cmd.communicate()

    return next(key for key, value in screen_modes.items() if value['label'] in rofi_selection)


print(select_mode_rofi())
