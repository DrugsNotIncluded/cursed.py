<div align="center">
    <h1>Cursed.py ⚒️</h1>
    <img width="64px" alt="icon" src="./curseforge.png">
</div>

[![PyPI version](https://badge.fury.io/py/cursedpy.svg)](https://badge.fury.io/py/cursedpy)

About:
---
Full **Curseforge API** wrapper<br> 
👉 https://docs.curseforge.com<br>
```
All Json Schemas (Python Types) are exactly the same as in docs
Except missing "Return types" which are essentially just this: {"data": Any} or this {"data": Any, "pagination": Pagination}
```

Usage examples:
---
- [Search mods](./examples/search_mods/README.MD)
- [~~Get curseforge supported games list~~](./examples/games_list/README.md) **TODO**
- [~~Get mods download links~~](./examples/mods_download_links/README.md) **TODO**

Implemented API:
---
- [x] Games
- [x] Categories
- [x] Mods
- [x] Files
- [x] Fingerprints
- [x] Minecraft

TODO:
- [ ] Partially rewrite with `requests.Session()`
- [ ] Add native async support

QOL:
---
- [ ] Error handling
- [ ] Document all types parameters
- [ ] Make proper docs page???
