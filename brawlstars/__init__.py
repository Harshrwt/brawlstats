from .brawlstats import brawlstars


def setup(bot):
    bot.add_cog(brawlstars())
