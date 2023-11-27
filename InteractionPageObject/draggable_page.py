import time
from Tools.function import BaseDriver
from selenium.webdriver import ActionChains


class Draggable(BaseDriver):

    draggable_module = "//span[normalize-space()='Dragabble']"
    header = "//div[@class='main-header']"

    axis_restricted_tab = "//a[@id='draggableExample-tab-axisRestriction']"
    x_axis = "//div[@id='restrictedX']"
    y_axis = "//div[@id='restrictedY']"

    container_restricted_tab = "//a[@id='draggableExample-tab-containerRestriction']"
    contained_within_box = "//div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']"
    contained_within_parent = "//span[@class='ui-widget-header ui-draggable ui-draggable-handle']"

    cursor_style_tab = "//a[@id='draggableExample-tab-cursorStyle']"
    cursor_center = "//div[@id='cursorCenter']"
    cursor_top_left = "//div[@id='cursorTopLeft']"
    cursor_bottom = "//div[@id='cursorBottom']"

    simple_tab = "//a[@id='draggableExample-tab-simple']"
    drag_box_simple = "//div[@id='dragBox']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_module(self):
        self.find(self.draggable_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Dragabble" in headers
        image = "Dragabble Header.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_open_axis_restricted_tab(self):
        self.find(self.axis_restricted_tab).click()

    def test_only_x(self):
        x = self.find(self.x_axis)
        actions = ActionChains(self.driver)
        actions.click_and_hold(x).move_by_offset(500, 0).release().perform()
        time.sleep(2)
        image = "Draggable Right only X1.png"
        self.s_shot(self.ss_url_interaction, image)
        actions.click_and_hold(x).move_by_offset(-352, 0).release().perform()
        time.sleep(2)
        image = "Draggable Left only X2.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_only_y(self):
        y = self.find(self.y_axis)
        actions = ActionChains(self.driver)
        actions.click_and_hold(y).move_by_offset(0, 600).release().perform()
        time.sleep(2)
        image = "Draggable Go down only Y1.png"
        self.s_shot(self.ss_url_interaction, image)
        actions.click_and_hold(y).move_by_offset(0, -400).release().perform()
        time.sleep(2)
        image = "Draggable Go up only Y2.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_container_restricted_tab(self):
        self.find(self.container_restricted_tab).click()

    def test_contained_within_box(self):
        contained_box = self.find(self.contained_within_box)
        actions = ActionChains(self.driver)
        actions.click_and_hold(contained_box).move_by_offset(520, 70).release().perform()
        image = "Draggable contained within box.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_contained_within_parent(self):
        contained_parent = self.find(self.contained_within_parent)
        actions = ActionChains(self.driver)
        actions.click_and_hold(contained_parent).move_by_offset(11, 84).release().perform()
        image = "Draggable contained within parent.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_cursor_style_tab(self):
        self.find(self.cursor_style_tab).click()

    def test_cursor_center(self):
        center = self.find(self.cursor_center)
        actions = ActionChains(self.driver)
        actions.click_and_hold(center).move_by_offset(570, 17).perform()
        time.sleep(1)
        image = "Draggable Cursor center.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_cursor_top_left(self):
        top_left = self.find(self.cursor_top_left)
        actions = ActionChains(self.driver)
        actions.click_and_hold(top_left).move_by_offset(824, 70).release().perform()
        time.sleep(1)
        image = "Draggable Cursor Top left.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_cursor_bottom(self):
        bottom = self.find(self.cursor_bottom)
        actions = ActionChains(self.driver)
        actions.click_and_hold(bottom).move_by_offset(500, 65).release().perform()
        time.sleep(1)
        image = "Draggable Cursor Bottom.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_simple(self):
        self.find(self.simple_tab).click()
        drag_box = self.find(self.drag_box_simple)
        actions = ActionChains(self.driver)
        actions.click_and_hold(drag_box).move_by_offset(600, 170).perform()
        image = "Draggable Cursor Simple.png"
        self.s_shot(self.ss_url_interaction, image)








