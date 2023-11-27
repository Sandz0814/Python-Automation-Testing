import time
from Tools.function import BaseDriver
from selenium.webdriver import ActionChains


class Droppable(BaseDriver):

    droppable_module = "//span[normalize-space()='Droppable']"
    header = "//div[@class='main-header']"

    accept_tab = "//a[@id='droppableExample-tab-accept']"
    acceptable = "//div[@id='acceptable']"
    not_acceptable = "//div[@id='notAcceptable']"
    drop_here = "//div[@id='acceptDropContainer']//div[@id='droppable']"

    simple_tab = "//a[@id='droppableExample-tab-simple']"
    simple_drag_me = "//div[@id='draggable']"
    simple_drop_here = "//div[@id='simpleDropContainer']//div[@id='droppable']"

    prevent_propagation = "//a[@id='droppableExample-tab-preventPropogation']"
    drag_box = "//div[@id='dragBox']"
    outer_not_greedy = "//div[@id='notGreedyDropBox']//p[contains(text(),'Outer droppable')]"
    inner_not_greedy = "//div[@id='notGreedyInnerDropBox']"
    outer_greedy = "//div[@id='greedyDropBox']//p[contains(text(),'Outer droppable')]"
    inner_greedy = "//div[@id='greedyDropBoxInner']"

    revert_draggable_tab = "//a[@id='droppableExample-tab-revertable']"
    will_revert = "//div[@id='revertable']"
    not_revert = "//div[@id='notRevertable']"
    drop_revert = "//div[@id='revertableDropContainer']//div[@id='droppable']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_module(self):
        self.find(self.droppable_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Droppable" in headers
        image = "Droppable Header.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_accept_tab(self):
        self.find(self.accept_tab).click()

    def test_acceptable(self):
        drop_accept = self.find(self.acceptable)
        dropped = self.find(self.drop_here)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drop_accept, dropped).release().perform()
        image = "Drag and Dropped acceptable.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_not_acceptable(self):
        drop_accept = self.find(self.not_acceptable)
        dropped = self.find(self.drop_here)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drop_accept, dropped).release().perform()
        image = "Drag and Dropped Not acceptable.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_simple_tab(self):
        self.find(self.simple_tab).click()

    def test_simple_drag_me(self):
        drag_simple = self.find(self.simple_drag_me)
        simple_drop = self.find(self.simple_drop_here)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_simple, simple_drop).release().perform()
        image = "Simple Drag and Drop.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_prevent_propagation_tab(self):
        self.find(self.prevent_propagation).click()

    def test_drag_box(self):
        drag_boxs = self.find(self.drag_box)
        outer_not = self.find(self.outer_not_greedy)
        inner_not = self.find(self.inner_not_greedy)
        outer = self.find(self.outer_greedy)
        inner = self.find(self.inner_greedy)

        actions = ActionChains(self.driver)

        actions.drag_and_drop(drag_boxs, outer_not).release().perform()
        time.sleep(2)
        image = "Prevent Propagation Drag and Drop outer not greedy.png"
        self.s_shot(self.ss_url_interaction, image)
        actions.drag_and_drop(drag_boxs, inner_not).release().perform()
        time.sleep(2)
        image = "Prevent Propagation Drag and Drop inner not greedy.png"
        self.s_shot(self.ss_url_interaction, image)
        actions.drag_and_drop(drag_boxs, outer).release().perform()
        time.sleep(2)
        image = "Prevent Propagation Drag and Drop outer greedy.png"
        self.s_shot(self.ss_url_interaction, image)
        actions.drag_and_drop(drag_boxs, inner).release().perform()
        image = "Prevent Propagation Drag and Drop inner greedy.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_revert_draggable_tab(self):
        self.find(self.revert_draggable_tab).click()

    def test_will_revert(self):
        revert = self.find(self.will_revert)
        revert_drop = self.find(self.drop_revert)

        actions = ActionChains(self.driver)
        # Drop box original color white become blue item had been dropped
        actions.drag_and_drop(revert, revert_drop).release().perform()
        time.sleep(0)
        drop_box_background = revert_drop.value_of_css_property('background-color')
        steel_blue = drop_box_background
        assert drop_box_background == steel_blue
        image = "Will Revert Droppable.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_not_revert(self):
        revert_not = self.find(self.not_revert)
        revert_drop = self.find(self.drop_revert)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(revert_not, revert_drop).release().perform()
        image = "Will not Revert Droppable.png"
        self.s_shot(self.ss_url_interaction, image)

















