"""LLM interface for decision making."""
from typing import Dict, Any, Optional

class LLMInterface:
    """Interface for Nemotron-based decision making."""

    def __init__(self):
        # TODO: Initialize Nemotron connection
        # Will be implemented once we have access to Nemotron
        pass

    async def process_instruction(
        self,
        instruction: str,
        vision_data: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process user instruction with vision context."""
        # TODO: Implement Nemotron processing pipeline
        # Will implement:
        # 1. Context preparation
        # 2. Instruction formatting
        # 3. LLM query
        # 4. Response parsing

        return {
            'type': 'no_op',
            'reason': 'LLM integration pending'
        }
