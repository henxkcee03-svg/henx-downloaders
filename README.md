# Henx Downloader

An Android app (built with Kivy + yt-dlp) for downloading video/audio from
supported sites, with a queue for multiple simultaneous downloads.

## Building

This repo builds automatically via GitHub Actions on every push to `main`
(see `.github/workflows/build.yml`). The resulting `.apk` is attached as a
downloadable artifact on the corresponding Actions run.

To build locally instead:

```bash
pip install buildozer
buildozer android debug
```

## Notes

- Downloads are saved to the app's own storage directory (no special
  Android permission required), visible via the in-app Share button or a
  file manager under `Android/data/org.henx.henxdownloader/files/Download`.
- **Best quality + MP3 (EXPERIMENTAL).** The build workflow fetches a
  prebuilt Android ffmpeg binary and bundles it into the APK so "Best"
  quality can merge separate video+audio streams, and audio downloads can
  convert to real `.mp3`. This relies on a trick (disguising the binary as
  a `.so` library) to get around an Android 10+ restriction on running
  bundled executables, and hasn't been verified on a real device build yet
  -- if it doesn't work, or the ffmpeg release asset the workflow looks for
  ever moves/disappears, the app automatically falls back to single-file
  downloads (quality capped, audio kept in its original format like m4a)
  rather than crashing.
