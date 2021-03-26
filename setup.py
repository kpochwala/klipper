import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'klipper',
    version="0.9.0",
    author="KevinOConnor",
    description = 'Klipper 3D Printing Firmware',
    packages=setuptools.find_packages(),
    entry_points = { "console_scripts": [ "klippy = klippy.klippy:main" ] },
    url = "https://www.klipper3d.org/",
    python_requires='>=3.5',
)