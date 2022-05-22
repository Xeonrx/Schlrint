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
Usage is pretty straight foward for SCHLRINT. You give a school district, and a location (state/region) if needed.<br />
`python3 Schlrint.py -d SomeSchool -l RandomPlace` *(location isnt required but helps)*
