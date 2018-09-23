"""Example moduel for Sopel

This is just to learn some of the commands
"""

import sopel.module

@sopel.module.commands('helloworld', 'hw')
def helloworld(bot, trigger):
	bot.say('Hello, world!')

@sopel.module.commands('echo', 'repeat')
def echo(bot, trigger):
	    bot.reply(trigger.group(2))
