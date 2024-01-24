import pytest
from InteractionPageObject.draggable_page import Draggable
from InteractionPageObject.droppable_page import Droppable
from InteractionPageObject.resizable_page import Resizable
from InteractionPageObject.selectable_page import Selectable
from InteractionPageObject.sortable_page import Sortable
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElements(BaseDriver):

    def test_interaction(self):
        self.page_scroll()

        # Validate the Sortable function
        self.sort = Sortable(self.driver)
        self.sort.test_open_interaction_icon()
        self.sort.test_open_sortable_module()
        self.sort.test_header()
        self.sort.test_grid()
        self.sort.test_one_move_to_nine()
        self.sort.test_four_move_to_eight()
        self.sort.test_list()
        self.sort.test_two_move_to_six()
        self.sort.test_three_move_to_five()

        # Validate the Selectable funtion
        self.selectable = Selectable(self.driver)
        self.selectable.test_open_selectable_module()
        self.selectable.test_header()
        self.selectable.test_grid()
        self.selectable.test_select_grid_13579()
        self.selectable.test_list()
        self.selectable.test_select_list_select_14()

        # Validate the Resizable function
        self.resize = Resizable(self.driver)
        self.resize.test_open_resizable_module()
        self.resize.test_header()
        self.resize.test_resize_box()
        self.resize.test_infinite_resize()

        # Validate the Droppable function
        self.drop = Droppable(self.driver)
        self.drop.test_open_module()
        self.drop.test_header()
        self.drop.test_accept_tab()
        self.drop.test_acceptable()
        self.drop.test_not_acceptable()
        self.drop.test_simple_tab()
        self.drop.test_simple_drag_me()
        self.drop.test_prevent_propagation_tab()
        self.drop.test_drag_box()
        self.drop.test_revert_draggable_tab()
        self.drop.test_will_revert()
        self.drop.test_not_revert()

        # Validate the Draggable function
        self.drag = Draggable(self.driver)
        self.drag.test_open_module()
        self.drag.test_header()
        self.drag.test_open_axis_restricted_tab()
        self.drag.test_only_x()
        self.drag.test_only_y()
        self.drag.test_container_restricted_tab()
        self.drag.test_contained_within_box()
        self.drag.test_contained_within_parent()
        self.drag.test_cursor_style_tab()
        self.drag.test_cursor_center()
        self.drag.test_cursor_top_left()
        self.drag.test_cursor_bottom()
        self.drag.test_simple()
