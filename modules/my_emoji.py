import re
import unicodedata
from sopel.module import rule, priority

unicode_range="[\U00000b20-\U00002017\U00002020-\U00002025\U00002027-\U0001f9dd]"
unicode_space="[\U00000020]"

def translate_emoji(matchobj):
	unicode_point = matchobj.group(0)
	try:
		return '(' + unicodedata.name(unicode_point).lower() + ')'
	except ValueError:
		print("Unknown unicode point: ", unicode_point)
		return '(unknown)'

@rule('.*')
@priority('high')
def find_emoji(bot, trigger):
	line = trigger.group()
	if re.match('.*' + unicode_range + '+.*', line):
		bot.say(re.sub(unicode_range, translate_emoji, line))
	# elif re.match('^' + unicode_space + '*$', line) and trigger.nick == "aam":
	# 	bot.say(re.sub(unicode_space, translate_emoji, line))
