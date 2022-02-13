# Schlrint
When tracing a target, confirming the school they attend to could lead to another handful of information. <br />
Use the guidance of this script to give you a hand in digging through school districts, using your targets name. <br />

With the use of a general neighborhood/city + a target name, Schlrint can scan though districts searching for attended students.
You can find a good bunch of possible school districts in a city with a simple google search. It's best to make more educated guesses
to save time. <br />

# The Point?
Locating your target's school district isn't neccessary, but can serve some use, if serious about gathering information.
Find possible; class information, hobbies, photos, acquaintances, and more with the use of knowing an attended school.
It could also catagorize their home in a smaller area or region of a city, if that's what you're looking for.

Yeah, this may seem a little extra or far fetched. But sometimes, it could be the best shot to a new foothold of information.

# Usage?
Schlrint works by google dorking the given school district and fetching full names off any related website it could find.
By default, it will scrape any name it can find off a list of the most common names. You can sped up the script by lowering
the amount of results, or make it more accurate *(but longer)* by searching for more results. 
```
-d --district | School district to analyze.  (REQUIRED)
-l --location | Specify a location for a more percise search.
-t --target   | Checks for specified names only.  

-F --firstnames | Use a custom list of firstnames for big lists.
-L --lastnames  | Use a custom list of lastnames for big lists.
-Q --queries    | Use a custom list for query searches.

-m --max | Max amount of scrapped names.
--full   | Scrape full names only. (Will only scrape firstnames by default)
--unique | Disposes of matching names before displaying.
--deeper | Dig through more results for a more accurate search.
```
> You can use the --full tag with given first names (-t), to find every surname of the names you specified.
