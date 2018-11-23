# -*- coding: utf-8 -*-
import os
from robot.libraries.BuiltIn import BuiltIn
from appium import webdriver
from AppiumLibrary.locators import ElementFinder

class AppiumLibraryExtender(object):
    applib = None
    
    def __init__(self, alias='AppiumLibrary'):
        self.alias = alias
        self.ef = ElementFinder()

    def _current_application(self):
        if self.applib is None:
            self.applib = BuiltIn().get_library_instance(self.alias)
        return self.applib._current_application()

    def is_element_present(self, locator):
        driver = self._current_application()
        elements = self.ef.find(driver,locator)
        if len(elements) > 0:
            return True
        return False

    def dragFromToForDuration(self, fromX, start_y, end_x, end_y, duration):
        driver = self._current_application()
        width = driver.get_window_width()
        height = driver.get_window_height()
        fromX = float(start_x) / 100 * width
        toX = float(end_x) / 100 * width
        fromY = float(start_y) / 100 * height
        toY = float(end_y) / 100 * height

        platform = driver._get_platform()
        if platform == 'android':
            self.swipe(x_start, y_start, x_end, y_end, duration)
        else:
#            self.swipe(x_start, y_start, x_offset, y_offset, duration)
            self.driver.execute_script("mobile: dragFromToForDuration", {"fromX": fromX,
                                                                         "fromY":fromY,
                                                                         "toX": toX,
                                                                         "toY": toY
                                                                         "duration": duration})
