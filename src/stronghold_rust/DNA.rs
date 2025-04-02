// Counting DNA Nucleotides

use std::collections::HashMap;

fn dna_count(dna_string: &str) {
    /*
    This function counts the number of each type of nucleotide within a DNA sequence.

    Input: a DNA string
    Prints: the counts of A, C, G, and T within the DNA string as four integers separated by spaces
    */
    let mut nuc_map = HashMap::new(); // creating hash map to store nucleotide counts
    for nuc in dna_string.chars() { // iterating over DNA string 
        let counter = nuc_map.entry(nuc).or_insert(0);
        *counter += 1
    }
    let mut sorted: Vec<_> = nuc_map.iter().collect(); // going to sort the keys
    sorted.sort_by_key(|a| a.0);
    for (key, value) in sorted.iter() { // possibility to improve this later
        print!("{} ", value);
    }
}
