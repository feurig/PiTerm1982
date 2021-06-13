# PiTerm1986
**GOAL:** Convert 80s style user interface ( 8031 based ADP Product: chicklet keyboard and 2x20 lcd ) to pi zero based terminal using i2c based io expanders.

![](images/IMG_3780.jpg)
![](images/IMG_3784.jpg)
![](images/IMG_3783.jpg)
![](images/IMG_3782.jpg)
![](images/IMG_3781.jpg)

Looking under the keyboard membrane and tracing the connectors we can get the following key map under a 4x12 array (16 pins).

<table>
<tr><td>*</td><td>#</td><td> </td><td>Z</td><td>X</td><td>C</td><td>V</td><td>B</td><td>N</td><td>M</td><td>/</td><td>STOP</td></tr>
<tr>
<td>&#45;</td><td>L</td><td>A</td><td>S</td><td>D</td><td>F</td><td>G</td><td>H</td><td>J</td><td>K</td><td>N/C</td><TD>ENTER</TD></tr>
<tr>
<td>0</td><td>9</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>&LT;----</td><td>START</td></tr>
<tr>
<td>P</td><td>O</td><td>Q</td><td>W</td><td>E</td><td>R</td><td>T</td><td>Y</td><td>U</td><td>I</td><td>CANCEL</td><td>DIAL</td></tr>
</table>
### Keyboard

![](images/IMG_3779.jpg)

For this we look at the AW9523 GPIO expander with 16 pins of io.

### LCD/VFD 

Since the LCD is a 5v circuit requiring either 8 or 12 pins we look at the Microchip MCP23017 on the Adafruit GPIO Expander Bonnet. 


