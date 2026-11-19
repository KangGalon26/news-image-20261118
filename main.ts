// Wednesday 18 November 2026 — world news in one image.
// Entry program for make.fun bounty news-image-20261118.
// It places the newspaper front page drawn for this day, entry.png,
// into the grader's output directory. Node 22, standard library only.
// No network, no randomness: every run writes the same bytes.
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
const image = readFileSync(join(here, "entry.png"));
writeFileSync(target, image);
console.log(`wrote ${target} (${image.length} bytes)`);
