import sys

import pygame

def check_events():
    """响应按键与鼠标事件"""
    for event in pygame.event.get():
