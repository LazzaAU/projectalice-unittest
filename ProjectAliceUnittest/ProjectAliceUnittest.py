from unittest.mock import MagicMock, patch

class ProjectAliceUnittest:
	patch('core.base.model.AliceSkill.AliceSkill', return_value='a')
