import pyautogui
from pynput import keyboard
from PIL import Image

savePosPalete = []

def startDraw():
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            for index, elem in enumerate(pale):
                tmp = img.getpixel((i, j))
                tmp = [tmp[0], tmp[1], tmp[2]]
                if tmp == elem:
                    pyautogui.click(x=savePosPalete[index+1][0], y=savePosPalete[index+1][1], button='left', clicks=2, interval=0.025)
                    pyautogui.click(x=savePosPalete[0][0]+i, y=savePosPalete[0][1]+j, button='left', clicks=2, interval=0.025)
                    break

def on_press(key):
    try:
        if(key.char == 's'):
            mouse_x, mouse_y = pyautogui.position()
            savePosPalete.append([mouse_x, mouse_y])
            print(savePosPalete)
        if(key.char == 'p'):
            startDraw()
    except AttributeError: print('special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


listener.start()

if __name__ == '__main__':

    img = Image.open('input.png')
    print(img.size)
    print(img.getpixel((0, 0)))
    print(img.getpixel((1, 6)))

    colors_count = 8

    q = img.quantize(colors=colors_count, method=2)
    pale = []
    for i in range(3 * colors_count):
        if i % 3 == 0:
            pale.append([q.getpalette()[i], q.getpalette()[i + 1], q.getpalette()[i + 2]])

    print(pale)

    input("Waiting enter palete in your redector... If ready press ENTER")
    print("Init position of palete")