
def register_resources(mcp):
    @mcp.resource("docs://observation-guide")
    def eeg_guide() -> str:
        """Provide instructions on how to preprocess EEG data"""
        return """
        EEG Data Preprocessing Guide:
        1. Load the EEG data file using the appropriate format (e.g., EDF, BDF).
        2. Apply filtering to remove noise and artifacts.
        3. Segment the data into epochs if necessary.
        4. Perform artifact rejection to clean the data.
        5. Optionally, apply baseline correction.
        6. Save the preprocessed data for further analysis.
        """