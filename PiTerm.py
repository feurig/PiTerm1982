keymap=[]
keymap.append('*# ZXCVBNM/\001')
keymap.append('-LASDFGHJK\r\n')
keymap.append('0912345678\010\002')
keymap.append('POQWERTYUI\030\004')

import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 24
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.message = "Hello\nCircuitPython"
