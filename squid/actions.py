"""Action execution module for implementing UI interactions."""
from typing import Dict, Any
import pyautogui

class ActionExecutor:
    """Executes UI actions based on coordinates from Molmo."""

    def __init__(self):
        pyautogui.FAILSAFE = True  # Safety feature for macOS

    async def execute_action(self, action_plan: Dict[str, Any]) -> bool:
        """Execute a planned action using pyautogui."""
        action_type = action_plan.get('type')
        coordinates = action_plan.get('coordinates')

        if not all([action_type, coordinates]):
            return False

        try:
            if action_type == 'click':
                pyautogui.click(coordinates['x'], coordinates['y'])
            elif action_type == 'type':
                pyautogui.typewrite(action_plan.get('text', ''))
            elif action_type == 'move':
                pyautogui.moveTo(coordinates['x'], coordinates['y'])
            return True
        except Exception as e:
            print(f"Action execution failed: {e}")
            return False
