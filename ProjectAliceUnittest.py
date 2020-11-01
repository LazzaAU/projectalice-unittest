import importlib
import inspect
from unittest.mock import patch

import mocks.base.model.AliceSkill as AliceSkill
import mocks.base.SuperManager as SuperManager
import mocks.dialog.model.DialogSession as DialogSession
import mocks.util.Decorators as Decorators


class ProjectAliceUnittest:

	def __init__(self):
		patcher = patch.dict(
			'sys.modules',
			{
				'core.base.model.AliceSkill': AliceSkill,
				'core.dialog.model.DialogSession': DialogSession,
				'core.util.Decorators': Decorators,
				'core.base.SuperManager': SuperManager
			}
		)
		patcher.start()


	@property
	def start(self):
		# Init the skill we are testing
		try:
			caller = inspect.getmodulename(inspect.stack()[1][1])
			skillName = caller.replace('test_', '')
			skillImport = importlib.import_module(f'{skillName}')
			klass = getattr(skillImport, skillName)
			return klass()
		except:
			print("Couldn't import skill to test")


	@classmethod
	def SuperManager(cls): #NOSONAR
		return SuperManager.SuperManager(**{
			'talkManager.randomTalk.return_value': 'unittest',
			'languageManager.activeLanguage.return_value': 'en',
			'languageManager.supportedLanguages.return_value': ['en']
		})
