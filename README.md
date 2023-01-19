# Satisfactory-Logistics-Planner
A python-based GUI for visualizing the production tree of an item of your choosing from the game "Satisfactory" (early access, update 7).  
The current version contains **no alternate recipes**.

Image source: https://satisfactory.fandom.com/wiki/Satisfactory_Wiki (Jan, 2023)
### Requirements:
```
python==3.7
pyqt5==5.15
pandas==0.24
```
### Usage:
Select your current ingame progress with the 8 available tier buttons. Enter an item in the search bar titled 'Item Name'. Available items depend on the selected tier. The 'Target' defines how much of that item you want per minute. All required basic resources are listed under the target. The display in the middle is non-interactable aside from possible scrollbars on the edges. Douplicate items are combined at their earliest occurence to increase readability. Pressing the 'Clear' button clears the current item and its production tree.
### Possible new features:
-resizable production tree widgets  
-save/load configuration  
-implementation of alternate recipes
