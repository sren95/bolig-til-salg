import { readdir, writeFile } from "node:fs/promises";
import path from "node:path";

const galleryDir = path.join(process.cwd(), "assets", "gallery");
const outputPath = path.join(galleryDir, "gallery-manifest.json");
const allowedExtensions = new Set([".jpg", ".jpeg", ".png", ".webp", ".avif"]);

const files = (await readdir(galleryDir))
  .filter((file) => allowedExtensions.has(path.extname(file).toLowerCase()))
  .sort((a, b) => a.localeCompare(b, "da", { numeric: true }));

const manifest = files.map((file, index) => ({
  src: `assets/gallery/${file}`,
  label: `Billede ${index + 1} af ${files.length}`
}));

await writeFile(outputPath, `${JSON.stringify(manifest, null, 2)}\n`);
console.log(`Wrote ${manifest.length} gallery images to ${outputPath}`);
