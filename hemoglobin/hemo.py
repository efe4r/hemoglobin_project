from Bio.PDB import PDBList, PDBParser, Superimposer
import os
import py3Dmol

# ---------- 1️⃣ Hemoglobin PDB ID ----------
pdb_id = "1A3N"  # Human hemoglobin

# ---------- 2️⃣ Directory to save PDB file ----------
save_dir = "."  # Current script directory
os.makedirs(save_dir, exist_ok=True)

# ---------- 3️⃣ Download PDB file ----------
pdbl = PDBList()
pdbl.retrieve_pdb_file(pdb_id, pdir=save_dir, file_format="pdb")

# ---------- 4️⃣ Analyze chains and residues ----------
pdb_file = os.path.join(save_dir, "pdb1a3n.ent")
parser = PDBParser()
structure = parser.get_structure("hemoglobin", pdb_file)

chain_info = {}
print("Chains and number of amino acids:")
for model in structure:
    for chain in model:
        residues = list(chain.get_residues())
        chain_info[chain.id] = residues
        print(f"Chain {chain.id}: {len(residues)} residues")

# ---------- 5️⃣ Calculate RMSD between chains ----------
print("\nRMSD between chains (C-alpha atoms):")
chains = list(chain_info.keys())
for i in range(len(chains)):
    for j in range(i+1, len(chains)):
        chain1 = chain_info[chains[i]]
        chain2 = chain_info[chains[j]]
        
        # Select only C-alpha atoms
        ca1 = [res['CA'] for res in chain1 if 'CA' in res]
        ca2 = [res['CA'] for res in chain2 if 'CA' in res]
        
        # Use minimum length for RMSD
        length = min(len(ca1), len(ca2))
        sup = Superimposer()
        sup.set_atoms(ca1[:length], ca2[:length])
        rmsd_value = sup.rms
        print(f"RMSD between chain {chains[i]} and {chains[j]}: {rmsd_value:.2f} Å")

# ---------- 6️⃣ Amino acid composition ----------
polar_residues = ['SER','THR','ASN','GLN','TYR','CYS','HIS']
nonpolar_residues = ['ALA','VAL','ILE','LEU','MET','PHE','TRP','PRO','GLY']
charged_residues = ['ARG','LYS','ASP','GLU']

polar_count = 0
nonpolar_count = 0
charged_count = 0

for residues in chain_info.values():
    for res in residues:
        res_name = res.get_resname()
        if res_name in polar_residues:
            polar_count += 1
        elif res_name in nonpolar_residues:
            nonpolar_count += 1
        elif res_name in charged_residues:
            charged_count += 1

print("\nAmino acid composition:")
print(f"Polar residues: {polar_count}")
print(f"Nonpolar residues: {nonpolar_count}")
print(f"Charged residues: {charged_count}")

# ---------- 7️⃣ 3D Visualization and HTML export ----------
with open(pdb_file, "r") as f:
    pdb_data = f.read()

view = py3Dmol.view(width=1600, height=1000)
view.setBackgroundColor('white')
view.addModel(pdb_data, 'pdb')
view.setStyle({'cartoon': {'color':'spectrum'}})  # Chains in spectrum colors
view.setStyle({'resn':'HEM'}, {'stick':{'color':'red'}})  # Heme groups in red
view.zoomTo()

html_file = os.path.join(save_dir, "hemoglobin_3d.html")
html = view._make_html()
with open(html_file, "w") as f:
    f.write(html)

print(f"\n3D visualization saved as {html_file}")
print("Open the HTML file in a browser to explore the 3D hemoglobin model interactively.")

# ---------- 8️⃣ Research summary ----------
print("\nResearch Summary:")
print("""
In this project, the human hemoglobin protein was analyzed. The number of amino acids in each chain was calculated.
Structural differences between chains were evaluated using RMSD based on C-alpha atoms.
Amino acids were categorized as polar, nonpolar, or charged. 
Heme groups were highlighted in red in the 3D visualization.
The resulting figures and analyses provide visual and quantitative insights into hemoglobin's structure and functional regions.
""")
