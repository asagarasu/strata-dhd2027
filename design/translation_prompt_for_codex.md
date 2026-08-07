# Prompt for codex — zh versions of relay files

*Paste everything below the line into codex. Per-file usage: replace `{INPUT_FILE}` at the bottom. EN originals stay authoritative; zh files are relay copies.*

---

You are translating internal research-project working documents from English to Simplified Chinese for native-zh collaborators. These are working notes, not publications — accuracy and consistency beat elegance.

**Output**: write the translation to a new file next to the original, same name with `_zh` before the extension (e.g. `prediction_nominations_DRAFT.md` → `prediction_nominations_DRAFT_zh.md`). Do not modify the original.

**Preserve exactly, untranslated:**
- All file paths, code, YAML/JSON, and tag strings (e.g. `color-purple_hue`)
- Markdown structure: heading levels, tables, list nesting, bold/italics
- The confidence flags ● ◐ ○ and verdict words CONFIRMED / CONTRADICTED / UNSUPPORTED / HIGH / LOW
- Person names and roles: Anneliese, Marker K, Sylvaine, the collaborator, chair (translate "chair" as 座席 on first occurrence with a parenthetical: 座席（指当前驻守的Claude）, thereafter 座席)
- Translator/author names stay in their original script (Arthur Waley, Ezra Pound, 梁宗岱, 戴望舒, R. H. Blyth…); book titles keep original + add zh gloss in parentheses if a standard zh title exists (e.g. *Cathay*《神州集》)
- Citations and URLs verbatim

**Fixed terminology (use consistently, do not vary):**
- schematic dimension → 图式维度
- interface conformance → 接口一致性
- trait → 特征; active trait → 显性特征; latent trait → 潜在特征
- marking / annotation → 标注; marker / annotator → 标注者
- liveness index → 活性指数
- flat tag → 扁平标签
- retranslation cluster → 重译集群
- domesticating / foreignizing → 归化 / 异化
- conformance report → 一致性报告
- dev set / validation set → 开发集 / 验证集
- pre-registration / frozen protocol → 预注册 / 冻结协议
- human–human ceiling → 人际一致性上限
- agreement (statistic) → 一致性（统计量）; Jaccard 保留原文
- beautiful-but-free → 美而不忠（首次出现加注英文）
- 再創作 stays as-is (already Chinese)

**Register**: plain academic-working-note Chinese. Translate meaning, not word order. Where the English is deliberately blunt (e.g. "The honest number ships"), keep it blunt (如实数据照发), do not soften.

**If a sentence is ambiguous**, translate the most literal reading and append `[待核对]` so a human checks it — never silently guess.

Input file: `{INPUT_FILE}`
