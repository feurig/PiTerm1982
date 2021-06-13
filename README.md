# PiTerm1986
**GOAL:** Convert 80s style user interface ( 8031 based ADP Product: chicklet keyboard and 2x20 lcd ) to pi zero based terminal using i2c based io expanders.

![](images/IMG_3780.jpg)
![](images/IMG_3784.jpg)
![](images/IMG_3783.jpg)
![](images/IMG_3782.jpg)
![](images/IMG_3781.jpg)

Looking under the keyboard membrane and tracing the connectors we can get the following key map under a 4x12 array (16 pins).

```
   0123456789A    B
  --------------------
0) *# ZXCVBNM/    <STOP>
1) -LASDFGHJK<?>  <ENTER>
2) 0912345678<BS> <START>
2) POQWERTYUI<CAN><DIAL>
```
### Keyboard

![](images/IMG_3779.jpg)

For this we look at the AW9523 GPIO expander with 16 pins of io.

### LCD/VFD 

Since the LCD is a 5v circuit requiring either 8 or 12 pins we look at the Microchip MCP23017 on the Adafruit GPIO Expander Bonnet. 


