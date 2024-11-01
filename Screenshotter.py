#!/bon/bash/env python

import base64
import win32api
import win32con
import win32gui
import win32ui

def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUAL_SCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUAL_SCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUAL_SCREEN)

def screenshot(name='screenshot'):
    hdesktop = win32gui.GetDesktopWindow()
    width, height, left, top = get_dimensions()

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    screeshot = win32ui.CreateBitmap()
    screeshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0,0), (width, height),
                  img_dc, (left, top), win32con.SRCCOPY)
    screeshot.SaveBitmapFile(mem_dc, f'{name}.bmp')

    mem_dc.DeletDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def run():
    screenshot()
    with open('screenshot.bmp') as f:
        img = f.read()
    return img

if __name__ == '__main__':
    screenshot()