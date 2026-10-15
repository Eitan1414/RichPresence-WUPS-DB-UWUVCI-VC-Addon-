# Wii U Rich Presence — VC Injection Add-on Database

Community fork of [FlamingNineteen/RichPresenceWUPS-DB](https://github.com/FlamingNineteen/RichPresenceWUPS-DB), intended to keep the original Wii U game image database **and** provide optional cover art for custom Virtual Console (VC) injections made with tools such as Cafe Inject Studio or UWUVCI.

> [!IMPORTANT]
> **Unofficial project.** Not affiliated with, endorsed by, or maintained by FlamingNineteen or the Wii U Rich Presence developers. The upstream database deliberately **does not accept VC injections**. Additions for injections belong in **this fork**, not in upstream pull requests.

## Current status

- ✅ Fork of the original database; original `titles.json` and `icons/` retained.
- ✅ Existing official Wii U and official Virtual Console entries preserved.
- 🧪 Custom VC injection additions are **planned / experimental**. No injection is automatically supported merely because this fork exists.
- 🧪 Cafe Inject Studio automatic publishing is **not yet implemented**.
- ✅ No Wii U plugin modification is expected solely to select a different image database, but injection-name detection still needs real-device testing.

## How the database works

The [Wii U Rich Presence plugin](https://github.com/FlamingNineteen/RichPresenceWUPS) communicates with its companion application on your computer, which uses the game title to look up an icon.

- `titles.json`: maps the game's **exact reported title** to a filename.
- `icons/`: contains the referenced JPEG images.
- Entries for unofficial injections should use a distinctive filename and must not overwrite an existing game's icon.

Example (illustrative only — not an included game):
```json
{
  "Example VC Injection": "vc_example.jpg"
}
```
This entry requires `icons/vc_example.jpg` to exist. The key must match the title actually received by WURP; the title shown in the injection builder may not always be identical.

## Using this fork with WURP

Install the official Wii U plugin and the WURP desktop companion according to the [upstream installation instructions](https://github.com/FlamingNineteen/RichPresenceWUPS#installation). With Discord running, start the desktop companion using its supported `repo` argument (the documented `--repo` form also exists):

```powershell
.\WURP-Windows.exe repo Eitan1414/RichPresence-WUPS-DB-UWUVCI-VC-Addon-
```

Or for the Python companion:
```bash
python3 discord-script.py repo Eitan1414/RichPresence-WUPS-DB-UWUVCI-VC-Addon-
```

These commands **select this fork as the image repository**. They do not install VC injections, add games automatically, or guarantee that every custom title will be recognized. If an injection does not display, inspect the companion application's reported game title first.

## Adding a VC injection manually

1. Create your own VC injection using legally obtained game content.
2. Locate the injection's `meta/meta.xml`; read its `longname_en` value. If available, compare this with the title reported by the running desktop companion.
3. Create a **512 × 512 pixel JPEG** of its icon, for example `icons/vc_example.jpg`. Avoid reusing an existing image filename.
4. Add a mapping to `titles.json`: `"Exact Game Name": "vc_example.jpg"`. Keep the JSON valid and existing mappings intact.
5. Commit both the JSON change and the JPEG to **this repository**, then restart WURP and test it.

Names must match exactly, including punctuation, case, spaces, and special characters.

## Planned Cafe Inject Studio integration

The intended workflow is:

1. Read the injection's title and icon from its metadata.
2. Preview/edit the proposed title and cover art.
3. Detect an existing mapping or icon collision.
4. Add or update the entry in a local copy of `titles.json` and save a 512 × 512 JPEG.
5. Publish those changes to this fork through an explicit, authenticated GitHub workflow.

**Do not embed GitHub personal access tokens in distributed installers or upload private game files.** Only metadata and cover art should be published.

## Compatibility and limitations

- Official Wii U/VC titles: existing upstream entries are retained.
- Custom Wii U-format VC injections: intended target; detection is **unverified until tested**.
- Wii games launched in vWii, GameCube titles through Nintendont, homebrew and system applets: no expanded support is promised by this database fork.
- Name collisions: two different injections with the same reported title will share one mapping. Solving this requires further design and possibly changes outside the database.

## Maintaining the fork

Keep additions here, and periodically sync changes from [the upstream repository](https://github.com/FlamingNineteen/RichPresenceWUPS-DB). Review merge conflicts in `titles.json` carefully so that neither upstream mappings nor your own injections get lost.

This repository retains upstream material and credits its original maintainers. See the [upstream project](https://github.com/FlamingNineteen/RichPresenceWUPS-DB) for its original contribution documentation.
