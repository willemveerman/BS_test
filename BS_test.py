# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:14:50 2014

@author: willem
"""

from bioservices import *

class Features():
    def __init__(self,id):  
        self.id = id
        
        list_of_genes = []
        
        f = open(id,"r")
        
        for line in f:
            list_of_genes.append(line.strip())
        
        f.close()
            
        self.list=list_of_genes
        
    def __str__(self):
        return "Takes a list of protein names and outputs a file containing each proteins' GO terms."
        
    def items(self):
        """ Return the file's constituents as a list"""
        
        return self.list
    
    def conv_to_up(self,organism):
        """Convert KEGG gene names to UniProt IDs"""
        
        uniprot_IDs_list = []
        
        kegg_class = KEGGParser()
        
        for i in self.list:
            gene_kegg_entry = kegg_class.get(organism+":"+i)
            try:
                parsed_entry = kegg_class.parse(gene_kegg_entry)
            except AttributeError:
                pass
            uniprot_IDs_list.append(str(parsed_entry['dblinks']['UniProt']))
        
        return uniprot_IDs_list
        
    def file_up(self,filename,organism):
        """Creates a text file containing each gene with its corresponding UniProt IDs."""
        
        f=open(filename,"w")
        
        gene_list= self.list
        
        up_list = self.conv_to_up(organism)
        
        for i, gene in enumerate(gene_list):
            f.write(gene+" "+up_list[i]+"\n")
                
        f.close()
        
    def parser(self):
        """ Parses a file containing a list of genes, separated by newlines."""
        list_of_genes = []
        
        f = open(self,"r")
        
        for line in f:
            list_of_genes.append(line.strip())
            
        return list_of_genes

#    def uniprot_id(self,organism):
#        """ UniProt IDs for a list of KEGG Gene IDs.    
#        """
#        kegg_class = KEGGParser()
#        gene_kegg_entry = kegg_class.get(organism:self)
#        parsed_entry = kegg_class.parse(gene_kegg_entry)
#        uniprot_id = str(parsed_entry['dblinks']['UniProt'])
#        
#
#    def go_attributes(self):
#        """Uses BioServices to query QuickGO Gene Ontology database.
#        
#            Returns a Pandas.DataFrame, displaying only columns 4 & 5.
#            
#        """
#        #Initialize BioServices QuickGO object
#        bioservices_quickgo_obj = QuickGO()
#        #Search QuickGO for protein UniProt ID
#        res = bioservices_quickgo_obj.Annotation_from_protein(protein=str(Features.part_attrib(self,'uniprot_id')))
#
#        #Use Pandas.DataFrame method object iloc to select specific columns
#        print res.iloc[:,[4,5]]


#test2
