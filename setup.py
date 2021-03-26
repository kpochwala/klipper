import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

c_helper = setuptools.Extension('klippy/chelper/c_helper',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    sources = [ 'klippy/chelper/itersolve.c',
                                'klippy/chelper/kin_cartesian.c',
                                'klippy/chelper/kin_corexy.c',
                                'klippy/chelper/kin_delta.c',
                                'klippy/chelper/kin_extruder.c',
                                'klippy/chelper/kin_polar.c',
                                'klippy/chelper/kin_rotary_delta.c',
                                'klippy/chelper/kin_winch.c',
                                'klippy/chelper/pyhelper.c',
                                'klippy/chelper/serialqueue.c',
                                'klippy/chelper/stepcompress.c',
                                'klippy/chelper/trapq.c' ])

setuptools.setup(
    name = 'klipper',
    version="0.9.0",
    author="KevinOConnor",
    description = 'Klipper 3D Printing Firmware',
    packages=setuptools.find_packages(),
    ext_modules = [ c_helper ],
    install_requires = [ "greenlet", "cffi" ],
    entry_points = { "console_scripts": [ "klippy = klippy.klippy:main" ] },
    url = "https://www.klipper3d.org/",
    python_requires='>=3.5',
)
