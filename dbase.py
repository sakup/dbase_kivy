from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    """docstring for StudentListButton."""
    pass

class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):
        pass

    def delete_student(self):
        pass

    def replase_student(self):
        pass

class StudentDBApp(App):
    def build(self):
        return StudentDbase()

StudentDBApp().run()