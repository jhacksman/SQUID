"""Context management system for language processing."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from .base import Message

@dataclass
class MemoryEntry:
    """Represents a single memory entry."""
    content: str
    timestamp: float
    metadata: Optional[Dict] = None
    importance: float = 1.0

class ContextManager:
    """Manages context and memory for language processing."""

    def __init__(self, max_context_size: int = 4096):
        self.max_context_size = max_context_size
        self.short_term_memory: List[MemoryEntry] = []
        self.working_memory: Dict[str, Any] = {}
        self.conversation_history: List[Message] = []

    async def update_context(
        self,
        new_context: Dict[str, Any]
    ) -> None:
        """Update working memory with new context.

        Args:
            new_context: Dictionary of new context variables
        """
        self.working_memory.update(new_context)

    async def add_memory(
        self,
        content: str,
        metadata: Optional[Dict] = None,
        importance: float = 1.0
    ) -> None:
        """Add new memory entry.

        Args:
            content: Content to remember
            metadata: Optional metadata
            importance: Importance score (0-1)
        """
        import time
        entry = MemoryEntry(
            content=content,
            timestamp=time.time(),
            metadata=metadata,
            importance=importance
        )
        self.short_term_memory.append(entry)
        self._prune_memory()

    async def get_relevant_context(
        self,
        query: str,
        max_items: int = 5
    ) -> List[MemoryEntry]:
        """Get most relevant memories for query.

        Args:
            query: Search query
            max_items: Maximum items to return

        Returns:
            List of relevant memory entries
        """
        # Simple importance-based retrieval for now
        # Will be enhanced with semantic search in future
        sorted_memories = sorted(
            self.short_term_memory,
            key=lambda x: x.importance,
            reverse=True
        )
        return sorted_memories[:max_items]

    def _prune_memory(self) -> None:
        """Remove old or less important memories when exceeding context size."""
        if len(self.short_term_memory) > self.max_context_size:
            # Sort by importance and recency
            sorted_memories = sorted(
                self.short_term_memory,
                key=lambda x: (x.importance, x.timestamp),
                reverse=True
            )
            self.short_term_memory = sorted_memories[:self.max_context_size]
