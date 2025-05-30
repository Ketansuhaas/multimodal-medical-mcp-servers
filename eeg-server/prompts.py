def register_prompts(mcp):
    @mcp.prompt()
    def get_eeg(eeg_path: str) -> str:
        """
        Prompt for the path to the EEG data file."""
        return f"""Here is the path to the EEG data file: {eeg_path}. Use this."""

    