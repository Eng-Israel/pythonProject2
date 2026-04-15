[app]
title = Crop AI
package.name = cropai
package.domain = org.engisrael
source.dir = .
source.include_exts = py,h5
requirements = python3,kivy,numpy,pillow,tensorflow
orientation = portrait
fullscreen = 1
version = 1.0.0

# Permissions your app may need
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Entry point
main.py

[buildozer]
log_level = 2
warn_on_root = 1
