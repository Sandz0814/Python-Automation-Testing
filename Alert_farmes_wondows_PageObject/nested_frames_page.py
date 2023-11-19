from Tools.function import BaseDriver


class NestedFrames(BaseDriver):
    nested_frames_btn = "//span[normalize-space()='Nested Frames']"

    def __init__(self, driver):
        self.driver = driver




