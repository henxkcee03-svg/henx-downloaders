[app]

# ---- App identity ----
title = Henx Downloader
package.name = henxdownloader
package.domain = org.henx

# ---- Source ----
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# ---- Requirements ----
# Trimmed to packages with reliable Android build recipes.
# pycryptodomex / brotli / websockets / mutagen were removed: they're
# optional yt-dlp extras with no working python-for-android recipe under
# those names, and were the cause of the first build failure.
#
# python3 AND hostpython3 are both pinned to 3.11.8. Buildozer builds
# two separate Pythons — one that runs during the build itself
# (hostpython3) and one that ships on the phone (python3) — and they
# must match exactly. Pinning only python3 left hostpython3 to default
# to a bleeding-edge 3.14.2, which is what caused the "should have
# same version as hostpython3, 3.11.8 != 3.14.2" failure. Both are
# pinned now so they match.
# plyer added for the native Android share sheet ("Share App"). It's a
# widely-used, well-supported recipe in python-for-android (unlike the
# pycryptodomex/brotli/websockets packages removed earlier, which had no
# working recipe) — this shouldn't reopen the earlier build issues.
requirements = hostpython3==3.11.8,python3==3.11.8,kivy==2.3.0,plyer,yt-dlp,certifi,chardet,idna,urllib3,requests

orientation = portrait
fullscreen = 0
# icon.png — a dark, glowing rounded badge (near-black gradient
# background, thin blue-to-teal rim) with a download arrow + tray
# glyph, matching the Android status-bar download icon. Buildozer
# resizes it for the various Android icon densities automatically.
icon.filename = %(source.dir)s/icon.png

# presplash — the screen shown for a split second while the app is
# launching. Previously left unset, so Android fell back to a default
# blank/placeholder splash that didn't match the real app icon. Using
# the same icon here so launch and home-screen icon are consistent.
presplash.filename = %(source.dir)s/icon.png
android.presplash_color = #0e1016

# ---- Android permissions ----
# INTERNET: required to download.
# Storage permissions were removed: the app writes to its own app-specific
# external directory (getExternalFilesDir), which needs no runtime
# permission on any Android version -- unlike /sdcard/Download, which
# Android 10+ blocks direct writes to regardless of permission grants.
android.permissions = INTERNET

# ---- Android build config ----
android.api = 33
android.minapi = 21
android.ndk = 25b
# Building one architecture first to prove the build works and to keep
# build time down. Add ", armeabi-v7a" back once this succeeds if you
# need to support older 32-bit devices too.
android.archs = arm64-v8a
android.allow_backup = True

# ---- Bundled ffmpeg (EXPERIMENTAL) ----
# Populated by the GitHub Actions workflow's "Fetch prebuilt ffmpeg" step
# before this build runs. Files here get installed into the APK's native
# library directory, which is the one place Android allows a bundled
# binary to actually execute from (Android 10+ blocks running anything
# extracted to the app's own storage at runtime) -- hence the lib*.so
# naming even though ffmpeg itself isn't really a shared library.
# If that workflow step didn't find a release asset, this directory is
# empty and the line below simply matches nothing; the app already
# handles a missing ffmpeg without crashing.
android.add_libs_arm64_v8a = libs/android-v8/*.so
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
