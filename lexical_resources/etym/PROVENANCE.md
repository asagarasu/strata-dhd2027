# etym/ — etymological chain resources (word-latent instrument v1)
*Vendored #52, 2026-07-19 night. Payloads UNTRACKED per house
convention (shas here; fetch commands below). All open/PD; all far
under her 1GB relay threshold.*

| file | sha256[:16] | what | source |
|---|---|---|---|
| skeat_etymological_raw.txt | 1ff610c4598996e8 | Skeat, *An Etymological Dictionary of the English Language* (PD; body OCR clean, front-matter noise) | archive.org/download/etymologicaldict00skeauoft/…_djvu.txt |
| grc.lsj.perseus-eng11.xml | d4d49ef5bb84a4e0 | LSJ segment — **kappa range; contains καλχαίνω** (key `kalxai/nw`, entry prints "(ka/lxh) prop. make purple" — the founding chain) | raw.githubusercontent.com/PerseusDL/lexica/master/CTS_XML_TEI/perseus/pdllex/grc/lsj/grc.lsj.perseus-eng11.xml |
| grc.lsj.perseus-eng10/12/13.xml | a754c36f… · e835c276… · 4502e400… | neighboring LSJ segments (mu region etc.; kept for coverage) | same repo, same path pattern |

Betacode note: LSJ keys/orths are betacode (καλχαίνω = `kalxai/nw`;
accents as `/` `=` `\`). The grc module must transliterate or match
betacode — do not grep unicode Greek against these files.

Refetch: `curl -sL <source url> -o <file>` — no auth, no rate
issues observed 07-19.
