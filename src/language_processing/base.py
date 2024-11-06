"""Base interfaces for language model integration."""
from abc import ABC, abstractmethod
from typing import AsyncIterator, Dict, List, Optional, Union
from dataclasses import dataclass

@dataclass
class Message:
    """Represents a message in a conversation."""
    role: str
    content: str
    metadata: Optional[Dict] = None

@dataclass
class ModelResponse:
    """Represents a response from a language model."""
    content: str
    metadata: Optional[Dict] = None
    confidence: float = 1.0

class BaseModelInterface(ABC):
    """Abstract base class for model interfaces."""

    @abstractmethod
    async def generate(
        self,
        prompt: Union[str, List[Message]],
        stop: Optional[List[str]] = None,
        **kwargs
    ) -> ModelResponse:
        """Generate response from model.

        Args:
            prompt: Input prompt as string or list of messages
            stop: Optional list of stop sequences
            **kwargs: Additional model-specific parameters

        Returns:
            ModelResponse containing generated content and metadata
        """
        pass

    @abstractmethod
    async def stream(
        self,
        prompt: Union[str, List[Message]],
        stop: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterator[ModelResponse]:
        """Stream response from model.

        Args:
            prompt: Input prompt as string or list of messages
            stop: Optional list of stop sequences
            **kwargs: Additional model-specific parameters

        Yields:
            ModelResponse chunks as they are generated
        """
        pass
