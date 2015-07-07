#python
#coding=utf-8
from uiLoader import GtkLoader
from model import Model
from calculator import ConnectView
from gi.repository import Gdk, Gtk

class MainWindow(GtkLoader):
    def __init__(self):
        GtkLoader.__init__(self, filename="ui/calculator.glade")

        self._calculator.set_title("简易计算器")
        self._calculator.show_all()
        self._model = Model()
        self.algorithm = ConnectView(self._model)

        self._one.connect("button_press_event", self.one_button_on_press)
        self._two.connect("button_press_event", self.two_button_on_press)
        self._three.connect("button_press_event", self.three_button_on_press)
        self._four.connect("button_press_event", self.four_button_on_press)
        self._five.connect("button_press_event", self.five_button_on_press)
        self._six.connect("button_press_event", self.six_button_on_press)
        self._seven.connect("button_press_event", self.seven_button_on_press)
        self._eight.connect("button_press_event", self.eight_button_on_press)
        self._nine.connect("button_press_event", self.nine_button_on_press)
        self._zero.connect("button_press_event", self.zero_button_on_press)

        self._plus.connect("button_press_event", self.puls_button_on_press)
        self._reduction.connect("button_press_event", self.reduct_button_on_press)
        self._multiply.connect("button_press_event", self.mul_button_on_press)
        self._divsion.connect("button_press_event", self.divsion_button_on_press)

        self._equ.connect("button_press_event", self.equ_button_on_press)
        self._result.connect("activate", self.equ_enter_button)
        self._result.connect("button_press_event", self.equ_button_press)

        self._leftbracket.connect("button_press_event", self.left_button_on_press)
        self._rightbracket.connect("button_press_event", self.right_button_on_press)
        self._clear.connect("button_press_event", self.clear_button_on_press)
        self._back.connect("button_press_event", self.back_button_on_press)
        self._point.connect("button_press_event", self.point_button_on_press)

        self._model.on_trait_change(self.update_display, "result")
        self._result.set_text("0")
        self._result.set_alignment(1)

    def equ_button_press(self, widget, event):
        if widget.get_text() == "0":
            self._model.result = ""
        widget.set_text(self._model.result)

    def equ_enter_button(self, widget):
        self._model.result = self._result.get_text()
        self.algorithm.calculator()

    def point_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.point)

    def back_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self._model.result = self._model.result[:-1]

    def clear_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self._model.result = '0'

    def left_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.leftBracket)

    def right_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.rightBracket)

    def update_display(self, value):
        self._result.set_text(value)

    def puls_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.plus)
        self._model.isClear = False

    def reduct_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.reduct)
        self._model.isClear = False

    def mul_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.mul)
        self._model.isClear = False

    def divsion_button_on_press(self, widget, event):
        self._model.result = self._result.get_text()
        self.change_result(self._model.divsion)
        self._model.isClear = False

    def equ_button_on_press(self, widget, event):
        self._model.isClear = True
        self.algorithm.calculator()

    def one_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.one)
        self._model.isClear = False

    def two_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.two)
        self._model.isClear = False

    def three_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.three)
        self._model.isClear = False

    def four_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.four)
        self._model.isClear = False

    def five_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.five)
        self._model.isClear = False

    def six_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.six)
        self._model.isClear = False

    def seven_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.seven)
        self._model.isClear = False

    def eight_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.eight)
        self._model.isClear = False

    def nine_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.nine)
        self._model.isClear = False

    def zero_button_on_press(self, widget, event):
        self.get_value_in_entry()
        self.change_result(self._model.zero)
        self._model.isClear = False

    def change_result(self, value):
        self._model.result = self._model.result + value

    def get_value_in_entry(self):
        if self._model.isClear is True:
            self._model.result = ''
            return

        if self._result.get_text() == '0':
            self._model.result =""
        else:
            self._model.result = self._result.get_text()

def startup():
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path("./theme/gtk.css")
    screen = Gdk.Screen.get_default()
    Gtk.StyleContext.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    window = MainWindow()
    Gtk.main()

if __name__ == '__main__':
    startup()