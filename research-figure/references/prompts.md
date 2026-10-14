# GPT Image 提示词骨架

填入当前研究内容，删除不适用项。科学关系来自证据，生成图负责视觉表达。

## 完整设计稿

```text
Create a scientific figure for [paper / talk], at [aspect ratio / target size].
Reader: [audience]. Main takeaway: [one defensible contribution].
Show [input / real example], [essential mechanism], and [output / real result].
Make [novel operation or representation] the visual focus; keep [routine context] compact.
Reading order and connections: [explicit object-to-object relations and arrow meanings].
Use concrete visual objects or transformations for [concepts]; keep labels short.
Exact labels: [small inventory]. Leave room for editable labels in [regions].
Style: [reference-backed palette, stroke treatment, illustration style, background].
Include only [necessary content]. Omit [nonessential detail / decoration].
Quantitative panels: [use supplied authentic data image as specified / reserve space].
Do not invent metrics, plots, mechanisms, or experimental evidence.
Attached references: [which controls structure, which controls style].
This is a visual draft for later editable reconstruction in [Figma / PowerPoint].
```

数字图优先由数据工具制作并在编辑阶段组合，生成模型不能代替数值绘图。不要先编造“看起来像结果”的图再修正。

## 独立局部插图

```text
Generate only [specific object / scene] for panel [role].
It represents [scientific meaning]; show exactly [required visual details].
Match the attached figure's [viewpoint, proportions, palette, line weight, shading].
Composition: [bounds, facing direction, separation and safe margin].
Background: [transparent / matching solid background].
No labels, letters, arrows, panel frame, or extraneous objects.
This is an illustrative schematic, not an experimental observation.
```

生成后实际打开素材，核对部件数量、方向、语义和透明边缘。已有认可原图局部时，优先复用以保持一致性。

## 定向修改

只描述要改的区域、原因和具体目标，明确保持已正确的关系与对象。整图逻辑正确后，文字、连线和对齐通常在 Figma / PPT 中更容易精确修正。
