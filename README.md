# game-db

I can't seem to find a good product that will let me keep a database of all the games I own, including console, and being able to sort them on various criteria.

This project aims to fill that gap.

## FAQ

### Which APIs are used to gather data?

Media Type | Source | Implemented?
----|----|----
**Video Games** | [IGDB](https://api-docs.igdb.com) | *In Progress*
Steam | [Steam API](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0001.29) | No
Nintendo Switch | [Nintendo Switch Rest API](https://dev.to/mathewthe2/intro-to-nintendo-switch-rest-api-2cm7) | No
Playstation Network | [PSNAWP](https://pypi.org/project/PSNAWP) | No
GOG | [GOG API](https://gogapidocs.readthedocs.io/en/latest/) | No
Xbox Live | [XSAPI](https://learn.microsoft.com/en-us/gaming/gdk/_content/gc/reference/live/rest/uri/profilev2/uri-usersuseridprofilesettingspeopleuserlistget) | No
Epic Games | [EOS SDK API](https://dev.epicgames.com/docs/en-US/api-ref) | No
Rockstar Games | [R* Social Club API](https://rockstar-api.readthedocs.io/en/latest) | No
Board Games | [Board Game Geek API](https://boardgamegeek.com/wiki/page/BGG_XML_API2) | No

### What are your future plans?

Some future features include:

- Ratings
- Comments
- Custom fields
- Wish lists
  - Creation
  - Sharing
  - Price hunting (looking for sales)
- Game suggestions
- Web interface
- ???
