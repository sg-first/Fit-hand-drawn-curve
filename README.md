Fit hand-drawn curve
===========
It can convert the curve you draw on the coordinate diagram manually into a smooth coordinate sequence.

How to use
----------
* On a picture of the same size as the example picture(`test.png`), use a brush of the same color as the example picture(red) to draw your curve
* Specify `xStart`(X value of starting point of you drawn curve), `yKnow`(Y value of the point that closest to 0 on the Y axis of the coordinate diagram border), `yknowVal`(coordinate diagram Y value on the graph of that point), `dayEnd`(coordinate diagram X value of you drawn curve) variable value. For example `yknowVal=10` in `test.png`

**Note:** If the relative position of your picture and coordinate diagram is sufficient from `test.png`, then other variables need to be adjusted.

* Run `main.py`

How it work
----------
The program will extract the coordinate points you draw as much as possible, and then fit a cubic spline function based on these coordinate points. Then find the coordinates of each integer point from `dayStart` (coordinate diagram X value of `xStart`) to `dayEnd`.
