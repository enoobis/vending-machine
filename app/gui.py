from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
import os
import serial
from serial import Serial
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

class MyApp:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r".\assets")
        self.window = Tk()
        self.ser = serial.Serial('COM3', 9600)
        self.window.geometry("500x500")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.create_widgets()
        self.window.resizable(False, False)
        self.update_text()

        self.paymnet_true = False

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def clear_window(self):
        for widget in self.window.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        if self.paymnet_true:
            self.canvas.delete(self.image_3)
            self.paymnet_true = False 


    def back_to_main(self):
        self.clear_window()
        self.create_widgets()

    def create_icecream_widgets(self):
        self.clear_window()
        
        # Create image items
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(152, 71, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(98, 71, image=self.image_image_2)

        # Create buttons
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_main,
            relief="flat"
        )
        self.back_button.place(x=273, y=51, width=150, height=40)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("strawberry_button.png"))
        self.strawberry_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(20, "strawberry_button clicked"),
            relief="flat"
        )
        self.strawberry_button.place(x=273, y=304, width=150, height=150)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("vanilla_button.png"))
        self.vanilla_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(30, "vanilla_button clicked"),
            relief="flat"
        )
        self.vanilla_button.place(x=273, y=114, width=150, height=150)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("chocolate_button.png"))
        self.chocolate_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(40, "chocolate_button clicked"),
            relief="flat"
        )
        self.chocolate_button.place(x=77, y=304, width=150, height=150)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("cream_button.png"))
        self.cream_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(10, "cream_button clicked"),
            relief="flat"
        )
        self.cream_button.place(x=77, y=114, width=150, height=150)

        self.text_obj = self.canvas.create_text(
            114,
            59,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

    def create_drinks_widgets(self):
        self.clear_window()
        
        # Create image items
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(152, 71, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(98, 71, image=self.image_image_2)

        # Create buttons
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_main,
            relief="flat"
        )
        self.back_button.place(x=273, y=51, width=150, height=40)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("pepsi_button.png"))
        self.pepsi_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(20, "pepsi_button clicked"),
            relief="flat"
        )
        self.pepsi_button.place(x=273, y=304, width=150, height=150)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("fanta_button.png"))
        self.fanta_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(30, "fanta_button clicked"),
            relief="flat"
        )
        self.fanta_button.place(x=273, y=114, width=150, height=150)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("cocacola_button.png"))
        self.cocacola_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(40, "cocacola_button clicked"),
            relief="flat"
        )
        self.cocacola_button.place(x=77, y=304, width=150, height=150)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("sprite_button.png"))
        self.sprite_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(10, "sprite_button clicked"),
            relief="flat"
        )
        self.sprite_button.place(x=77, y=114, width=150, height=150)

        self.text_obj = self.canvas.create_text(
            114,
            59,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter", 20 * -1)
        )
  
    def create_teas_widgets(self):
        self.clear_window()
        
        # Create image items
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(152, 71, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(98, 71, image=self.image_image_2)

        # Create buttons
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_main,
            relief="flat"
        )
        self.back_button.place(x=273, y=51, width=150, height=40)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("hotmilk_button.png"))
        self.hotmilk_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(20, "hotmilk_button clicked"),
            relief="flat"
        )
        self.hotmilk_button.place(x=273, y=304, width=150, height=150)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("greentea_button.png"))
        self.greentea_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(30, "greentea_button clicked"),
            relief="flat"
        )
        self.greentea_button.place(x=273, y=114, width=150, height=150)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("chocolate_button.png"))
        self.chocolate_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(40, "chocolate_button clicked"),
            relief="flat"
        )
        self.chocolate_button.place(x=77, y=304, width=150, height=150)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("balcktea_button.png"))
        self.balcktea_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(10, "balcktea_button clicked"),
            relief="flat"
        )
        self.balcktea_button.place(x=77, y=114, width=150, height=150)

        self.text_obj = self.canvas.create_text(
            114,
            59,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

    def create_coffee_widgets(self):
        self.clear_window()
        
        # Create image items
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(152, 71, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(98, 71, image=self.image_image_2)

        # Create buttons
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_main,
            relief="flat"
        )
        self.back_button.place(x=273, y=51, width=150, height=40)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("americano_button.png"))
        self.americano_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(20, "americano_button clicked"),
            relief="flat"
        )
        self.americano_button.place(x=273, y=304, width=150, height=150)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("latte_button.png"))
        self.latte_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(30, "latte_button clicked"),
            relief="flat"
        )
        self.latte_button.place(x=273, y=114, width=150, height=150)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("cappuccino_button.png"))
        self.cappuccino_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(40, "cappuccino_button clicked"),
            relief="flat"
        )
        self.cappuccino_button.place(x=77, y=304, width=150, height=150)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("espresso_button.png"))
        self.espresso_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_on_led_and_buy(10, "espresso_button clicked"),
            relief="flat"
        )
        self.espresso_button.place(x=77, y=114, width=150, height=150)

        self.text_obj = self.canvas.create_text(
            114,
            59,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter", 20 * -1)
        )
    
    def create_payment_widgets(self):
        self.clear_window()

        # Create image items
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(152, 71, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(98, 71, image=self.image_image_2)

        # Create buttons
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_main,
            relief="flat"
        )
        self.back_button.place(x=273, y=51, width=150, height=40)

        # Create text
        self.text_obj = self.canvas.create_text(
            114,
            59,
            anchor="nw",
            text="0",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        # Create QR code image
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("qr.png"))
        self.image_3 = self.canvas.create_image(250, 292, image=self.image_image_3)
        self.paymnet_true = True

    def create_widgets(self):
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(152, 71, image=self.image_image_1)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("payment_button.png"))
        self.payment_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            activebackground="white",
            command=self.create_payment_widgets,
            relief="flat"
        )
        self.payment_button.place(x=273, y=51, width=150, height=40)

        # Create other buttons similarly...

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("icecream_button.png"))
        self.icecream_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            activebackground="white",
            command=self.create_icecream_widgets,
            relief="flat"
        )
        self.icecream_button.place(x=77, y=114, width=150, height=150)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("coffee_button.png"))
        self.coffee_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="white",
            command=self.create_coffee_widgets,
            relief="flat"
        )
        self.coffee_button.place(x=273, y=304, width=150, height=150)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("colddrinks_button.png"))
        self.colddrinks_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            activebackground="white",
            command=self.create_drinks_widgets,
            relief="flat"
        )
        self.colddrinks_button.place(x=273, y=114, width=150, height=150)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("hotdrinks_butto.png"))
        self.hotdrinks_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            activebackground="white",
            command=self.create_teas_widgets,
            relief="flat"
        )
        self.hotdrinks_button.place(x=77, y=304, width=150, height=150)

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(98, 71, image=self.image_image_2)

        self.text_obj = self.canvas.create_text(
            114,
            59,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

    def update_text(self):
        with open(self.OUTPUT_PATH / "data.txt", "r") as file:
            new_text = file.read().strip()
            self.canvas.itemconfig(self.text_obj, text=new_text)
        self.window.after(5000, self.update_text)

    def turn_on_led_and_buy(self, price, button_name):
        with open(self.OUTPUT_PATH / "data.txt", "r") as file:
            data = int(file.read().strip())
            if data >= price:
                # Assuming ser is a global variable or defined elsewhere
                self.ser.write("turn_on_led\n".encode())
                self.check_and_buy(price, button_name)

    
    def check_and_buy(self, price, button_name):
        with open(self.OUTPUT_PATH / "data.txt", "r+") as file:
            data = int(file.read().strip())
            if data >= price:
                file.seek(0)
                file.write(str(data - price))
                file.truncate()
                self.update_text()
                print(button_name)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = MyApp()
    app.run()
