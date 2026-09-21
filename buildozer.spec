[app]

title = Simple Calculator

package.name = simplecalculator
package.domain = org.malekul

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 35

android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a

android.sdk_path = /usr/local/lib/android/sdk

android.accept_sdk_license = True

android.skip_update = True

android.allow_backup = True


[buildozer]

log_level = 2

warn_on_root = 1
