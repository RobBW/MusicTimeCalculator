# Helper function to parse time string (extracted from TimeCalc.py)
def parse_time(text):
    if not text:
        return None
    clean_val = text.strip()
    try:
        if "." in clean_val:
            parts = clean_val.split('.')
            mins = int(parts[0]) if parts[0] else 0
            secs = int(parts[1]) if len(parts) > 1 and parts[1] else 0
        else:
            mins, secs = int(clean_val), 0
        return (mins * 60) + secs
    except ValueError:
        return None

# Test function for the arithmetic
def test_time_arithmetic():
    inputs = ["5.5", "3.27", "2.08"]
    expected_seconds = [305, 207, 128]  # Pre-calculated for verification
    total_expected = 640  # Sum of expected_seconds
    
    # Parse each input and collect seconds
    parsed_seconds = []
    for inp in inputs:
        secs = parse_time(inp)
        assert secs is not None, f"Failed to parse {inp}"
        parsed_seconds.append(secs)
    
    # Verify individual parses
    assert parsed_seconds == expected_seconds
    
    # Verify total sum
    total_actual = sum(parsed_seconds)
    assert total_actual == total_expected, f"Expected {total_expected} seconds, got {total_actual}"
    
    # Optional: Test formatted output (using app's format_time logic)
    def format_time(seconds):
        is_neg = seconds < 0
        abs_secs = abs(seconds)
        return f"{'-' if is_neg else ''}{abs_secs // 60}:{abs_secs % 60:02d}"
    
    assert format_time(total_expected) == "10:40"