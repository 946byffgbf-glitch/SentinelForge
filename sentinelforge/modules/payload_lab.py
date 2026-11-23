"""Benign training strings for validating output encoding in a local demo."""

def harmless_markers():
    return {"html_text":"SF_TEST_MARKER: <b>text</b>",
            "script_text":"SF_TEST_MARKER: alert text is not executed",
            "sql_text":"SF_TEST_MARKER: ' OR 'x'='x (display-only; do not submit)",
            "csrf_note":"Use a local demo form and verify anti-CSRF token enforcement manually."}
