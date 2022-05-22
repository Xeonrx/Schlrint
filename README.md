 ```
    __________
  /_\ _________\       <S C H L R I N T>
|   | SCHLRINT |     ATTENDE GATHERING TOOL
|_H_|__________| [OSINT & INFORMATION GATHERING]
```
>Discover attending students of a given school district with SCHLRINT.<br />
>Results may be based off of students who are currently attending or HAVE attended in the past.


Back in past OSINT investigations, locating a persons education system was sometimes a challenge for me.<br />
Constantly digging through Google dorks, seeing if any name results come up with local school districts.

This script was developed to aid me in google dorking, doing all the work for in searching through results.<br />
SCHLRINT can return found people off a wordlist of names, or I can specify a specifc name to find for me.

I don't see too many 'school based' OSINT scripts/techniques online, so I figured I'd share it with the internet.

## Usage
Usage is pretty straight foward for SCHLRINT. You give a school district, and a location (state/region) if needed.

`python3 Schlrint.py -d SomeSchool -l RandomPlace` *(location isnt required but helps)*

- By default, Schlrint will only return first names. Give the `--full` flag, and it will search for full names.<br />
- Use the `--unique` flag, and Schlrint will ingnore repeated names for an easier output.<br />
- If you want to dig through more results, use the `--deeper` flag, to search even further.

If you must refer to the usage again, just use the `-h` flag, and it will be there for you.

## Configuration
Schlrint is 
