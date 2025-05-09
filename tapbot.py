import pyautogui
import time

pyautogui.FAILSAFE = True

# Get screen size
screenWidth, screenHeight = pyautogui.size()
print(f"Screen size: {screenWidth}x{screenHeight}")

# Wait for user to position the mouse
print("Move mouse to tap point and wait 5 seconds...")
time.sleep(5)

# Capture mouse position
x, y = pyautogui.position()
print(f"Tap position captured at: {x}, {y}")

# Tap loop
num_taps = 1000
delay_between_taps = 0.01  # 10ms

print(f"Starting {num_taps} taps...")
for i in range(num_taps):
    pyautogui.click(x, y)
    time.sleep(delay_between_taps)

print("Done tapping!")
