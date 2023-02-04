# Virtual Kabbage :leafy_green: - A virtual-keyboard generator for eScriptorium

## Usage

Install dependencies in a virtual environment with pip (`pip install -r requirements.txt`) and run `cook.py` providing up to three arguments:

- `-i` : (required) path to CSV file used to generate the virtual keyboard (sep must be `,`!).
- `-auth` : (opt) allows you to add a value to the "author" field in the final JSON file.
- `-k` : (opt) allows you to specify a value for the "name" field in the final JSON file.

## Examples

``` sh
$ python cook.py -i test/test.csv
>>> ...
    "version": "0.1",
    "name": "test",
    "author": "Virtual Kabbage",
    "characters": [
    ...
```

```sh
$ python cook.py -i test/test.csv -auth "Jane Doe <jane.doe@example.com>"

>>> ...
    "version": "0.1",
    "name": "test",
    "author": "Virtual Kabbage & Jane Doe <jane.doe@example.com>",
    "characters": [
    ...
```

```sh
$ python cook.py -i test/test.csv -auth "Jane Doe <jane.doe@example.com>" -k "my nice keyboard"

>>> ...
    "version": "0.1",
    "name": "my nice keyboard",
    "author": "Virtual Kabbage & Jane Doe <jane.doe@example.com>",
    "characters": [
    ...
```





## Expected mapping

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
    "author": "Virtual Kabbage",
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
