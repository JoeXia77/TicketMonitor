from PIL import ImageGrab
import time
import pyautogui
from playsound import playsound
import random




## Blue: Color at position (2151, 834) is (223, 239, 252)
## White: Color at position (2122, 803) is (248, 251, 254)


## check range:
## start position and end position is: 
## for the left page: (2119, 776), (2323, 892)
## for the right page: (2370, 775), (2576, 893) 
## calculate logic: x = x0 + diff, diff = 0 for the first, diff = (x2-x1)*(n-1)//6

## four points after page expired
'''
Recorded position: (5112, 1343)
Recorded position: (5112, 1343)
Recorded position: (2007, 471)
Recorded position: (2042, 535)
'''


pos = {'refresh_page':(85, 51), 'warning_after_refresh':(2554, 825), 'arrow_to_bottom':(2840, 185), 'Date_of_Appointment':(2234, 667) ,'next':(2587, 707), "prev":(2117, 708), "start_point_left_month":{2119, 776}, "start_point_right_month":(2370, 775)}

blue_color = (225, 239, 252)
white_color = (246, 250, 254)
background_color = (255, 255, 255)

refresh_count = 30
refresh_interval = 280 ## second


def click_positions(positions):
    for pos in positions:
        noise_x = random.randint(-2, 2)
        noise_y = random.randint(-2, 2)
        pyautogui.click(pos[0] + noise_x, pos[1] + noise_y)
        time.sleep(2.5)


def get_pixel_color(x, y):
    return ImageGrab.grab().getpixel((x, y))


def calculate_pos_to_check():
    ## generate all the positions we want to check:
    ## start position and end position is: (2119, 776), (2323, 892)
    ## there are 7 positions horizontally, 5 positions vertically, given the start position and end position, we can got a metrix of 35 positions
    left_start_position = (2119, 776)
    left_end_position = (2323, 892)
    left_page_positions = []
    for j in range(5):
        for i in range(7):
            left_page_positions.append((left_start_position[0] + (left_end_position[0]-left_start_position[0])*i//6, left_start_position[1] + (left_end_position[1]-left_start_position[1])*j//4))
    
    ## right page positions start from (2370, 775) end at (2576, 893) 
    right_start_position = (2370, 775)
    right_end_position = (2576, 893)
    right_page_positions = []
    for j in range(5):
        for i in range(7):
            right_page_positions.append((right_start_position[0] + (right_end_position[0]-right_start_position[0])*i//6, right_start_position[1] + (right_end_position[1]-right_start_position[1])*j//4))
    
    return left_page_positions + right_page_positions

def print_matrix(colors, rows=5, cols=7):
    for i in range(rows):
        row = ""
        for j in range(cols):
            color = colors[i * cols + j]
            row += f"{color}   "
        print(row)


def play_sound_if_blue_icon_found(color_labels):
    for color in color_labels:
        if color[0] == "B":
            playsound('found.mp3')

if __name__ == "__main__":

    ## prepare, 
    ## 1. expand your brower
    ## 2. go to the Schedule Appointment page
    ## 3. set the click_seq making current month to May
    click_seq = [pos['refresh_page'], pos['Date_of_Appointment'], pos['next']]
    found_blue = False
    for i in range(refresh_count):
        if found_blue:
            print("\nFound blue\n")
        else:
            print("\nNot found blue yet\n")
        time.sleep(5)
        click_positions(click_seq)
        color_error = 6
        pos_to_check = calculate_pos_to_check()
    
        color_labels = []
        for pos in pos_to_check:
            color = get_pixel_color(pos[0], pos[1])
            label = ""
    
            if abs(color[0] - blue_color[0]) <= color_error and abs(color[1] - blue_color[1]) <= color_error and abs(color[2] - blue_color[2]) <= color_error:
                label = f"B {color}"
                found_blue = True
            elif abs(color[0] - white_color[0]) <= color_error and abs(color[1] - white_color[1]) <= color_error and abs(color[2] - white_color[2]) <= color_error:
                label = f"W {color}"
            elif abs(color[0] - background_color[0]) <= color_error and abs(color[1] - background_color[1]) <= color_error and abs(color[2] - background_color[2]) <= color_error:
                label = f"N {color}"
            else:
                label = f"E {color}"
            
            color_labels.append(label)
    
        # Assuming there are exactly 70 positions to check, print two 7x5 matrices
        print_matrix(color_labels[:35])
        print("\n")
        print_matrix(color_labels[35:])
        play_sound_if_blue_icon_found(color_labels)
        
        time.sleep(refresh_interval)
    if found_blue:
        print("Found blue")
    else:
        print("Not found blue")





