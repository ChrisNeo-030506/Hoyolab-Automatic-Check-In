from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pyautogui

options = Options()
options.add_argument("start-maximized")
options.add_argument(r"user-data-dir=C:\Users\SCSM11\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"profile-directory=Profile 1")
chrome = webdriver.Chrome(options=options)

chrome.get("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&lang=en-us&bbs_theme=dark&bbs_theme_device=1")

time.sleep(3)

genshin_impact_red_dot = pyautogui.locateOnScreen("png/genshin_impact_red_dot.png", confidence=0.9)

if genshin_impact_red_dot:
    pyautogui.moveTo(genshin_impact_red_dot, duration=1)
    pyautogui.moveRel(-50, 40, duration=1)
    pyautogui.click()

chrome.execute_script("window.open("");")

chrome.switch_to.window(chrome.window_handles[1])

chrome.get("https://act.hoyolab.com/bbs/event/signin/hkrpg/e202303301540311.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&utm_campaign=checkin&utm_id=6&lang=en-us&bbs_theme=dark&bbs_theme_device=1")

time.sleep(3)

honkai_starrail_red_dot = pyautogui.locateOnScreen("png/honkai_starrail_red_dot.png", confidence=0.9)

if honkai_starrail_red_dot:
    pyautogui.moveTo(honkai_starrail_red_dot, duration=1)
    pyautogui.moveRel(-60, 50, duration=1)
    pyautogui.click()

chrome.execute_script("window.open("");")

chrome.switch_to.window(chrome.window_handles[2])

chrome.get("https://act.hoyolab.com/bbs/event/signin/zzz/e202406031448091.html?act_id=e202406031448091&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_campaign=checkin&utm_id=8&utm_medium=tools&utm_source=hoyolab&lang=en-us&bbs_theme=dark&bbs_theme_device=1")

time.sleep(3)

zenless_zone_zero_red_dot = pyautogui.locateOnScreen("png/zenless_zone_zero_red_dot.png", confidence=0.9)

if zenless_zone_zero_red_dot:
    pyautogui.moveTo(zenless_zone_zero_red_dot, duration=1)
    pyautogui.moveRel(-60, 50, duration=1)
    pyautogui.click()