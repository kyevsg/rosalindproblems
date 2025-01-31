// Transcribing DNA into RNA

fn transcription(dna_string: &str) {
    /*
    This function transcribes a DNA sequence to an RNA one.

    Input: a DNA string
    Prints: the corresponding RNA string
    */
    let rna_string = dna_string.replace("T", "U"); // replace T nucleotides with U
    print!("{}", rna_string);
}
