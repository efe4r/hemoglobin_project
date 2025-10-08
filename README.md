# Human Hemoglobin Structural Analysis

**Author:** Efe Can Orhan

---

## 🌟 Project Overview

This project focuses on the **computational analysis and 3D visualization of human hemoglobin** (PDB ID: `1A3N`). Hemoglobin is a vital protein responsible for oxygen transport in the bloodstream. Understanding its structure, amino acid composition, and inter-chain variations is critical in molecular biology, bioinformatics, and biomedical research.

The project integrates **Python programming, structural bioinformatics, and interactive 3D molecular visualization** to provide a comprehensive analysis pipeline. It is designed to be reproducible, educational, and extendable for further computational biology studies.

---

## 🧬 Key Objectives

1. **Structural Analysis**: Determine the number of amino acids per chain and overall protein composition.
2. **Inter-chain Comparison**: Calculate structural differences between chains using **RMSD (Root Mean Square Deviation)** based on C-alpha atoms.
3. **Amino Acid Categorization**: Classify residues into polar, nonpolar, and charged groups to assess biochemical properties.
4. **Interactive 3D Visualization**: Render an interactive 3D model of hemoglobin highlighting chains and functional heme groups using **py3Dmol**.
5. **Educational Insights**: Provide clear, reproducible outputs for learning structural bioinformatics and computational modeling techniques.

---

## 🔹 Features

### 1. PDB Download
- Automatically retrieves the **1A3N hemoglobin structure** from the Protein Data Bank.
- Saves the PDB file locally for further analysis.
- Ensures reproducibility for future projects.

### 2. Chain & Residue Analysis
- Extracts chains from the protein structure.
- Counts the number of residues per chain.
- Provides a summary table printed in the console.

### 3. RMSD Calculations
- Compares chains quantitatively using **C-alpha RMSD**.
- Evaluates structural deviations to identify conformational differences.
- Output can be used for comparative studies or modeling validation.

### 4. Amino Acid Composition
- Categorizes amino acids into:
  - **Polar**: SER, THR, ASN, GLN, TYR, CYS, HIS
  - **Nonpolar**: ALA, VAL, ILE, LEU, MET, PHE, TRP, PRO, GLY
  - **Charged**: ARG, LYS, ASP, GLU
- Provides a numeric breakdown of the protein's biochemical properties.

### 5. 3D Interactive Visualization
- Uses **py3Dmol** to create interactive models:
  - Chains colored in a spectrum gradient.
  - Heme groups highlighted in red for functional emphasis.
- Outputs an **HTML file** that can be explored in any browser.
- Zoom, rotate, and inspect structural details interactively.

---

## 📦 Dependencies

- [Biopython](https://biopython.org/)  
- [py3Dmol](https://pypi.org/project/py3Dmol/)  
- Python ≥ 3.8  

Install dependencies via pip:

```bash
pip install biopython py3Dmol
