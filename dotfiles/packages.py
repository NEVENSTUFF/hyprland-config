import os
def install():
    packages = ['hyprland', 'hyprpaper', 'waybar', 'wofi', 'kitty', 'dunst']
    for i in packages:
        os.system(f'sudo pacman -S --needed --noconfirm {i}')
    os.system('cp -r ~/dotfiles/.config/ ~/.config/')
    sleep(3)
    print('.config been copied')
