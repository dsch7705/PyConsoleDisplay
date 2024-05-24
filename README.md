# PyConsoleDisplay
 Wrapper for win32console module enabling double-buffering and quality of life methods.

## Double-buffering
 All draw functions are called on the back buffer; the `flip()` function must be called to set the back buffer to the active buffer and display changes made.
