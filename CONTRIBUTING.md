# Contributing · 参与完善

Improve a decision, then show the visual consequence. English and Chinese contributions are welcome.

## Report a mismatch

Include the skill version, agent and image tool if known, the exact request, a source image you may share, and the result. Explain one concrete issue: incorrect structure, crowded paper, heavy material, excessive pigment, a weak title, or a typography error. If you cannot publish the source, describe it rather than upload it.

Do not post private photos, credentials, or other people's images without permission. New gallery entries need source and usage information.

## Suggest a change

Keep each change focused. Preserve the subject and all already successful parts when testing a material or typography correction. Compare results on more than one subject before turning a one-image preference into a universal rule.

Both skills contain identical shared references so either can be installed alone. Synchronize changes to shared guidance across the two copies. Title selection and material direction are evaluated by visual and language review, not a fixed answer or a self-awarded score.

Run the package check from the repository root:

```sh
python scripts/validate.py
```

This checks package structure, UTF-8 text, local links, shared references, and gallery image files. It does not judge beauty or prove stable image generation. Use [title cases](tests/title-cases.md) and [pigment cases](tests/pigment-cases.md) for human review.

## 中文说明

一次改一个具体问题，并说明修改前后的视觉影响。反馈可包含调用版本、工具、实际请求、可公开素材与成图。无法公开素材时，用文字描述，不上传未经允许的图片。

共享参考文件在两个技能内各保留一份，请同步修改。检验结构可运行上面的命令；审美、题名与图像稳定性仍需实际看图、读文案。提交展示作品时说明来源和许可，不把单次结果写成普遍保证。
