from unittest.mock import patch

import mocks.base.model.AliceSkill as AliceSkill
import mocks.dialog.model.DialogSession as DialogSession
import mocks.util.Decorators as Decorators


class ProjectAliceUnittest:

	def __init__(self):
		patcher = patch.dict(
			'sys.modules',
			{
				'core.base.model.AliceSkill': AliceSkill,
				'core.dialog.model.DialogSession': DialogSession,
				'core.util.Decorators': Decorators
			}
		)
		patcher.start()
