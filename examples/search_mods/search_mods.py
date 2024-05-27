import asyncio

# For output coloring
from colorama.Fore import GREEN, BLUE, MAGENTA
from colorama.Style import RESET_ALL

# Cursed.py
from cursedpy import CFClient
from cursedpy import ModLoaderType

API_KEY = "YOURS_CURSEFORGE_API_KEY"
"""
Which you definitely can't get by any other means other than asking for it on: https://support.curseforge.com/en/support/solutions/articles/9000208346-about-the-curseforge-api-and-how-to-apply-for-a-key

You definitely can't and should't use example CF key from sourcecode, neither you should try to extract it from curseforge Overwolf client lying on webarchive with some magic linux tools, nor you can't look for it on https://cf.polymc.org/api

Yeah, don't do it. :^)
"""

async def main():
    try:
        CursedClient = CFClient(API_KEY)
        mods, pagination = await CursedClient.Mods.search_mods(
            432,
            modLoaderType=ModLoaderType.NeoForge, # Modloader
            gameVersion='1.20.1',                 # Game Version
            searchFilter="Create"                 # Free search
            )
    finally:
        CursedClient.close()

    for mod in mods:
        for category in mod.categories:
            if category.slug == "mc-addons": # Category slug
                print(
                    f'''
                    Mod: {BLUE}{mod.name}{RESET_ALL}
                    Rating: {GREEN}{mod.rating}{RESET_ALL}
                    Likes: {GREEN}{mod.thumbsUpCount}{RESET_ALL}
                    Downloads: {GREEN}{mod.downloadCount}{RESET_ALL}
                    Links:
                        {MAGENTA}Website:{RESET_ALL} {mod.links.websiteUrl}
                        {MAGENTA}Source:{RESET_ALL} {mod.links.sourceUrl}
                        {MAGENTA}Wiki:{RESET_ALL} {mod.links.wikiUrl}
                    Description (HTML): {mod.summary}\n
                    '''
                )
                break
asyncio.run(main())