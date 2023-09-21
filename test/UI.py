import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Social Car Club", width=350, height=250):
    dpg.add_text("Velkommen til Social Car Club\n\n"
                 "Venligst logg inn med brukernavn og passord")
    dpg.add_child_window(label="login")



dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
