import os
import arguably 
import pyprofilers as pp
import pandas as pd
@pp.profile(sort_by='cumulative', out_lines=30) 
@pp.profile_by_line(exit=1) 
@pp.simple_timer(num=1)
snap = CodeSnap()
snap = CodeSnap(tracer="python") 
snap.start()
@arguably.Command
def trinityAnnotateDraw(transcripts_path = FALSE)
"""
a gff parser for the trinity transcipt predictions 
and annotations for the transcript structuve visualization. 
Given a transcript assembly file, it will make the tab 
delimited file for the coordinates transcript. This will 
prepare all the coordinates tuples and you can use them 
to view in mauve or the genome visualization kit.
"""
if transcripts_path:
    trascripts_path = os.path.join(os.getcwd(), transcripts_path)
fasta_names = []
start = []
end = []
strand = []
length = []
names_draw = []
species_name = ""
while True:
    take_species = input("Please enter the species names for the transcript map")
    species_name += take_species
    if take_species == "":
        break
with open("transcripts_path","r") as transcripts:
    for line in transcripts.readlines():
        if line.startswith(">"):
            fasta_names.append(line.strip().replace(">",""))
        else:
            pass
for i in range(len(fasta_names)):
    start.append(list(filter(lambda n: n !=  "-",re.findall(r'[0-9]{0,3}-[0-9]{0,6}',fasta_names[i])))[0].split("-")[0])
    end.append(list(filter(lambda n: n != "-",re.findall(r'[0-9]{0,3}-[0-9]{0,6}',fasta_names[i])))[0].split("-")[1])
    strand.append(fasta_names[i].split()[-1][-2])
    length.append(fasta_names[i].split()[4].split(":")[-1])
    names.append(fasta_names[i].split()[1].split("_")[1])
start_end_strand = [(i,j,k) for i,j,k in zip(start, end, strand)]
start_end_strand_tu = tuple(start_end_strand)
with open("save_coordinates_visualization.txt", "w") as write_gff:
    write_gff.write(f"The coordinates for the transcript structure are given below from the transcriptome assembly")
    write_gff.write("\n")
    write_gff.write(f"{names} \t{start} \t{end} \t{strand}")
    write_gff.write("\n")
    write_gff.write(f"the formatted tuples for the coordinates are:")
    write_gff.write(f"{start_end_strand}")
    write_gff.close()
snap.stop()
snap.save()
if __name__ == "__main__":
    arguably.run()
