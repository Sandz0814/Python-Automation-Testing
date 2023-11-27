import pytest
from Tools.function import BaseDriver
from aWidgetsPageObject.accordian_page import Widgets
from aWidgetsPageObject.auto_complete_page import AutoComplete
from aWidgetsPageObject.date_picker_page import DatePicker
from aWidgetsPageObject.menu_page import Menu
from aWidgetsPageObject.progress_bar_page import ProgressBar
from aWidgetsPageObject.select_menu_page import SelectMenu
from aWidgetsPageObject.slider_page import Slider
from aWidgetsPageObject.tabs_page import Tabs
from aWidgetsPageObject.tool_tip_page import ToolTip


@pytest.mark.usefixtures("setup")
class TestWidgets(BaseDriver):

    def test_accordion(self):
        self.page_scroll()

        # Validate the Accordion function
        self.widgets = Widgets(self.driver)
        self.widgets.test_click_widgets_icon()
        self.widgets.test_open_accordian_module()
        self.widgets.test_header_main()
        self.widgets.test_accordion1_header()
        self.widgets.test_accordion2_header()
        self.widgets.test_accordion3_header()

        # Validate the Autocomplete function
        self.ac = AutoComplete(self.driver)
        self.ac.test_open_module()
        self.ac.test_header()
        self.ac.test_multiple_color_input()
        self.ac.test_single_color_input()

        # Validate the Date Picker function
        self.dp = DatePicker(self.driver)
        self.dp.test_open_tab()
        self.dp.test_header()
        self.dp.test_select_date()
        self.dp.test_date_and_time()
        self.dp.test_date_time_input()

        # Validate the Slider function
        self.slider = Slider(self.driver)
        self.slider.test_open_slider_module()
        self.slider.test_header()
        self.slider.test_slider()

        # Validate the Progress Bar function
        self.pb = ProgressBar(self.driver)
        self.pb.test_progress_bar()
        self.pb.test_header()
        self.pb.test_start_btn()

        # Validate the Tabs function
        self.tabs = Tabs(self.driver)
        self.tabs.test_tab_module()
        self.tabs.test_what()
        self.tabs.test_origin()
        self.tabs.test_use()

        # Validate the Tooltip function
        self.tt = ToolTip(self.driver)
        self.tt.test_tool_tip_module()
        self.tt.test_hover_me()
        self.tt.test_contrary()
        self.tt.test_section()

        # Validate the Menu function
        self.menu = Menu(self.driver)
        self.menu.test_menu_tab()
        self.menu.test_header()
        self.menu.test_menu2()
        self.menu.test_menu1()
        self.menu.test_menu3()

        # Validate tje Select Menu function
        self.sm = SelectMenu(self.driver)
        self.sm.test_open_select_menu()
        self.sm.test_header()
        self.sm.test_select_value()
        self.sm.test_select_one()
        self.sm.test_old_select_menu()
        self.sm.test_multi_dropdown()
        self.sm.test_standard_multi_select()


