"""
Toolchain setup for the embedded_computervision project.

Usage inside Jupyter notebooks:
    from config.toolchain.toolchain import check_libraries
    check_libraries()
"""

import importlib

# List of main libraries you’ll actually use (not every minor dep from requirements.txt)
LIBRARIES = [
    "numpy",
    "pandas",
    "matplotlib",
    "cv2",                # opencv-python
    "tensorflow",
    "keras",
    "sklearn",            # scikit-learn
    "skimage",            # scikit-image
    "PIL",                # pillow
    "dotenv",             # python-dotenv
]

def check_libraries():
    print("🔧 Checking toolchain libraries...\n")
    for lib in LIBRARIES:
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "no version attr")
            print(f"✅ {lib:12s} {version}")
        except ImportError:
            print(f"❌ {lib:12s} not installed")
    print("\nDone.")
