class basicItems(object):
    """Establishes the framework for items found in player inventory"""
    def __init__(self,name,description,uses):
        self.Itemname=name
        self.ItemDesc=description
        self.itemUses=uses


#creating the murderer items, could be placed in main file but going here for now for testing 
#Addendum: decided to create it in the class file instead
#"Pillow","Gun","Knife"
#Knife=basicItems("Knife","BLABLABLA THIS IS A TEST DESCRIPTION",2)
#Gun=basicItems("Gun","BLABLABLA THIS IS A TEST DESCRIPTION",3)
#Pillow=basicItems("Pillow","BLABLABLA THIS IS A TEST DESCRIPTION",1)



