<div align="center">

# Paper Relief Art · 纸境浮绘

**Photographs, held in paper.**

Recognizable subjects. Quiet space. Fibers that catch the light.<br>
Pigment that soaks into the sheet instead of sitting on top.

[English](README.md) · [简体中文](README.zh-CN.md)<br>
[Install](#install) · [Two skills](#choose-your-skill) · [Examples](docs/examples.md) · [Art direction](docs/art-direction.md)

</div>

Paper Relief Art turns photographs into Chinese-inspired paper-pulp relief artwork: a photographic core, softly raised fibers, pale absorbed color, and generous warm-paper negative space. Choose a finished editorial poster with type, or an image that lets the paper speak for itself.

## Two scenes, two treatments

| With text · 有字 | Without added text · 无字 |
| :---: | :---: |
| <img src="assets/examples/pine-court-text.png" alt="Pine courtyard paper artwork with the Chinese title 松庭照水 and restrained English typography" width="430"> | <img src="assets/examples/pine-court-no-text.png" alt="Pine courtyard and pond reflections dissolving into ivory paper without typography" width="430"> |
| **松庭照水 · Pine Court Reflections** | **Architecture, fibers, and quiet space** |
| <img src="assets/examples/mountain-lake-text.png" alt="Turquoise mountain lake paper poster titled 碧水涵山 with light serif lettering" width="430"> | <img src="assets/examples/mountain-lake-no-text.png" alt="Mountain peaks and a pine peninsula above clear turquoise water with sparse pigment absorption at the paper edge" width="430"> |
| **碧水涵山 · Mountains Mirrored in Blue** | **Clear water, pale pigment, and open paper** |

These are purpose-made illustrative scenes. See the [source images and example notes](docs/examples.md). Each artwork is a separate file; the gallery simply presents the two options.

## What gives it its character

- **A recognizable core.** Preserve the important structure, proportion, color, and relationships in the input.
- **Space before texture.** A portrait poster starts with about 60% quiet paper; subject scale and intended use shape the final composition.
- **Paper-pulp relief.** Local fibers, shallow ridges, thin torn sheets, and subtle side-lit shadows belong to the paper surface.
- **Pale, scarce, spacious color.** Sample the nearest subject: tree green beside trees, water blue beside water. Let diluted pigment enter fibers and nearby paper, with visible white intervals.
- **Titles with a reason to exist.** The text version compares several source-grounded Chinese titles, then locks the wording before drawing light editorial typography.

[Read the art direction →](docs/art-direction.md)

## Choose your skill

| Skill | Use it for |
| --- | --- |
| [`paper-relief-art-text`](skills/paper-relief-art-text/SKILL.md) | Posters, covers, and cultural visuals with a considered Chinese title, optional English, and restrained editorial typography. Also works for title suggestions alone. |
| [`paper-relief-art-no-text`](skills/paper-relief-art-no-text/SKILL.md) | Artwork, cover backgrounds, and illustrations without added typography. Original signs or inscriptions remain unless you explicitly ask to remove them. |

Both skills are self-contained. Install either one or both; there is no third router skill.

## Install

### With the Skills CLI

Requires Node.js and npm. Install both skills for Codex:

```sh
npx skills add Ellventequila/paper-relief-art --agent codex --global --skill paper-relief-art-text paper-relief-art-no-text
```

Or install one:

```sh
npx skills add Ellventequila/paper-relief-art --agent codex --global --skill paper-relief-art-no-text
```

The installer is the independent [Skills CLI](https://github.com/vercel-labs/skills). Install to another compatible agent by choosing its supported `--agent` value; the image-generation requirement below still applies.

### Manual installation

1. Download this repository with **Code → Download ZIP**, or clone it.
2. Copy the complete `skills/paper-relief-art-text` and/or `skills/paper-relief-art-no-text` folder into your skill directory. Keep each folder's `SKILL.md`, `agents/`, and `references/` together.
3. For current Codex local discovery, the user-level directory is `~/.agents/skills/` (`%USERPROFILE%\.agents\skills\` on Windows). Use the skill location configured by your client if it differs. Avoid installing the same skill name into multiple scanned directories.
4. Open a new session if the skills do not appear.

See the official [Codex skill documentation](https://developers.openai.com/codex/skills/) for discovery and installation details. Save local customizations before replacing an existing installation.

## First use

Attach a photograph, then invoke the version you want:

**Without added text**

```text
Use $paper-relief-art-no-text to turn this photograph into a 3:4 paper-relief artwork.
Preserve the recognizable subject, leave generous quiet paper, and keep edge pigments pale and sparse.
Do not add typography.
```

**With a considered title**

```text
Use $paper-relief-art-text to create a 3:4 paper-relief poster from this photograph.
Choose a concise Chinese title grounded in the visible scene, with a small English interpretation.
Keep the type light, the paper spacious, and the absorbed pigments subtle.
```

**A fixed title, Chinese only**

```text
Use $paper-relief-art-text. The title is 松庭照水.
Use Chinese only: no English, numbers, or captions. Preserve the subject and generous paper space.
```

**Title ideas only**

```text
Use $paper-relief-art-text to suggest three Chinese titles with brief visual reasons.
Do not generate an image.
```

Specify a different aspect ratio, text policy, subject treatment, or output folder whenever needed. Your explicit request takes precedence over the defaults. [中文示例 →](README.zh-CN.md#开始使用)

## How it works

The agent reads the image, identifies what must remain, organizes the subject against open paper, and places only a few fiber-to-pigment transitions. The text skill adds candidate selection and an exact wording pass before rendering. After generation it inspects composition, subject fidelity, material behavior, and text separately, then makes a focused correction if needed.

The reusable guidance is split into [material direction](skills/paper-relief-art-text/references/art-direction.md), [prompt organization](skills/paper-relief-art-text/references/prompt-guide.md), and [title selection](skills/paper-relief-art-text/references/title-writing.md). The skill instructions are in Chinese; requests can be written in English or Chinese.

## Requirements and boundaries

Use an agent environment that can view input images and generate or edit images. The skills supply art direction, not an image model, API service, or renderer. A text-only agent can prepare a prompt or title, but cannot produce the final bitmap by installing these files alone.

The examples were made in an environment with image editing available. Image results vary by tool and input. Chinese typography and precise subject preservation need visual review; edits are not guaranteed to be pixel-identical. Other agents are not claimed to have passed image-output testing.

This is a visual reinterpretation workflow, not documentary photo restoration. Use source material you have permission to adapt and share. No separate runtime package is required by the skill itself.

## Contribute

Good feedback includes the requested treatment, a permitted source image, the result, and the specific mismatch: subject, space, fibers, pigment, or type. English and Chinese issues are welcome. See [contributing](CONTRIBUTING.md) and the [visual review cases](tests/title-cases.md).

If the project helps your work, a star makes it easier for others to find. Contributions that improve a real visual result are especially welcome.

## License

Skill instructions, scripts, and documentation: [MIT](LICENSE). Images under `assets/examples/` are excluded from that license and are provided for demonstration. See [image usage](assets/examples/README.md).
