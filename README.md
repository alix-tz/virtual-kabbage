# Virtual Kabbage :leafy_green: - A virtual-keyboard generator for eScriptorium

Input: `my_kbd.csv`

``` csv
a,b,c
d,,
```

Output: `my_kbd.json`

``` json
{
    "version": "0.1",
    "name": "my_kbd",
    "author": "Virtual-Kabbage",
    "characters": [
        {
            "row": 0,
            "column": 0,
            "character": "a",
            "keyboard_code": null
        },
        {
            "row": 0,
            "column": 1,
            "character": "b",
            "keyboard_code": null
        },
        {
            "row": 0,
            "column": 3,
            "character": "c",
            "keyboard_code": null
        },
        {
            "row": 1,
            "column": 0,
            "character": "d",
            "keyboard_code": null
        }
    ]
}
```
