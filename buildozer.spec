[app]
title = My Game
package.name = mygame
package.domain = org.yourname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,ogg
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1