import mne

def register_tools(mcp):

    @mcp.tool(name="get_channel_names", description="Get channel names from a .set file")
    def get_channel_names(file_path: str) -> list:
        """Get channel names from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "channel names" : raw.ch_names
        }
    @mcp.tool(name="get_sampling_rate", description="Get sampling rate from a .set file")
    def get_sampling_rate(file_path: str) -> float:
        """Get sampling rate from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "sampling_rate": raw.info['sfreq']
        }
    @mcp.tool(name="get_data_shape", description="Get data shape from a .set file")
    def get_data_shape(file_path: str) -> dict:
        """Get data shape from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "data_shape": raw.get_data().shape
        }
    @mcp.tool(name="get_data", description="Get data from a .set file")
    def get_data(file_path: str, picks=None, start=0, stop=None) -> dict:
        """Get data from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        data, times = raw[picks, start:stop]
        return {
            "data": data.tolist(),
            "times": times.tolist()
        }
    @mcp.tool(name="get_info", description="Get info from a .set file")
    def get_info(file_path: str) -> dict:
        """Get info from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "info": raw.info
        }
    @mcp.tool(name="get_annotations", description="Get annotations from a .set file")
    def get_annotations(file_path: str) -> dict:
        """Get annotations from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "annotations": raw.annotations.tolist()
        }
    @mcp.tool(name="get_montage", description="Get montage from a .set file")
    def get_montage(file_path: str) -> dict:
        """Get montage from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        montage = raw.get_montage()
        if montage is not None:
            return {
                "montage": montage.to_dict()
            }
        else:
            return {
                "montage": None
            }
    @mcp.tool(name="get_dig_points", description="Get dig points from a .set file")
    def get_dig_points(file_path: str) -> dict:
        """Get dig points from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        dig = raw.info['dig']
        if dig is not None:
            return {
                "dig": [d.to_dict() for d in dig]
            }
        else:
            return {
                "dig": None
            }
    @mcp.tool(name="get_channel_types", description="Get channel types from a .set file")
    def get_channel_types(file_path: str) -> dict:
        """Get channel types from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "channel_types": raw.get_channel_types()
        }
    @mcp.tool(name="get_channel_units", description="Get channel units from a .set file")
    def get_channel_units(file_path: str) -> dict:
        """Get channel units from a .set file."""
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
        return {
            "channel_units": raw.get_channel_units()
        }
    
    