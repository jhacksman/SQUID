"""Main entry point for SQUID system."""
import asyncio
from squid.vision import ScreenAnalyzer
from squid.actions import ActionExecutor
from squid.llm import LLMInterface

async def main():
    """Initialize and run SQUID system."""
    print("Initializing SQUID for macOS...")

    try:
        # Initialize components
        screen_analyzer = ScreenAnalyzer()
        action_executor = ActionExecutor()
        llm_interface = LLMInterface()

        print("SQUID initialized. Ready for instructions.")

        # TODO: Implement main interaction loop
        # Will implement:
        # 1. Get user instruction
        # 2. Analyze screen with Molmo
        # 3. Process through Nemotron
        # 4. Execute actions

    except Exception as e:
        print(f"Initialization failed: {e}")
        return

if __name__ == "__main__":
    asyncio.run(main())
