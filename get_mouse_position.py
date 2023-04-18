from pynput import mouse
import time

positions = []

def on_click(x, y, button, pressed):
    global last_click_time

    if pressed:
        positions.append((x, y))
        print(f"Recorded position: ({x}, {y})")
        return len(positions) < 2 or time.time() - last_click_time > 0.5
    else:
        last_click_time = time.time()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    

print("Recorded positions:", positions[:-2])





## error of position: +-3

## in sep and oct, here is the bule and white color's position:
## position of blue: 2151, 834
## positoin of white: 2122, 803











