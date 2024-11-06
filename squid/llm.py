"""LLM interface for decision making."""
from typing import Dict, Any, Optional, List, Callable
from dataclasses import dataclass
from enum import Enum

@dataclass
class FunctionCall:
    """Represents a function call from the LLM."""
    name: str
    arguments: Dict[str, Any]

class ActionType(Enum):
    """Types of actions that can be performed."""
    CLICK = "click"
    TYPE = "type"
    READ = "read"
    MOVE = "move"
    WAIT = "wait"
    NO_OP = "no_op"

class LLMInterface:
    """Interface for Nemotron-based decision making."""

    def __init__(self):
        # TODO: Initialize Nemotron connection
        # Will be implemented once we have access to Nemotron
        self._function_registry: Dict[str, Callable] = {}
        self._register_functions()

    def _register_functions(self):
        """Register available functions for LLM to call."""
        self._function_registry.update({
            'find_element': self._find_element,
            'click_element': self._click_element,
            'type_text': self._type_text,
            'read_text': self._read_text,
            'wait': self._wait
        })

    async def process_instruction(
        self,
        instruction: str,
        vision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process user instruction with vision context."""
        try:
            # Prepare context for LLM
            formatted_context = self._prepare_context(instruction, vision_data, context)

            # Get LLM response with function calling
            function_calls = await self._get_llm_response(formatted_context)

            # Execute function calls
            results = []
            for call in function_calls:
                if call.name in self._function_registry:
                    result = await self._function_registry[call.name](**call.arguments)
                    results.append(result)

            return {
                'type': ActionType.NO_OP if not results else results[-1]['type'],
                'results': results
            }

        except Exception as e:
            return {
                'type': ActionType.NO_OP,
                'reason': f'Error processing instruction: {str(e)}'
            }

    async def _get_llm_response(self, context: Dict[str, Any]) -> List[FunctionCall]:
        """Get response from LLM with function calling."""
        # TODO: Implement actual LLM call with function definitions
        # This will:
        # 1. Format function definitions
        # 2. Make LLM API call
        # 3. Parse response into FunctionCall objects
        return []

    def _prepare_context(
        self,
        instruction: str,
        vision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Prepare context for LLM processing."""
        return {
            'instruction': instruction,
            'screen_state': vision_data,
            'context': context or {},
            'available_functions': list(self._function_registry.keys())
        }

    async def _find_element(self, description: str) -> Dict[str, Any]:
        """Find UI element based on description."""
        # TODO: Implement element search using MOLMO
        return {'type': ActionType.NO_OP}

    async def _click_element(self, element_id: str) -> Dict[str, Any]:
        """Click on identified UI element."""
        # TODO: Implement click action using MOLMO coordinates
        return {'type': ActionType.CLICK}

    async def _type_text(self, element_id: str, text: str) -> Dict[str, Any]:
        """Type text into identified UI element."""
        # TODO: Implement text input action
        return {'type': ActionType.TYPE}

    async def _read_text(self, element_id: str) -> Dict[str, Any]:
        """Read text from identified UI element."""
        # TODO: Implement text extraction using MOLMO
        return {'type': ActionType.READ}

    async def _wait(self, milliseconds: int) -> Dict[str, Any]:
        """Wait for specified duration."""
        # TODO: Implement wait action
        return {'type': ActionType.WAIT}
