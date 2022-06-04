 ```
    __________
  /_\ _________\       <S C H L R I N T>
|   | SCHLRINT |     ATTENDE GATHERING TOOL
|_H_|__________| [OSINT & INFORMATION GATHERING]
```

<p align="center">
  <img width="600" height="500" src="https://github.com/Xeonrx/Schlrint/blob/main/img/sample.png">
</p>
>Discover attending students of a given school district with SCHLRINT.<br />
>Results may be based off of students who are currently attending or HAVE attended in the past.


Back in past OSINT investigations, locating a persons school/education was sometimes a challenge for me.<br />
Constantly digging through Google dorks, seeing if any name results come up with local school districts.

This script was developed to aid me in google dorking, doing all the work for in searching through results.<br />
SCHLRINT can return found people off a wordlist of names, or I can specify a specifc name to find for me.

I don't see too many 'school based' OSINT scripts/techniques online, so I figured I'd share it with the internet.<br />
*Note: Full preview cannot be shown for the respect of others privacy.*

## Usage
Usage is pretty straight foward for SCHLRINT. You give a school district, and a location (state/region) if needed.

`python3 Schlrint.py -d SomeSchool -l RandomPlace` *(location isnt required but helps)*

- By default, Schlrint will only return first names. Give the `--full` flag, and it will search for full names.
- Use the `--unique` flag, and Schlrint will ingnore repeated names for an easier output.
- If you want to dig through more results, use the `--deeper` flag, to search even further.
- To search for specific 'targets', use the `-t` flag along with given names.
- To output your findings into a file, use the `-o` flag, along with the file name.

If you must refer to the usage again, just use the `-h` flag, and it will be there for you.

## Configuration
Schlrint is already all set up for you, but if you really want to reconfigure it, read this.
- `FIRST.txt` is the file searched through to find first names.
- `LAST.txt` these are the last names. They are added onto every first name, and checked for results.
- `QUERY.txt` the content in this file helps return results by google dorking common school activties.

Every one of these files are easily editable. You can add more content for more accuracy, or even remove content.<br />
Just know adding more content will make the process longer to complete, but maybe time isn't a problem :)

## Disclaimer & License
Just know the intent of SCHLRINT is for OSINT. Not to help dox anyone, nor to harrass people.<br />
Please stay right, and in the legal bounds of things.

and **PLEASE** don't rely on this script for a guarenteed answer. Checking Manually is always better!

*This script uses the MIT License. Read more about it here: https://opensource.org/licenses/MIT*
