import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import adafruit_aw9523

keymap=[]
keymap.append('*# ZXCVBNM/\001')
keymap.append('-LASDFGHJK\r\n')
keymap.append('0912345678\010\002')
keymap.append('POQWERTYUI\030\004')

lcd_columns = 24
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.message = "PiTerm 1986 v0.0\nOk >"

aw = adafruit_aw9523.AW9523(i2c)
row_pins = [aw.get_pin(8),aw.get_pin(9),aw.get_pin(10),aw.get_pin(11)]
for pin in row_pins:
   pin.switch_to_output(value=True)

col_pins = [aw.get_pin(0),aw.get_pin(15),aw.get_pin(14),aw.get_pin(13),
            aw.get_pin(12),aw.get_pin(7),aw.get_pin(6),aw.get_pin(5),
            aw.get_pin(4),aw.get_pin(3),aw.get_pin(2),aw.get_pin(1)]

for pin in col_pins:
   pin.switch_to_input(value=True)


old_row=0;
for pin in row_pins:
    pin.value=1

while True:
    for r in range(4):
        row_pins[old_row].value=1
        row_pins[r].value=0
        old_row=r
        for c in range(12):
            if (col_pins[c].value==0):
                print(keymap[r][c])
