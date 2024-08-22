    # ... (code remains the same)
    # ... (code remains the same)
    # ... (code remains the same)
    if len(args) not in [2, 4]:
```python
"""Image loader module"""

import logging

def load_image(self):
    """Loads an image and logs its dimensions."""
    logging.info("Image loaded with dimensions %dx%d", self.width, self.height)
